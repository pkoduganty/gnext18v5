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

class Announcement(Object):
  def __init__(self, courseId=None, id=None, text=None, materials=[], state='PUBLISHED',
               alternateLink=None, creationTime=None, updateTime=None, 
               scheduledTime=None, assigneeMode='ALL_STUDENTS', 
               individualStudentsOptions=None, creatorUserId=None):
    self.courseId=courseId
    self.id=id
    self.text=text
    
    self.materials=[]
    if len(materials)>0:
      for m in materials:
        self.materials.append(CourseMaterial(**m))
        
    self.state=state
    self.alternateLink=alternateLink
    self.creationTime=creationTime
    self.updateTime=updateTime
    self.scheduledTime=scheduledTime
    self.assigneeMode=assigneeMode
    self.individualStudentsOptions=individualStudentsOptions
    self.creatorUserId=creatorUserId

'''
announcements=[]
with open('mock/announcements.json') as file:
  announcements_json = json.loads(file.read())['announcements']
  for a in announcements_json:
    announcements.append(Announcement(**a))
  file.close()

class AnnouncementAPI(Resource):
  # https://classroom.googleapis.com/v1/courses/{courseId}/announcements/{id}
  def get(self, courseId, id):
    announcement = [a for a in announcements if a.id==id and a.courseId==courseId]
    if len(announcement) == 0:
        abort(404)
    response=make_response(announcement[0].toJSON())
    response.headers['content-type'] = 'application/json'
    return response
      
class AnnouncementListAPI(Resource):
  # https://classroom.googleapis.com/v1/courses/{courseId}/announcements
  def get(self, courseId):
    a_list = [a for a in announcements if a.courseId==courseId]
    a_json='['
    for a in a_list:
      a_json += a.toJSON() + ','
    if len(a_json)>1:
      a_json=a_json[:-1]
    a_json+=']'
    response=make_response(a_json)
    response.headers['content-type'] = 'application/json'
    return response
'''