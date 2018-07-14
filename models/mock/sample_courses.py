#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:21:07 2018

@author: praveen
"""
from models.courses import Course
from models.common import *

courses=[
    Course(**{
        "id": "8SoStds", 
        "name": "8th Grade Social Studies", 
        "section": "A", 
        "grade":8,
        "subject":"SOCIAL_STUDIES",
        "descriptionHeading": "8th Grade Social Studies A", 
        "description": "Geography - Solar System, Our Planet - Earth", 
        "ownerId": "116353579384483626788", 
        "creationTime": "2018-05-26T20:10:12.481Z", 
        "updateTime": "2018-05-26T20:14:03.185Z", 
        "courseState": "ACTIVE", 
        "imageUri": "https://gnext18-v5.appspot.com/play/img/social_studies.jpg", 
        "calendarId": "classroom104678386445181366460@group.calendar.google.com"
    }),
    Course(**{
        "id": "8Scnce", 
        "name": "8th Grade Science", 
        "section": "A", 
        "grade":8,
        "subject":"SCIENCE",
        "descriptionHeading": "8th Grade Biology A", 
        "description":"Biology - Animal and Plant cell, Cell division",
        "ownerId": "116353579384483626788", 
        "creationTime": "2018-05-26T19:52:24.427Z", 
        "updateTime": "2018-05-26T20:09:34.010Z", 
        "courseState": "ACTIVE", 
        "imageUri": "https://gnext18-v5.appspot.com/play/img/science.jpg", 
        "calendarId": "classroom109210969298598032477@group.calendar.google.com"
    })
  ]

courses_id_dict=dict()
for c in courses:
  courses_id_dict[c.id]=c
  
courses_grade_dict=dict()
for c in courses:
  if courses_grade_dict.get(c.grade) is None:
    courses_grade_dict[c.grade]=[]
  courses_grade_dict[c.grade].append(c)
  
courses_subject_dict=dict()
for c in courses:
  if courses_subject_dict.get(c.subject) is None:
    courses_subject_dict[c.subject]=[]
  courses_subject_dict[c.subject].append(c)
  
if __name__ == '__main__':
  print('courses: '+len(courses))