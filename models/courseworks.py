#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:40:44 2018

@author: praveen
"""
#import json
#from flask import jsonify, abort, make_response
#from flask_restful import Resource

from models.common import Object, Media, CourseMaterial

class Question(Object):
  def __init__(self, choices=[]):
    # if choices is empty should be a short answer question else mutliple choice
    self.choices=choices

class Assignment(Object):
  def __init__(self, studentWorkFolder=None):
    self.studentWorkFolder=studentWorkFolder

class CourseWork(Object):
  def __init__(self, courseId=None, id=None, title=None, description=None, details=None,
               materials=[], state='PUBLISHED', alternateLink=None, 
               creationTime=None, updateTime=None, dueDate=None, dueTime=None,
               scheduledTime=None, maxPoints=0, assigneeMode='ALL_STUDENTS', 
               workType=None, submissionModificationMode='MODIFIABLE_UNTIL_TURNED_IN',
               individualStudentsOptions=None, creatorUserId=None):
    self.courseId=courseId
    self.id=id
    self.title=title
    self.description=description
    
    self.details=None
    if 'studentWorkFolder' in details:
      self.details=details['studentWorkFolder']
    elif 'choices' in details:
      self.details=details['choices']
    
    self.materials=[]
    if len(materials)>0:
      for m in materials:
        self.materials.append(CourseMaterial(**m))
        
    self.state=state
    self.alternateLink=alternateLink
    self.creationTime=creationTime
    self.updateTime=updateTime
    self.dueDate=dueDate
    self.dueTime=dueTime
    self.scheduledTime=scheduledTime,
    self.maxPoints=maxPoints,
    self.assigneeMode=assigneeMode
    self.workType=workType,
    self.individualStudentsOptions=individualStudentsOptions
    self.submissionModificationMode=submissionModificationMode
    self.creatorUserId=creatorUserId

'''
work_items=[]
with open('mock/work_items.json') as file:
  work_items_json = json.loads(file.read())['work_items']
  for a in work_items_json:
    work_items.append(CourseWork(**a))
  file.close()

class CourseWorkAPI(Resource):
  # https://classroom.googleapis.com/v1/courses/{courseId}/courseWork/{id}
  def get(self, courseId, id):
    work = [w for w in work_items if w.id==id and w.courseId==courseId]
    work[0].toJSON()
    if len(work) == 0:
        abort(404)
    response=make_response(work[0].toJSON())
    response.headers['content-type'] = 'application/json'
    return response
      
class CourseWorkListAPI(Resource):
  # https://classroom.googleapis.com/v1/courses/{courseId}/courseWork
  def get(self, courseId):
    w_list = [w for w in work_items if w.courseId==courseId]
    w_json='['
    for w in w_list:
      w_json += w.toJSON() + ','
    if len(w_json)>1:
      w_json=w_json[:-1]
    w_json+=']'
    response=make_response(w_json)
    response.headers['content-type'] = 'application/json'
    return response
'''