#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:40:44 2018

@author: praveen
"""

from models.common import *
from models.activities import *

class Homework(Object):
  def __init__(self, courseId=None, id=None, title=None, description=None, 
               activity=None, state='PUBLISHED', alternateLink=None,
               creationTime=None, updateTime=None, dueDate=None, dueTime=None,
               scheduledTime=None, maxPoints=0, assigneeMode='ALL_STUDENTS', 
               activityType=None, creatorUserId=None):
    self.courseId=courseId
    self.id=id
    self.title=title
    self.description=description
    self.activity=activity #either of video, text, audio, quiz, link
    self.state=state
    self.alternateLink=alternateLink
    self.creationTime=creationTime
    self.updateTime=updateTime
    self.dueDate=dueDate
    self.dueTime=dueTime
    self.scheduledTime=scheduledTime,
    self.maxPoints=maxPoints,
    self.assigneeMode=assigneeMode
    self.activityType=activityType
    self.creatorUserId=creatorUserId
