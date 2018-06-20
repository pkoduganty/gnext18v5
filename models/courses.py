#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:40:44 2018

@author: praveen
"""
#import json
#from flask import jsonify, abort, make_response

from models.common import Object, Media, CourseMaterial

class Course(Object):
  def __init__(self, id=None, name=None, section=None, description=None, descriptionHeading=None, 
               room=None, ownerId=None, creationTime=None, updateTime=None, 
               enrollmentCode=None, courseState='ACTIVE', alternateLink=None, 
               teacherGroupEmail=None, courseGroupEmail=None, teacherFolder=None, 
               courseMaterialSets=None, guardiansEnabled=True, calendarId=None):
    self.id=id
    self.name=name
    self.section=section
    self.descriptionHeading=descriptionHeading
    self.description=description
    self.room=room
    self.ownerId=ownerId
    self.creationTime=creationTime
    self.updateTime=updateTime
    self.enrollmentCode=enrollmentCode
    self.courseState=courseState
    self.alternateLink=alternateLink
    self.teacherGroupEmail=teacherGroupEmail
    self.courseGroupEmail=courseGroupEmail
    self.teacherFolder=teacherFolder
    self.courseMaterialSets=courseMaterialSets
    self.guardiansEnabled=guardiansEnabled
    self.calendarId=calendarId

'''
courses=[]
with open('mock/courses.json') as file:
  courses_json = json.loads(file.read())['courses']
  for course in courses_json:
    courses.append(Course(**course))
  file.close()


class CourseAPI(Resource):
  # https://classroom.googleapis.com/v1/courses/{id}
  def get(self, id):
    course = [c for c in courses if c.id==id]
    if len(course) == 0:
        abort(404)
    response=make_response(course[0].toJSON())
    response.headers['content-type'] = 'application/json'
    return response

class CourseListAPI(Resource):
  # https://classroom.googleapis.com/v1/courses
  def get(self):
    courses_json='['
    for c in courses:
      courses_json += c.toJSON() + ','
    if len(courses_json)>1:
      courses_json=courses_json[:-1]
    courses_json+=']'
    response=make_response(courses_json)
    response.headers['content-type'] = 'application/json'
    return response
'''