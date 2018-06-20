#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random

from action_handlers.session import *

from response_generators.response import Response, Text, Media, OutputContext, Item
from response_generators.messages import *

from models.mock import sample_announcements, sample_workitems, sample_courses

def welcome(session, request):
  has_assignments = random.choice([True, False])
  multiple = random.choice([True, False])
  
  if has_assignments:
    if multiple:
      response_text = random.choice(PENDING_ASSIGNMENTS).format('Susan', len(sample_workitems.work_items))
      assignments = [wi.id for wi in sample_workitems.work_items]
      context = OutputContext(session, OUT_CONTEXT_ASSIGNMENT, lifespan=2, id=assignments, type=OUT_CONTEXT_ASSIGNMENT)
    else:
      assignment = random.choice(sample_workitems.work_items)
      context = OutputContext(session, OUT_CONTEXT_ASSIGNMENT, id=[assignment.id], type=OUT_CONTEXT_ASSIGNMENT) #read, working, done
      response_text = random.choice(PENDING_ASSIGNMENT).format('Susan', assignment.title)
    return Response(response_text).text(response_text).outputContext(context).suggestions(['Yes','No']).build()
  else:
    response_text = random.choice(WELCOME_BASIC).format('Susan')
    return Response(response_text).text(response_text).suggestions(['do homework','read messages','study lesson']).build()

def welcome_followup_yes(session, request):
  contexts = request.get('queryResult').get('outputContexts')
  outContexts = []
  response_text = 'didn\'t quite understand'
  for context in contexts:
    if context.get('parameters') is not None and context.get('parameters').get('type')==OUT_CONTEXT_ASSIGNMENT:
      response_text = 'ok, let us begin this assignment'
      assignments = context.get('parameters').get('id')
      outContext = OutputContext(session, OUT_CONTEXT_ASSIGNMENT, id=assignments, type=OUT_CONTEXT_ASSIGNMENT)
      outContexts.append(outContext)
    else:
      outContexts.append(context)
  return Response(response_text).text(response_text).setOutputContexts(outContexts).followupIntent('homework.select').build()

def welcome_followup_no(session, request):
  response_text = random.choice(WELCOME_BASIC).format('Susan')
  return Response(response_text).text(response_text).suggestions(['do homework','read messages','study lesson']).build()
