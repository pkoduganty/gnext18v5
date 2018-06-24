#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random

from action_handlers.session import *

from response_generators.response import Response, OutputContext, Text, Item
from response_generators.messages import *

from models.mock import sample_announcements, sample_homeworks, sample_lessons, sample_courses

def list_all(session, request):
  grade=8 #get user grade
  
  assignments=[]
  for homework in sample_homeworks.activities:
    if grade==sample_courses.courses_id_dict[homework.courseId]:
      assignments.append(homework)

  if len(assignments)==0:
    response_text = random.choice(NO_HOMEWORK)
  elif len(assignments)==1:
    response_text = random.choice(PENDING_HOMEWORK).format('Susan')
  else:
    response_text = random.choice(PENDING_HOMEWORKS).format('Susan', len(assignments))
  
  items = []
  for a in assignments:
    items.append(Item(id='homework - '+a.id, 
                      title=sample_courses.courses_id_dict[a.courseId].name + '-' + a.title, 
                      description=a.description))
  context = OutputContext(session, OUT_CONTEXT_HOMEWORK, type=OUT_CONTEXT_HOMEWORK)
  return Response(response_text).text(response_text).outputContext(context).select(response_text, items).build()

  
def select_subject(session, request):
  error_text = 'Error, homework not found'
  subject = request.get('queryResult').get('parameters').get('subject')
  grade = request.get('queryResult').get('parameters').get('grade') #TODO use students current grade
  grade = grade if grade is not None else 8
  
  courses_by_subject = sample_courses.courses_subject_dict.get(subject)
  if len(courses_by_subject)==0:
    return Response(error_text).text(error_text).build()

  course_ids_by_subject_grade = [c.id for c in courses_by_subject if c.grade==grade]
  if len(course_ids_by_subject_grade)==0:
    return Response(error_text).text(error_text).build()

  homework_by_subject_grade = [h for h in sample_homeworks.activities if h.courseId in course_ids_by_subject_grade]
    
  if len(homework_by_subject_grade)==0:
    response_text = random.choice(NO_HOMEWORK)
  elif len(homework_by_subject_grade)==1:
    response_text = random.choice(PENDING_HOMEWORK).format('Susan', homework_by_subject_grade.title)
  else:
    response_text = random.choice(PENDING_HOMEWORKS).format('Susan', len(homework_by_subject_grade))
  
  items = []
  for a in assignments:
    items.append(Item(id='homework - '+a.id, 
                      title=sample_courses.courses_id_dict[a.courseId].name + '-' + a.title, 
                      description=a.description))
  context = OutputContext(session, OUT_CONTEXT_HOMEWORK, type=OUT_CONTEXT_HOMEWORK)
  return Response(response_text).text(response_text).outputContext(context).select(response_text, items).build()

