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
  if request.get('queryResult').get('parameters').get('reset'):
    userContext=UserContext()
  else:
    userContext=getUserContext(request)
  
  if userContext:
    welcome = random.choice(WELCOME_SECOND_LOGON)
    userContext.last_logon=datetime.now()
  else:
    welcome = random.choice(WELCOME_BASIC)
    userContext=UserContext() # new if one already doesn't exist
    
  instructions = random.choice(WELCOME_TEXT)
  return Response(welcome[0].format(userContext.name))\
          .speech(welcome[1].format(userContext.name), 
                  welcome[0].format(userContext.name))\
          .speech(instructions[1].format(userContext.name), 
                  instructions[0].format(userContext.name))\
          .userStorage(userContext.toJson())\
          .suggestions(WELCOME_SUGGESTIONS).build()


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
    return course_id(session, option_value[len('course')+1:])
  elif option_value.startswith('lesson'):
    return lesson_id(session, option_value[len('lesson')+1:])
  elif option_value.startswith('homework'):
    return homework_id(session, option_value[len('homework')+1:])
  elif option_value.startswith('activity'):
    return activity_id(session, option_value[len('activity')+1:])
  
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()
