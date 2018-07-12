#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 01:30:31 2018

@author: praveen
"""
import json
from marshmallow import Schema, fields, pprint
from datetime import datetime

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

class UserContextSchema(Schema):
  enable_push_notifications=fields.Boolean()
  last_logon=fields.DateTime()
  last_activity=fields.String()
  last_activity_type=fields.String()
  activity_history=fields.List(fields.String())
  activities_started=fields.Integer()
  activities_finished=fields.Integer()
  badges=fields.List(fields.String())
  
class UserContext(object):
  def __init__(self, enable_push_notifications=False, last_logon=datetime.now(), 
               last_activity=None, last_activity_type=None, history=[], started=0, finished=0, score=0,
               badges=[]):
    self.enable_push_notifications=enable_push_notifications
    self.last_logon=last_logon
    self.last_activity=last_activity
    self.last_activity_type=last_activity_type
    self.activity_history=history
    self.activities_started=started
    self.activities_finished=finished
    self.learning_score=score
    self.badges=badges

  def toJson(self):
    schema = UserContextSchema()
    return schema.dumps(self)
    
def getUserContext(request):
  if request.get('user') and request.get('user').get('userStorage'):
    userContext=request.get('user').get('userStorage')
    schema = UserContextSchema()
    userContext=schema.loads(userContext)
    return userContext
  return None

    
if __name__ == '__main__':
  ctx = UserContext()
  schema = UserContextSchema()
  json_result = schema.dumps(ctx)
  pprint(json_result)  
  result = schema.loads(json_result.data)
  pprint(result)  
