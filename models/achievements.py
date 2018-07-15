#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 03:43:56 2018

@author: praveen
"""
from models.common import *

class ActivityType(object):
  VIDEO='video'
  AUDIO='audio'
  TEXT='text'
  QUIZ='quiz'
  LINK='link'

class Achievement(Object):
  def __init__(self, type, level, badge):
    self.type=type
    self.level=level
    self.badge=badge

class Badge(Object):
  def __init__(self, title, img):
    self.title=title
    self.img=img
    