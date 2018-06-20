#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random

from action_handlers.session import *

from response_generators.response import Response
from response_generators.messages import WELCOME_SUGGESTIONS, WELCOME_BASIC

# handle first logon for the day
# handle subsequent logins for the day
# start from where left off since last login if any
def welcome(session, request):
  response_text = random.choice(WELCOME_BASIC).format('Susan')
  return Response(response_text).text(response_text).suggestions(WELCOME_SUGGESTIONS).build()
