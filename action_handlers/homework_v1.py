#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *

from response_generators.response_v1 import Response, OutputContext, Item
from response_generators.messages import PENDING_ASSIGNMENT, PENDING_ASSIGNMENTS, WELCOME_BASIC, WELCOME_SUGGESTIONS

from models.mock import sample_announcements, sample_workitems, sample_lessons, sample_courses

def read(session, request):
  has_assignments = random.choice([True, False])
  multiple = random.choice([True, False])
  if has_assignments:
    if multiple:
      response_text = random.choice(PENDING_ASSIGNMENTS).format('Susan', len(sample_workitems.work_items))
      assignments = [wi.id for wi in sample_workitems.work_items]
      logging.info('homework.read, found multiple assignments :', assignments)
      context = OutputContext(session, OUT_CONTEXT_ASSIGNMENT, lifespan=2, id=assignments, type=OUT_CONTEXT_ASSIGNMENT)
    else:
      assignment = random.choice(sample_workitems.work_items)
      logging.info('homework.read, found 1 assignment :', assignment.title)
      context = OutputContext(session, OUT_CONTEXT_ASSIGNMENT, id=[assignment.id], type=OUT_CONTEXT_ASSIGNMENT) #read, working, done
      response_text = random.choice(PENDING_ASSIGNMENT).format('Susan', assignment.title)
    return Response(response_text).text(response_text).outputContext(context).suggestion('Yes').suggestion('No').build()

def read_followup_yes(session, request):
  contexts = request.contexts
  outContexts = []
  response_text = 'didn\'t quite understand'
  for context in contexts:
    if context.parameters is not None and context.parameters.get('type')==OUT_CONTEXT_ASSIGNMENT:
      response_text = 'ok, let us begin this'
      assignments = context.parameters.get('id')
    else:
      outContexts.append(context)
  
  items=[]
  for assignment in assignments:
    items.append(Item(assignment.id, assignment.title, assignment.description))
  return Response(response_text).text(response_text).setOutputContexts(outContexts).carousel(items).build()

def read_followup_no(session, request):
  response_text = random.choice(WELCOME_BASIC).format('Susan')
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()