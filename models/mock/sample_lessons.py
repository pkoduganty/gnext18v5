#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:54:16 2018

@author: praveen
"""

#import os
#from docx import Document

lessons = [
  {
    "id": "1234",
    "name": "Our Solar System",
    "file": "lessons/OurSolarSystemLesson.docx",
    "courseId": "14721899513", 
    "courseName": "8th Grade Social Studies"
  }
]
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