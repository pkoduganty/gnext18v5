#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 01:54:16 2018

@author: praveen
"""

from models.common import *
from models.courses import Lesson

lessons = [
  Lesson(**{
    "id": "1234",
    "name": "Our Solar System",
    "courseId": "14721899513", 
    "description": "8th Grade Social Studies",
    "materials": [
        Video(**{
          "title":'Planets of our Solar System',
          "url":'https://www.youtube.com/watch?v=libKVRa01L8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/8/8c/Systeme_solaire_fr.jpg'
        })
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/8/8c/Systeme_solaire_fr.jpg',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  }),
  Lesson(**{
    "id": "2345",
    "name": "Our Earth",
    "courseId": "14722160639", 
    "description": "7th Grade Social Studies",
    "materials": [
        Video(**{
          "title":'Layers of Earth',
          "url":'https://www.youtube.com/watch?v=3xLiOFjemWQ',
          "imageUri":'https://3.bp.blogspot.com/-MCsbIihWzMI/V8zLCDW1VAI/AAAAAAAAGyQ/iCEhWGNn5cQx7Q6zz2CsEn0oHxs80NiMwCLcB/s1600/layers-of-earth.gif'
        })
    ],
    "imageUri":'https://3.bp.blogspot.com/-MCsbIihWzMI/V8zLCDW1VAI/AAAAAAAAGyQ/iCEhWGNn5cQx7Q6zz2CsEn0oHxs80NiMwCLcB/s1600/layers-of-earth.gif',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  }),
  Lesson(**{
    "id": "3456",
    "name": "The Cell",
    "courseId": "14722164289", 
    "description": "8th Grade Science",
    "materials": [
        Video(**{
          "title":'Cell structure and function',
          "url":'https://www.youtube.com/watch?v=URUJD5NEXC8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png'
        }),
    ],
    "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png',
    "activeFromDate":"27/06/2018",
    "activeTillDate":"27/08/2018"
  })
]

lesson_id_dict=dict()
for l in lessons:
  lesson_id_dict[l.id]=l

courses_id_dict=dict()
for l in lessons:
  if courses_id_dict.get(l.courseId) is None:
    courses_id_dict[l.courseId]=[]
  courses_id_dict[l.courseId].append(l)
  