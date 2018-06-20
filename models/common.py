#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 03:43:56 2018

@author: praveen
"""
import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Media(Object):
  def __init__(self, id, title, alternativeLink=None, alternateLink=None):
    self.id=id
    self.title=title
    self.link=None
    if alternativeLink is None:
      self.link=alternativeLink
    else:
      self.link=alternateLink

class Link(Object):
  def __init__(self, url, title):
    self.url=url
    self.title=title

class CourseMaterialSet(Object):
  def __init__(self, title, materials):
    self.title=title
    if materials is not None:
      self.materials=CourseMaterial(**materials)
    
class CourseMaterial(Object):
  def __init__(self, driveFile, youTubeVideo, link):
    if driveFile is not None:
      self.driveFile=Media(**driveFile)
    if youTubeVideo is not None:
      self.youTubeVideo=Media(**youTubeVideo)
    if link is not None:
      self.link=Link(**link)
