#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import json
import random
import logging
from datetime import datetime

from action_handlers.session import *
from action_handlers.activity import do_homework, do_activity

from response_generators.messages import *
from response_generators.response import Response, OutputContext, Text, Item

from models.common import *
from models.activities import *
from models.mock import sample_announcements, sample_courses, sample_lessons, sample_homeworks

from SPARQLWrapper import SPARQLWrapper, JSON

from googleapiclient.discovery import build

class Concept(Object):
  def __init__(self, name, types, short_desc, image, long_desc):
    self.name=name
    self.types=types
    self.short_description=short_desc
    self.imageUri=image
    self.long_description=long_desc

def google_kgraph_lookup(concept, types):
  service = build("kgsearch", "v1", developerKey='AIzaSyBPobZc7OwY6D_XcOThmqst2Lpl9c3Ggas') #TODO hardcoded
  if types and len(types)>0:
    result = service.entities().search(prefix=True, query=concept, types=types, languages='en', limit=5).execute()
  else:
    result = service.entities().search(prefix=True, query=concept, languages='en', limit=5).execute()
  logging.info('Knowledge Graph Response = %s', json.dumps(result))
  
  items=[]
  for item in result.get('itemListElement'):
    logging.info('ItemListElement=%s', json.dumps(item))
    if (item and item.get('result') and item.get('result').get('detailedDescription') and 
        item.get('result').get('detailedDescription').get('articleBody')):
      concept=Concept(
          item.get('result').get('name').encode('ascii', 'ignore'),
          item.get('result').get('@type'),
          item.get('result').get('description').encode('ascii', 'ignore'),
          item.get('result').get('image').get('url').encode('ascii', 'ignore') if item.get('result').get('image').get('url') else None,
          item.get('result').get('detailedDescription').get('articleBody').encode('ascii', 'ignore')
          )
      items.append(concept)
  return items
  
def google_csearch(query):
  service = build("customsearch", "v1",
            developerKey="AIzaSyDRRpR3GS1F1_jKNNM9HCNd2wJQyPG3oN0")

  res = service.cse().list(
      q=query,
      cx='017576662512468239146:omuauf_lfve',
    ).execute()
  return res


def dbpedia_concept_lookup(concept):
  query = '''PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>    
    SELECT DISTINCT ?desc  WHERE {{
              ?subj rdfs:comment ?desc.
              FILTER( LANG(?desc)="en" )
              ?subj rdfs:label ?label.
              FILTER( lcase(str(?label)) = lcase(str("{0}")) )
            }} LIMIT 1
    '''.format(concept)
    
  sparql = SPARQLWrapper("http://dbpedia.org/sparql")
  sparql.setQuery(query)
  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()
  logging.debug('SPARQL Response = %s', json.dumps(results))
  
  if results and results.get('results') and results.get('results').get('bindings') and len(results.get('results').get('bindings'))>0:
    binding=results.get('results').get('bindings')[0]
    if binding.get('desc') and binding.get('desc').get('value'):
      return binding.get('desc').get('value').encode('ascii', 'ignore')
  return None


def course_id(session, courseId):
  response_text = random.choice(LESSON_SELECT)
  context = OutputContext(session, OUT_CONTEXT_COURSE, type=OUT_CONTEXT_COURSE)
  select_cards = []
  lessons = sample_lessons.courses_id_dict.get(courseId.strip())
  logging.debug('courseId: %s, %d lessons in course', courseId, len(lessons))
  if lessons is not None:
    for lesson in lessons:
      card=Item('lesson '+lesson.id, lesson.name, lesson.description)
      select_cards.append(card)
  return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()


def lesson_id(session, lessonId):
  logging.debug('lessonId: %s', lessonId)
  response_text = random.choice(LESSON_ACTIVITY_SELECT)
  context = OutputContext(session, OUT_CONTEXT_LESSON_ACTIVITY, type=OUT_CONTEXT_LESSON_ACTIVITY)
  select_cards = []
  lesson = sample_lessons.lesson_id_dict.get(lessonId.strip())
  if lesson is not None:
    for m in lesson.materials:
      logging.debug('activity type=%s, %s',type(m), m)
      if isinstance(m, Video):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Text):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Link):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Audio):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
      elif isinstance(m, Quiz):
        select_cards.append(Item(id='activity '+m.id, title=m.title, imageUri=m.imageUri))
    return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()
  error_text = 'Error, lesson not found'
  return Response(error_text).text(error_text).build()


def homework_id(session, homeworkId):
  assignment = sample_homeworks.homework_id_dict.get(homeworkId.strip())
  return do_homework(session, assignment).build()


def activity_id(session, activityId):
  activity=sample_lessons.activity_id_dict.get(activityId.strip())
  if activity is None: #homework activity
    activity=sample_homeworks.activity_id_dict.get(activityId.strip())
    logging.debug('found activity %s', activity.title)
  else:
    logging.debug('found activity %s', activity.title)
  
  return do_activity(session, activity).build()
