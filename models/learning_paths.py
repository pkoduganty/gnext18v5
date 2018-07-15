#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 03:43:56 2018

@author: praveen
"""
from models.common import *
from models.activities import *

import networkx as nx

class Path(Object):
  def __init__(self, id, title, questions, imageUri=None, imageText=None):
    self.id=id
    self.title=title
    self.questions=questions
    if imageUri is not None:
      self.imageUri=imageUri
      self.imageText=imageText if imageText is not None else title
