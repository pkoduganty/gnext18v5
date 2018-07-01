#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *
from action_handlers.activity import do_homework

from models.common import *
from models.mock import sample_announcements, sample_homeworks, sample_lessons, sample_courses

from response_generators.response import *
from response_generators.messages import *


def list_all(session, request):
  subject = request.get('queryResult').get('parameters').get('subject')
  grade = request.get('queryResult').get('parameters').get('grade') #TODO use students current grade
  grade = grade if grade is not None else 8
  
  assignments=[]
  for homework in sample_homeworks.activities:
    if grade==sample_courses.courses_id_dict[homework.courseId].grade:
      if subject is None or not subject.strip():
        assignments.append(homework)
      else: #subject is not none nor empty
        if subject==sample_courses.courses_id_dict[homework.courseId].subject:
          assignments.append(homework) # only if grade and subject match if subject is specified

  if len(assignments)==0:
    response_text = random.choice(NO_HOMEWORK).format('Susan')
    return Response(response_text).text(response_text).build()
  elif len(assignments)==1:
    return do_homework(session, assignments[0]).build()
  else:
    response_text = random.choice(PENDING_HOMEWORKS).format('Susan', len(assignments))
    items = []
    for a in assignments:
      items.append(Item(id='homework '+a.id, 
                      title=sample_courses.courses_id_dict[a.courseId].name + '-' + a.title, 
                      description=a.description))
    context = OutputContext(session, OUT_CONTEXT_HOMEWORK, type=OUT_CONTEXT_HOMEWORK)
    return Response(response_text).text(response_text).outputContext(context).select(response_text, items).build()
  
  
def select_id(session, request):
  error_text = 'Error, homework not found'  
  homeworkId=None
  for context in request.get('queryResult').get('outputContexts'):
    if context.get('name').endswith('actions_intent_option') and context.get('parameters').get('OPTION') is not None:
      option_value=context.get('parameters').get('OPTION')
      homeworkId=option_value[option_value.startswith('homework') and len('homework')+1:]

  if homeworkId is None:
    if request.get('queryResult').get('parameters').get('id') is not None:
      homeworkId=request.get('queryResult').get('parameters').get('id')
    else:
      return Response(error_text).text(error_text).build()
          
  return do_homework(session, sample_homeworks.homework_id_dict[homeworkId]).build()
  

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
    return Response(response_text).text(response_text).build()
  elif len(homework_by_subject_grade)==1:
    return do_homework(session, request, homework_by_subject_grade[0]).build()
  else:
    response_text = random.choice(PENDING_HOMEWORKS).format('Susan', len(homework_by_subject_grade))  
    items = []
    for a in homework_by_subject_grade:
      items.append(Item(id='homework '+a.id, 
                        title=sample_courses.courses_id_dict[a.courseId].name + '-' + a.title, 
                        description=a.description))
    context = OutputContext(session, OUT_CONTEXT_HOMEWORK, type=OUT_CONTEXT_HOMEWORK)
    return Response(response_text).text(response_text).outputContext(context).select(response_text, items).build()

