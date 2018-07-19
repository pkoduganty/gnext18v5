#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging
import re

from action_handlers.session import *
from action_handlers.activity import do_activity

from response_generators.response import *
from response_generators.messages import *

from models.common import *
from models.activities import *
from models.mock import sample_announcements, sample_homeworks, sample_lessons, sample_courses

def slot_filler(session, request):
  response_text = random.choice(COURSE_SELECT)
  subjects = [s.lower().replace('_',' ') for s in sample_courses.courses_subject_dict.keys()]
  contexts = []
  for context in request.get('queryResult').get('outputContexts'):
    contexts.append(context)
  return Response(response_text).text(response_text).\
        setOutputContexts(contexts).suggestions(subjects).build()

def list_all(session, request):
  error_text = 'Error, course not found'
  subject = request.get('queryResult').get('parameters').get('subject')
  grade = request.get('queryResult').get('parameters').get('grade') #TODO use students current grade
  grade = grade if grade is not None else 8
  
  logging.info('subject=%s, grade=%d', subject, grade)
  if subject is None:
    return Response(error_text).text(error_text).build()
  else:
    courses_by_subject=sample_courses.courses_subject_dict.get(subject)
    if courses_by_subject is None or len(courses_by_subject)==0:
      return Response(error_text).text(error_text).build()
    else:
      logging.debug('Courses with subject - '+str(courses_by_subject))
      courseIds=[c.id for c in courses_by_subject if c.grade==grade]
      logging.debug('Courses with subject and grade - '+str(courseIds))
      if len(courseIds)==0:
        return Response(error_text).text(error_text).build()

  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseIds[0])
  if lessons is not None:
    if len(lessons)==1:
      response_text = random.choice(LESSON_SELECT)
      context = OutputContext(session, OUT_CONTEXT_LESSON, type=OUT_CONTEXT_LESSON)
      return Response(response_text).text(response_text).card(Card(lessons[0].name, lessons[0].description, imageUri=lessons[0].imageUri)).outputContext(context).build()
    elif len(lessons)>1:
      for lesson in lessons:
        card=Item('lesson '+lesson.id, lesson.name, lesson.description, imageUri=lesson.imageUri)
        select_cards.append(card)
      response_text = random.choice(LESSON_SELECT)
      context = OutputContext(session, OUT_CONTEXT_LESSON, type=OUT_CONTEXT_LESSON)
      return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()
  
  response_text='No lessons'
  return Response(response_text).text(response_text).build()
  

def select_id(session, request):
  error_text = 'Error, lesson not found'  
  lessonId=None
  for context in request.get('queryResult').get('outputContexts'):
    if context.get('name').endswith('actions_intent_option') and context.get('parameters').get('OPTION') is not None:
      option_value=context.get('parameters').get('OPTION')
      lessonId=option_value[option_value.startswith('lesson') and len('lesson')+1:]
          
  logging.info('lesson=%s',lessonId)
  if lessonId is None:
    if request.get('queryResult').get('parameters').get('id') is not None:
      lessonId=request.get('queryResult').get('parameters').get('id')
    else:
      return Response(error_text).text(error_text).build()

  logging.info('lesson=%s',lessonId)

  ## duplicated in input.py
  response_text = random.choice(LESSON_ACTIVITY_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY, type=OUT_CONTEXT_LESSON_ACTIVITY)
  select_cards = []
  lesson = sample_lessons.lesson_id_dict.get(lessonId)
  if lesson is not None:
    if len(lesson.materials)==1:
      return do_activity(session, lesson.materials[0]).build()
    else:
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

def select(session, request):
  lessonType = request.get('queryResult').get('parameters').get('LessonType')
  lessonName = request.get('queryResult').get('parameters').get('LessonName')
  context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY, type=OUT_CONTEXT_LESSON_ACTIVITY)
  activity = search(lessonName,lessonType)
  if activity :
    return do_activity(session,activity).build()
  else:
    return Response("Sorry no lesson found.").text("You asked {0} from lesson {1} but we didn't find anything realted".format(lessonType,lessonName)).outputContext(context).build()


def findActivity(lessonName,lessonType):
    lesson = sample_lessons.lesson_name_dict[lessonName.upper()]
    for activity in lesson.materials:
        if isinstance(activity, sample_lessons.activity_typeDict[lessonType.lower()]):
            return activity
    return None

def search(lessonName,lessonType):
  words = lessonName.split(' ')
  lessons = sample_lessons.lessons
  matches = []

  if len(words) > 0:
    for word in words:
        regex=re.compile(".*({0}).*".format(word.lower()))
        midList = []
        midList = [match.group(0) for lesson in lessons for match in [regex.search(lesson.name.lower())] if match and not any(lsn == lesson.name.lower() for lsn in matches) ]
        for ls in midList:            
            matches.append(ls)
  mostMatches = dict()
  for match in matches:
    mostMatches[match] = [word.lower() in match.lower() for word in words].count(True)
  mostMatched = max(mostMatches, key=mostMatches.get) 
  
  return findActivity(mostMatched,lessonType)
  



