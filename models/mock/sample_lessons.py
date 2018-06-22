#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:54:16 2018

@author: praveen
"""

import os
#from docx import Document

from models.courses import Lesson

lessons = [
  Lesson(**{
    "id": "1234",
    "name": "Our Solar System",
    "courseId": "14721899513", 
    "description": "8th Grade Social Studies"
  }),
  Lesson(**{
    "id": "2345",
    "name": "Our Earth",
    "courseId": "14722160639", 
    "description": "7th Grade Social Studies"
  }),
  Lesson(**{
    "id": "3456",
    "name": "The Cell",
    "courseId": "14722164289", 
    "description": "8th Grade Science"
  })
]

courses_id_dict=dict()
for l in lessons:
  if courses_id_dict.get(l.courseId) is None:
    courses_id_dict[l.courseId]=[]
  courses_id_dict[l.courseId].append(l)
  
'''
for i in range(len(sample_lessons)):
  document = Document(sample_lessons[i]["file"])
  sections=[]
  section=None
  text=''
  for para in document.paragraphs:
    if para.style.name=='Heading 2':
      if section is not None:
        sections.append({"name":section, "text":text})
      section=para.text
      text=''
    elif para.style.name in ['Normal', 'BodyText', 'BodyText2', 'BodyText3', 'Caption', 'Quote']:
      text=text+'\n'+para.text
  sections.append({"name":section, "text":text}) #last section has no further headings below it
  sample_lessons[i]["sections"]=sections
  #print(sections)

if __name__ == '__main__':
  for lesson in sample_lessons:
    for section in lesson['sections']:
      print('Section: '+section["name"]+', text: '+section["text"])
'''