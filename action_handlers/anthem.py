#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import json
import random
import logging
from datetime import datetime

from action_handlers.session import *
from action_handlers.utils import *
from action_handlers.activity import do_homework, do_activity

from response_generators.messages import *
from response_generators.response import Response, OutputContext, Text, Item

from models.common import *
from models.activities import *
from models.mock import sample_announcements, sample_courses, sample_lessons, sample_homeworks


def read(session, request):
  anthem = random.choice(ANTHEM)
  userContext=UserContext()
  
  return Response(anthem[0].format(userContext.name))\
          .speech(anthem[1].format(userContext.name), 
                  anthem[0].format(userContext.name))\
          .userStorage(userContext.toJson())\
          .suggestions(WELCOME_SUGGESTIONS).build()
