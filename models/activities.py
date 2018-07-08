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

class Link(Object):
  def __init__(self, id, title, url):
    self.id=id
    self.url=url
    self.title=title

class Video(Object):
  def __init__(self, id, title, url, imageUri=None, imageText=None):
    self.id=id
    self.title=title
    self.url=url
    if imageUri is not None:
      self.imageUri=imageUri
      self.imageText=imageText if imageText is not None else title

class Audio(Object):
  def __init__(self, id, title, url, imageUri=None, imageText=None):
    self.id=id
    self.title=title
    self.url=url
    if imageUri is not None:
      self.imageUri=imageUri
      self.imageText=imageText if imageText is not None else title

class Text(Object):
  def __init__(self, id, title, text, ssmlText=None, imageUri=None, imageText=None):
    self.id=id
    self.title=title
    self.text=text
    if ssmlText is not None:
      self.ssmlText=ssmlText
    if imageUri is not None:
      self.imageUri=imageUri
      self.imageText=imageText if imageText is not None else title

class Quiz(Object):
  def __init__(self, id, title, questions, imageUri=None, imageText=None):
    self.id=id
    self.title=title
    self.questions=questions
    if imageUri is not None:
      self.imageUri=imageUri
      self.imageText=imageText if imageText is not None else title

class Question(Object):
  def __init__(self, id, question, answers, choices=[]):
    self.id=id
    # if choices is empty should be a short answer question else mutliple choice
    self.question=question
    self.choices=choices
    self.answers=answers