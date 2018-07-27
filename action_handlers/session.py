#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 01:30:31 2018

@author: praveen
"""
import json
import logging
from marshmallow import Schema, fields, post_load, pprint
from datetime import datetime
import pickle

EVENT_NEXT_QUESTION='action_next_question'

OUT_CONTEXT_COURSE='course'
OUT_CONTEXT_ANNOUNCEMENT='announcement'
OUT_CONTEXT_HOMEWORK='homework'
OUT_CONTEXT_DO_HOMEWORK='homework_do'
OUT_CONTEXT_LESSON='lesson'
OUT_CONTEXT_LESSON_ACTIVITY='lesson_activity'
OUT_CONTEXT_LESSON_ACTIVITY_DO='lesson_activity_do'
OUT_CONTEXT_QUIZ='quiz'
OUT_CONTEXT_QUIZ_DO='quiz_do'
OUT_CONTEXT_QUIZ_QUESTION='quiz_question'
defaultDict = dict()
defaultDict['GOLD'] = 0
defaultDict['SILVER'] = 0
defaultDict['BRONZE'] = 0


class BadgesSchema(Schema):    
  quiz = fields.Dict(defaultDict.copy(),allow_none=True)
  videos = fields.Dict(defaultDict.copy(),allow_none=True)
  course = fields.Dict(defaultDict.copy(),allow_none=True)
  shields = fields.Dict(defaultDict.copy(),allow_none=True)

class Badges(object):
  def __init__(self, quiz = defaultDict.copy(), videos= defaultDict.copy(), course = defaultDict.copy(), shields = defaultDict.copy()):   
    self.quiz = quiz
    self.videos = videos
    self.course = course
    self.shields = shields
    
  def toJSON(self):
    schema = BadgesSchema()
    return schema.dumps(self).data 


class UserContextSchema(Schema):
  name=fields.String()
  last_logon=fields.DateTime()
  last_activity=fields.String(allow_none=True)
  last_activity_type=fields.String(allow_none=True)
  activity_history=fields.List(fields.String())
  activities_started=fields.Integer()
  activities_finished=fields.Integer()
  learning_score=fields.Integer()
  quiz_badges = fields.Dict(defaultDict.copy(),allow_none=None)
  shields_badge = fields.String(allow_none=True)
  courses_badges = fields.Dict(defaultDict.copy(),allow_none=None)
  
  @post_load
  def processUser(self, data):
    # logging.debug(data)
    if isinstance(data, str):
      data=json.loads(data).data
   
    return UserContext(**data)
  
class UserContext(object):
  def __init__(self, name='Susan', last_logon=datetime.now(), 
               last_activity='', last_activity_type='', 
               activity_history=[], activities_started=0, activities_finished=0, learning_score=0,
               quiz_badges= defaultDict.copy(),shields_badge= None,courses_badges = defaultDict.copy()):
    self.name = name
    self.last_logon=last_logon
    self.last_activity=last_activity
    self.last_activity_type=last_activity_type
    self.activity_history=activity_history
    self.activities_started=activities_started
    self.activities_finished=activities_finished
    self.learning_score=learning_score
    self.quiz_badges = quiz_badges
    self.shields_badge = shields_badge
    self.courses_badges = courses_badges
  
  def toJson(self):
    schema = UserContextSchema()
    print(self)
    return schema.dumps(self).data  

def getUserContext(request):
  try:
    if request.get('user') and request.get('user').get('userStorage'):
      userContext=request.get('user').get('userStorage')
      schema = UserContextSchema()
      userContext=schema.loads(userContext).data
      return userContext
    elif (request.get('originalDetectIntentRequest') and 
          request.get('originalDetectIntentRequest').get('payload') and
          request.get('originalDetectIntentRequest').get('payload').get('user') and
          request.get('originalDetectIntentRequest').get('payload').get('user').get('userStorage')):
      userStore=request.get('originalDetectIntentRequest').get('payload').get('user').get('userStorage')
      schema = UserContextSchema()
      userContext = schema.loads(json.loads(userStore)).data
      return userContext
  except Exception as e:
    logging.error('Error while getting user context', e)
  return None

    
if __name__ == '__main__':
  ctx = UserContext()
  schema = UserContextSchema()
  json_result = schema.dumps(ctx)
  pprint(json_result)  
  result = schema.loads(json_result.data)
  pprint(result)  
