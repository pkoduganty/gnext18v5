#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *
from action_handlers.activity import do_activity

from response_generators.response import *
from response_generators.messages import *

from models.common import *
from models.mock import sample_announcements, sample_homeworks, sample_lessons, sample_courses

def start(session, request):
  error_text = 'Error, quiz not found'
  
  contexts=[]
  quizId=None
  for context in request.get('queryResult').get('outputContexts'):
    if context.get('name').endswith(OUT_CONTEXT_DO_HOMEWORK):
      homeworkId=context.get('parameters').get('id')
      contexts.append(OutputContext(session,OUT_CONTEXT_DO_HOMEWORK, lifespan=2, type=OUT_CONTEXT_DO_HOMEWORK, id=homeworkId))
    elif context.get('name').endswith(OUT_CONTEXT_LESSON_ACTIVITY_DO):
      quizId=context.get('parameters').get('id')
      contexts.append(OutputContext(session,OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, id=quizId))
        
    logging.info('start quiz - %s', quizId)
    if quizId is None:
      return Response(error_text).text(error_text)
    
    if homeworkId is None:
      activity = sample_homeworks.activity_id_dict[quizId] #from homework
    else:
      activity = sample_lessons.activity_id_dict[quizId] #from lesson
      
    description='{0} Questions in this quiz with 10 points for each. Ready to begin?'.format(len(activity.questions))
    card = Card(activity.title, description=description)
    response_text = activity.title
    context = OutputContext(session, OUT_CONTEXT_QUIZ_DO, type=OUT_CONTEXT_QUIZ_DO, lifespan=2, id=quizId)
    #return Response(response_text).text(description).setOutputContexts(contexts).outputContext(context).build()
    return Response(response_text).text(description).outputContext(context).build()
  