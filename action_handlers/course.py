#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *

from response_generators.response import Response, OutputContext, Text, Item
from response_generators.messages import *

from models.mock import sample_lessons, sample_courses

def list_all(session, request):
  response_text = random.choice(COURSE_SELECT)
  select_cards = []
  grade=8 #get user grade
  for course in sample_courses.courses:
    if course.grade==grade:
      card=Item(id='course '+course.id, title=course.name, description=course.description, 
              imageUri=course.imageUri, imageText=course.name)
      select_cards.append(card)
  context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()


def select_id(session, request):
  error_text = 'Error, course not found'  
  courseId=None
  for context in request.get('queryResult').get('outputContexts'):
    if context.get('name').endswith('actions_intent_option'):
      courseId=context.get('parameters').get('OPTION')
          
  if courseId is None:
    if request.get('queryResult').get('parameters').get('id') is not None:
      courseId=request.get('queryResult').get('parameters').get('id')
    else:
      return Response(error_text).text(error_text).build()

  ## duplicated in input.py
  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseId)
  logging.debug('courseId: %s, %d lessons in course', courseId, len(lessons))
  if lessons is not None:
    for lesson in lessons:
      card=Item('lesson '+lesson.id, lesson.name, lesson.description)
      select_cards.append(card)

  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON, type=OUT_CONTEXT_LESSON)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()

