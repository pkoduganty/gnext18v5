#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:40:44 2018

@author: praveen
"""

from models.common import *

class Course(Object):
  def __init__(self, id=None, name=None, section=None, grade=5, subject=None, description=None, descriptionHeading=None, 
               ownerId=None, creationTime=None, updateTime=None, 
               courseState='ACTIVE', imageUri=None, calendarId=None):
    self.id=id
    self.name=name
    self.section=section
    self.grade=grade
    self.subject=subject
    self.descriptionHeading=descriptionHeading
    self.description=description
    self.ownerId=ownerId
    self.creationTime=creationTime
    self.updateTime=updateTime
    self.courseState=courseState
    self.imageUri=imageUri
    self.calendarId=calendarId


class Lesson(Object):
  def __init__(self, id=None, courseId=None, name=None, section=None, description=None, 
               materials=[], imageUri=None, activeFromDate=None, activeTillDate=None):
    self.id=id
    self.name=name
    self.section=section
    self.courseId=courseId
    self.description=description
    self.materials=materials
    self.imageUri=imageUri
    self.activeFromDate=activeFromDate
    self.activeTillDate=activeTillDate
    