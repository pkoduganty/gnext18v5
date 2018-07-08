#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 00:14:03 2018

@author: praveen
"""

from google.appengine.ext import ndb


class Course(ndb.Model):
  id=ndb.Key(auto_now_add=True)
  name=ndb.StringProperty(required=True)
  section=ndb.StringProperty()
  grade=ndb.IntegerProperty(required=True, default=8)
  subject=ndb.StringProperty(required=True, choices=["SCIENCE", "SOCIAL_STUDIES"])
  descriptionHeading=ndb.TextProperty()
  description=ndb.TextProperty()
  ownerId=ndb.StringProperty()
  creationTime=ndb.DateTimeProperty(auto_now_add=True)
  updateTime=ndb.DateTimeProperty(auto_now_add=True)
  imageUri=ndb.StringProperty()
  calendarId=ndb.StringProperty()
    
class Announcement(ndb.Model):
  