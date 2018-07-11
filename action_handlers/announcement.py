#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random

from action_handlers.session import *

from response_generators.response import Response, Item
from response_generators.messages import *

from models.mock import sample_announcements, sample_courses


def get_random_announcements():
  announcements = random.sample(sample_announcements.announcements, 
                                random.randint(2, len(sample_announcements.announcements)-1))
  
  if len(announcements)==0:
    response_text = random.choice(NO_UNREAD_ANNOUNCEMENTS)
  elif len(announcements)==1:
    response_text = random.choice(UNREAD_ANNOUNCEMENT).format('Susan')
  else:
    response_text = random.choice(UNREAD_ANNOUNCEMENTS).format('Susan', len(announcements))
  
  items = []
  for a in announcements:
    items.append(Item(id=a.id, title=sample_courses.courses_id_dict[a.courseId].name, description=a.text))
    
  return Response(response_text).select(response_text, items).suggestions(WELCOME_SUGGESTIONS)

def list_all(session, request):
  ask_setup_push_notifications = random.choice([True, False])
  permissions=None
  if request.get('payload') and request.get('payload').get('user') and request.get('payload').get('user').get('permissions'):    
    permissions = request.get('payload').get('user').get('permissions')
  
  if permissions and permissions.index("UPDATE"):
      return get_random_announcements().build()
  else:
    userContext=getUserContext(request)
    if userContext and userContext.enable_push_notifications:
      return get_random_announcements().build()
    
  if ask_setup_push_notifications:
    response_text="Get immediate alerts for school updates?"
    return Response(response_text).permissions(response_text, ["UPDATE"],"announcement.list_all").build()
  
  return get_random_announcements().build()
    

def setup_push_notification_yes(session, request):
  userContext=getUserContext(request)
  if not userContext:
    userContext=UserContext()
    
  userContext.enable_push_notifications=True
  return get_random_announcements().userStorage(userContext.toJson()).build()
