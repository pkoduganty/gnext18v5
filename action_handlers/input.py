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
from action_handlers.activity import do_homework, do_activity

from response_generators.messages import *
from response_generators.response import Response, OutputContext, Text, Item

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


def google_kgraph_lookup(concept):
  service = build("kgsearch", "v1", developerKey='AIzaSyBPobZc7OwY6D_XcOThmqst2Lpl9c3Ggas') #TODO hardcoded
  result = service.entities().search(prefix=True, query=concept, languages='en', limit=1).execute()
  logging.info('Knowledge Graph Response = %s', json.dumps(result))
  
  if result and result.get('itemListElement') and len(result.get('itemListElement'))>0:
    item=result.get('itemListElement')[0]
    logging.info('ItemListElement=%s', json.dumps(item))
    if item and item.get('result') and item.get('result').get('detailedDescription') and item.get('result').get('detailedDescription').get('articleBody'):
      return item.get('result').get('detailedDescription').get('articleBody').encode('ascii', 'ignore')
  return None
  
def google_csearch(query):
  service = build("customsearch", "v1",
            developerKey="AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0")

  res = service.cse().list(
      q=query,
      cx='017576662512468239146:omuauf_lfve',
    ).execute()
  return res

def dbpedia_concept_lookup(concept):
  query = '''PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT DISTINCT ?desc  WHERE {{
              ?subj rdfs:comment ?desc.
              FILTER( LANG(?desc)="en" )
              ?subj rdfs:label ?label.
              FILTER( lcase(str(?label)) = lcase(str("{0}")) )
            }} LIMIT 1
    '''.format(concept)
    
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sparql.setQuery(query)
  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  logging.debug('SPARQL Response = %s', json.dumps(results))
  
  if results and results.get('results') and results.get('results').get('bindings') and len(results.get('results').get('bindings'))>0:
    binding=results.get('results').get('bindings')[0]
    if binding.get('desc') and binding.get('desc').get('value'):
      return binding.get('desc').get('value').encode('ascii', 'ignore')
  return None

def definition(session, request):
  concept = request.get('queryResult').get('parameters').get('concept')
  desc = google_kgraph_lookup(concept)
  
  if desc:
    return Response(desc).text(desc).suggestions(WELCOME_SUGGESTIONS).build()
  
  response_text=random.choice(CONCEPT_DEFINITION_UNKNOWN).format(concept)
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()
  
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
    return course_id(session, option_value[option_value.startswith('course') and len('course')+1:])
  elif option_value.startswith('lesson'):
    return lesson_id(session, option_value[option_value.startswith('lesson') and len('lesson')+1:])
  elif option_value.startswith('homework'):
    return homework_id(session, option_value[option_value.startswith('homework') and len('homework')+1:])
  elif option_value.startswith('activity'):
    return activity_id(session, option_value[option_value.startswith('activity') and len('activity')+1:])
  
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()


def course_id(session, courseId):
  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseId.strip())
  logging.debug('courseId: %s, %d lessons in course', courseId, len(lessons))
  if lessons is not None:
    for lesson in lessons:
      card=Item('lesson '+lesson.id, lesson.name, lesson.description)
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
        select_cards.append(Item(id='activity '+m.id, title=m.title))
      elif isinstance(m, Link):
        select_cards.append(Item(id='activity '+m.id, title=m.title))
      elif isinstance(m, Audio):
        select_cards.append(Item(id='activity '+m.id, title=m.title))
      elif isinstance(m, Quiz):
        select_cards.append(Item(id='activity '+m.id, title=m.title))
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
