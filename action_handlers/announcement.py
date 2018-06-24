#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random

from action_handlers.session import *

from response_generators.response import Response, Item
from response_generators.messages import (UNREAD_ANNOUNCEMENTS, 
    UNREAD_ANNOUNCEMENT, NO_UNREAD_ANNOUNCEMENTS)

from models.mock import sample_announcements, sample_courses

def select(session, request):
  announcements = random.sample(sample_announcements.announcements, 
                                random.randint(0, len(sample_announcements.announcements)-1))
  if len(announcements)==0:
    response_text = random.choice(NO_UNREAD_ANNOUNCEMENTS)
  elif len(announcements)==1:
    response_text = random.choice(UNREAD_ANNOUNCEMENT).format('Susan')
  else:
    response_text = random.choice(UNREAD_ANNOUNCEMENTS).format('Susan', len(announcements))
  
  items = []
  for a in announcements:
    items.append(Item(id=a.id, title=sample_courses.courses_id_dict[a.courseId].name, description=a.text))
  return Response(response_text).select(response_text, items).build()
