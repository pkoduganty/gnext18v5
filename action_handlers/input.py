#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import json
import random
import logging
from datetime import datetime

from action_handlers.session import *
from action_handlers.utils import *
from action_handlers.activity import do_homework, do_activity

from response_generators.messages import *
from response_generators.response import *

from models.common import *
from models.activities import *
from models.mock import sample_announcements, sample_courses, sample_lessons, sample_homeworks

from SPARQLWrapper import SPARQLWrapper, JSON

from googleapiclient.discovery import build

# handle first logon for the day
# handle subsequent logins for the day
# start from where left off since last login if any
def welcome(session, request):
  userContext=getUserContext(request)
  if userContext:
    response_text = random.choice(WELCOME_SECOND_LOGON).format('Susan')
    userContext.last_logon=datetime.now()
  else:
    response_text = random.choice(WELCOME_BASIC).format('Susan')
    userContext=UserContext() # new if one already doesn't exist
      
  return Response(response_text).text(response_text).text(WELCOME_TEXT) \
          .suggestions(WELCOME_SUGGESTIONS).userStorage(userContext.toJson()).build()


def definition(session, request):
  concept = request.get('queryResult').get('parameters').get('concept')
  results = google_kgraph_lookup(concept, ["Thing"])
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  if results and len(results)>0:
    item=results[0]
    card=Card(item.name, item.long_description, 
              subtitle=item.short_description, 
              imageUri=item.imageUri)
    return Response(item.name).card(card).suggestions(["Not relevant"].append(WELCOME_SUGGESTIONS)).build()
  
  response_text=random.choice(CONCEPT_DEFINITION_UNKNOWN).format(concept)
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()

def definition_fallback(session, request):
  concept = request.get('queryResult').get('parameters').get('concept')
  results = google_kgraph_lookup(concept, ["Thing"])  
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  cards=[]
  if results and len(results)>0:
    for item in results:
      card=Item(item.name, item.long_description, 
              imageUri=item.imageUri, synonyms=[item.name])
  return Response(item.name).carousel(cards).suggestions(WELCOME_SUGGESTIONS).build()  
  
def person(session, request):
  person = request.get('queryResult').get('parameters').get('person')
  results = google_kgraph_lookup(person, ["Person"])
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  if results and len(results)>0:
    item=results[0]
    card=Card(item.name, item.long_description, 
              subtitle=item.short_description, 
              imageUri=item.imageUri)
    return Response(item.name).card(card).suggestions(["Not this person"].append(WELCOME_SUGGESTIONS)).build()
  
  response_text=random.choice(CONCEPT_DEFINITION_UNKNOWN).format(concept)
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()

def person_fallback(session, request):
  person = request.get('queryResult').get('parameters').get('person')
  results = google_kgraph_lookup(person, ["Person"])  
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  cards=[]
  if results and len(results)>0:
    for item in results:
      card=Item(item.name, item.long_description, 
              imageUri=item.imageUri, synonyms=[item.name])
  return Response(item.name).carousel(cards).suggestions(WELCOME_SUGGESTIONS).build()  
  
def fallback(session, request):
  response_text = random.choice(GENERAL_FALLBACKS)
  query = request.get('queryResult').get('queryText')

  contexts = request.get('queryResult').get('outputContexts')
  option_value=None
  if query=='actions_intent_OPTION':
    for context in contexts:
      if context.get('name') is not None and context.get('name').endswith('actions_intent_option'):
        option_value = context.get('parameters').get('OPTION')
  else:
    option_value=query
  
  logging.debug('option_value=%s', option_value)

  if option_value.startswith('course'):
    return course_id(session, option_value[len('course')+1:])
  elif option_value.startswith('lesson'):
    return lesson_id(session, option_value[len('lesson')+1:])
  elif option_value.startswith('homework'):
    return homework_id(session, option_value[len('homework')+1:])
  elif option_value.startswith('activity'):
    return activity_id(session, option_value[len('activity')+1:])
  
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()


def course_id(session, courseId):
  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseId.strip())
  logging.debug('courseId: %s, %d lessons in course', courseId, len(lessons))
  if lessons is not None:
    for lesson in lessons:
      card=Item('lesson '+lesson.id, lesson.name, lesson.description, imageUri=lesson.imageUri)
      select_cards.append(card)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()


def lesson_id(session, lessonId):
  logging.debug('lessonId: %s', lessonId)
  response_text = random.choice(LESSON_ACTIVITY_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY, type=OUT_CONTEXT_LESSON_ACTIVITY)
  select_cards = []
  lesson = sample_lessons.lesson_id_dict.get(lessonId.strip())
  if lesson is not None:
    for m in lesson.materials:
      logging.debug('activity type=%s, %s',type(m), m)
      if isinstance(m, Video):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Text):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Link):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Audio):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Quiz):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
    return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()
  error_text = 'Error, lesson not found'
  return Response(error_text).text(error_text).build()


def homework_id(session, homeworkId):
  assignment = sample_homeworks.homework_id_dict.get(homeworkId.strip())
  return do_homework(session, assignment).build()

def activity_id(session, activityId):
  activity=sample_lessons.activity_id_dict.get(activityId.strip())
  if activity is None: #homework activity
    activity=sample_homeworks.activity_id_dict.get(activityId.strip())
    logging.debug('found activity %s', activity.title)
  else:
    logging.debug('found activity %s', activity.title)
  
  return do_activity(session, activity).build()
