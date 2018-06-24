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
  error_text = 'Error, course not found'
  subject = request.get('queryResult').get('parameters').get('subject')
  grade = request.get('queryResult').get('parameters').get('grade') #TODO use students current grade
  grade = grade if grade is not None else 8
  
  if subject is None:
    return Response(error_text).text(error_text).build()
  else:
    courses_by_subject=sample_courses.courses_subject_dict.get(subject)
    if len(courses_by_subject)==0:
      return Response(error_text).text(error_text).build()
    else:
      courseIds=[c for c in courses_by_subject if c.grade==grade]
      if len(courseIds)==0:
        return Response(error_text).text(error_text).build()

  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseIds[0])
  if lessons is not None:
    for lesson in lessons:
      card=Item('lesson - '+lesson.id, lesson.name, lesson.description)
      select_cards.append(card)

  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON, type=OUT_CONTEXT_LESSON)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()
  

def select_id(session, request):
  error_text = 'Error, course not found'
  if request.get('queryResult').get('parameters') is None or request.get('queryResult').get('parameters').get('lessonId') is None:
    return Response(error_text).text(error_text).build()
      
  lessonId = request.get('queryResult').get('parameters').get('lessonId')

  ## duplicated in input.py
  response_text = random.choice(LESSON_MATERIAL_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON_MATERIAL, type=OUT_CONTEXT_LESSON_MATERIAL)
  select_cards = []
  lesson = sample_lessons.lesson_id_dict.get(lessonId)
  if lesson is not None:
    for m in lesson.materials:
      card=Item(id=m.url, title=m.title, imageUri=m.imageUri)
      select_cards.append(card)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()
