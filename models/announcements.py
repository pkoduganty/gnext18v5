#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:40:44 2018

@author: praveen
"""
from models.common import *

class Announcement(Object):
  def __init__(self, courseId=None, id=None, text=None, state='PUBLISHED',
               alternateLink=None, creationTime=None, updateTime=None, 
               scheduledTime=None, assigneeMode='ALL_STUDENTS', creatorUserId=None):
    self.courseId=courseId
    self.id=id
    self.text=text
    self.state=state
    self.alternateLink=alternateLink
    self.creationTime=creationTime
    self.updateTime=updateTime
    self.scheduledTime=scheduledTime
    self.assigneeMode=assigneeMode
    self.creatorUserId=creatorUserId
