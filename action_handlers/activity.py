#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *

from response_generators.response import *
from response_generators.messages import *

from models.common import *
from models.activities import *
from models.mock import sample_announcements, sample_courses, sample_lessons, sample_homeworks

def do_homework(session, assignment):
  logging.debug('assignment id=%s',assignment.id)

  context = OutputContext(session, OUT_CONTEXT_DO_HOMEWORK, type=OUT_CONTEXT_DO_HOMEWORK, lifespan=2, id=assignment.id)
  response = do_activity(session, assignment.activity)
  return response.outputContext(context)


def do_activity(session, activity):
  logging.debug('activity type=%s, %s',type(activity), activity)
  
  if isinstance(activity, Video):
    button = Button('Open', activity.url)
    card = Card(activity.title, description='', imageUri=activity.imageUri, buttons=[button])
    response_text = 'Play this video, by clicking on the button'
    context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY_DO, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, id=activity.id)
    return Response(response_text).text(response_text).outputContext(context).card(card)
  
  if isinstance(activity, Text):
    context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY_DO, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, id=activity.id)
    return Response(activity.title).speech(activity.ssml, activity.text).outputContext(context)
  
  if isinstance(activity, Link):
    response_text = 'Click on link below'
    context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY_DO, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, id=activity.id)
    return Response(response_text).text(response_text).outputContext(context).link(activity.title, activity.url)
  
  if isinstance(activity, Audio):
    context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY_DO, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, id=activity.id)
    return Response(activity.title).text(activity.title).audio(activity.title, activity.url).outputContext(context)
  
  if isinstance(activity, Quiz):
    description='{0} Questions in this quiz with 10 points for each. Ready to begin?'.format(len(activity.questions))
    card = Card(activity.title, description=description)
    response_text = activity.title
    context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY_DO, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, id=activity.id)
    return Response(response_text).text(description).outputContext(context).followupEvent('quiz_start', id=activity.id)
  
  response_text='Error, unknown activity type.'
  return Response(response_text).text(response_text)