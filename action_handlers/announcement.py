#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging
import logging
import requests

from action_handlers.session import *

from response_generators.response import Response, Item , Card
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
  permissions=[]
  oriReq = request.get('originalDetectIntentRequest')
  if oriReq.get('payload') and oriReq.get('payload').get('user') and oriReq.get('payload').get('user').get('permissions'):    
    permissions = oriReq.get('payload').get('user').get('permissions')
  try:
    if permissions is not None and len(permissions) > 0 and permissions.index("UPDATE",0,len(permissions)) > -1:
      return get_random_announcements().build()
    else:
      response_text="Get immediate alerts for school updates?"
      return Response(response_text).permissions(response_text, ["UPDATE"],"input.get_notification").build()
  except :
    return get_random_announcements().build()

def setup_push_notification_yes(session, request):
  logging.info('Push notification accepted request: '+str(request))
  return get_random_announcements().build()

def getNotificationIdFromRequest(request):
  if request.get('payload') and request.get('payload').get('inputs'):
    inputs = request.get('payload').get('inputs')
    for inp in inputs:
      if inp['arguments'] :
        for arg in inp['arguments']:
          if arg.get('name') == 'id':
            return arg.get('textValue')
  return None

def get_notification(session,request,id): 
  
  if id:
    for announcement in sample_announcements.announcements:
      if announcement.id == id:   
        return Response(announcement.text).build()

  return get_random_announcements().build()  

def getAnnouncementFromFirebase(id):
  url = 'https://us-central1-gnext18-v5.cloudfunctions.net/getAnnouncementById?id=' + id
  data = requests.get(url).json()
  return data 