#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 00:14:03 2018

@author: praveen
"""

from google.appengine.ext import ndb


class Course(ndb.Model):
  name=ndb.StringProperty()
  section=ndb.StringProperty()
  grade=grade
  subject=ndb.StringProperty()
  descriptionHeading=ndb.TextProperty()
  description=ndb.TextProperty()
  creationTime=ndb.DateTimeProperty(auto_now_add=True)
  updateTime=ndb.DateTimeProperty(auto_now_add=True)
  imageUri=ndb.StringProperty()
    
class Announcement(ndb.Model):
  