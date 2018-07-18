#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import json
import random
import logging
import os
import sys
import importlib
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
  results = google_kgraph_lookup(concept, ["Thing"])
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  if results and len(results)>0:
    item=results[0]
    card=Card(item.name, item.long_description, 
              subtitle=item.short_description, 
              imageUri=item.imageUri)
    suggestions=["Not relevant"]
    suggestions.extend(WELCOME_SUGGESTIONS)
    return Response(item.name).text(item.name).card(card).suggestions(suggestions).build()
  
  response_text=random.choice(CONCEPT_DEFINITION_UNKNOWN).format(concept)
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()


def definition_wrong(session, request):
  concept = request.get('queryResult').get('parameters').get('concept')
  results = google_kgraph_lookup(concept, ["Thing"])  
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  cards=[]
  if results and len(results)>0:
    for item in results:
      card=Item(item.name, item.long_description, 
              imageUri=item.imageUri, synonyms=[item.name])
  return Response(item.name).text(item.name).carousel(cards).suggestions(WELCOME_SUGGESTIONS).build()  
  

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
    suggestions=["Not this person"]
    suggestions.extend(WELCOME_SUGGESTIONS)
    return Response(item.name).text(item.name).card(card).suggestions(suggestions).build()
  
  response_text=random.choice(CONCEPT_DEFINITION_UNKNOWN).format(concept)
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()


def person_wrong(session, request):
  person = request.get('queryResult').get('parameters').get('person')
  results = google_kgraph_lookup(person, ["Person"])  
  logging.debug('knowledge graph result: %s', json.dumps(results, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  cards=[]
  if results and len(results)>0:
    for item in results:
      card=Item(item.name, item.long_description, 
              imageUri=item.imageUri, synonyms=[item.name])
  return Response(item.name).text(item.name).carousel(cards).suggestions(WELCOME_SUGGESTIONS).build()  
  
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

def get_notification(session,request):
  argData = ''
  argData = getArgumentFromRequest(request.get('originalDetectIntentRequest'),'data')
  
  if argData is None:
    argData = request.get('queryResult').get('parameters').get('data')

  (notificationType,id) = argData.split("_",1)
  logging.info("id value: " + id)
  logging.info("notificationType value: " + notificationType)

  if id is not None and notificationType is not None:
    action_handler = importlib.import_module('action_handlers.' + notificationType)
    func = getattr(action_handler, 'get_notification')    
    return func(session, request,id)

def getArgumentFromRequest(request,nameOfArgument):
  if request.get('payload') and request.get('payload').get('inputs'):
    inputs = request.get('payload').get('inputs')
    for inp in inputs:
      if inp['arguments'] :
        for arg in inp['arguments']:
          if arg.get('name') == nameOfArgument:
            return arg.get('textValue')
  return None
