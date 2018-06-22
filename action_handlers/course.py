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

from models.mock import sample_announcements, sample_lessons, sample_courses

def select(session, request):
  response_text = random.choice(COURSE_SELECT)
  #context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  select_cards = []
  for course in sample_courses.courses:
    card=Item(id=course.id, title=course.name, description=course.description, imageUri=course.alternateLink, imageText=course.name)
    select_cards.append(card)
  #return Response(response_text).outputContext(context).select(response_text, select_cards).build()
  return Response(response_text).text(response_text).select(response_text, select_cards).build()
  
def id(session, request):
  error_text = 'Error, course not found'
  if request.get('queryResult').get('parameters') is None or request.get('queryResult').get('parameters').get('courseId') is None:
    return Response(error_text).text(error_text).build()
      
  courseId = request.get('queryResult').get('parameters').get('courseId')
  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseId)
  if lessons is not None:
    for lesson in lessons:
      card=Item(lesson.id, lesson.name, lesson.file)
      select_cards.append(card)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()

def materials(session, request):
  logging.info('selected course from list of select cards')
  response_text = 'select a subject, from your enrolled courses'
  return Response(response_text).text(response_text).followupIntent('course.select').build()
  '''
  contexts = request.get('queryResult').get('outputContexts')
  for context in contexts:
    if context.get('parameters') is not None and context.get('parameters').get('type')==OUT_CONTEXT_COURSE:
      
      lessons=[]
      for lesson in sample_lessons:
        if lesson.courseId==course.id:
          lessons.append(lesson.name)
      response_text='Show course materials'
      assignments=context.get('parameters').get('id')
      outContext = OutputContext(session, OUT_CONTEXT_ASSIGNMENT, id=assignments, type=OUT_CONTEXT_ASSIGNMENT)
      return Response(response_text).text(response_text).outputContexts(contexts).outputContext(outContext).followupIntent('assignment.do').build()
  '''
