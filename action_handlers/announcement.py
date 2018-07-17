#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *

from response_generators.response import Response, Item
from response_generators.messages import *

from models.mock import sample_announcements, sample_courses

def getAnnouncementItem(announcement):
  return Item(id=announcement.id, title=sample_courses.courses_id_dict[announcement.courseId].name, description=announcement.text)


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
    items.append(getAnnouncementItem(a))
    
  return Response(response_text).select(response_text, items)

def list_all(session, request):
  permissions=None
  if request.get('payload') and request.get('payload').get('user') and request.get('payload').get('user').get('permissions'):    
    permissions = request.get('payload').get('user').get('permissions')
  
  if permissions and permissions.index("UPDATE"):
      return get_random_announcements().build()
  else:
    response_text="Get immediate alerts for school updates?"
    return Response(response_text).permissions(response_text, ["UPDATE"],"announcement.get_notification").build()
  
def setup_push_notification_yes(session, request):
  return get_random_announcements().build()

def get_notification(session,request):
  logging.info("Request : " + json.dumps(request))
  id = request.get('queryResult').get('parameters').get('id')
  response_text = 'Announcement'
  items = []
  if id is not None:
    for announcement in sample_announcements.announcements:
      if announcement.id == id:   
        items.append(getAnnouncementItem(announcement))
        return Response(response_text).select(response_text, items)
  else:
    return get_random_announcements().build()