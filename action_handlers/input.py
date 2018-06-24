#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random

from action_handlers.session import *

from response_generators.messages import *
from response_generators.response import Response, OutputContext, Text, Item

from models.mock import sample_announcements, sample_courses, sample_lessons, sample_homeworks

# handle first logon for the day
# handle subsequent logins for the day
# start from where left off since last login if any
def welcome(session, request):
  response_text = random.choice(WELCOME_BASIC).format('Susan')
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()

def fallback(session, request):
  response_text = random.choice(GENERAL_FALLBACKS)
  
  query = request.get('queryResult').get('queryText')
  contexts = request.get('queryResult').get('outputContexts')
  
  select_list_type = None
  if query=='actions_intent_OPTION':
    for context in contexts:
      if context.get('parameters') is not None:
        select_list_type = context.get('parameters').get('type')
        option_value = context.get('parameters').get('OPTION')
        
    if select_list_type=='course':
      return course_id(session, option_value)
    elif select_list_type=='lesson':
      return lesson_id(session, option_value)
    elif select_list_type=='homework':
      return homework_id(session, option_value)
    
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()

def course_id(session, courseId):
  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseId)
  if lessons is not None:
    for lesson in lessons:
      card=Item(lesson.id, lesson.name, lesson.description)
      select_cards.append(card)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()

def lesson_id(session, lessonId):
  response_text = random.choice(LESSON_MATERIAL_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON_MATERIAL, type=OUT_CONTEXT_LESSON_MATERIAL)
  select_cards = []
  lesson = sample_lessons.lesson_id_dict.get(lessonId)
  if lesson is not None:
    for m in lesson.materials:
      card=Item(id=m.url, title=m.title, imageUri=m.imageUri)
      select_cards.append(card)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()

def homework_id(session, homeworkId):
  assignment = sample_homeworks.homework_id_dict.get(homeworkId)
  response_text = random.choice(PENDING_HOMEWORK).format('Susan', assignment.title)
  return Response(response_text).text(response_text).build()
