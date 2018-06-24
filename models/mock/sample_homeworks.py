#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:21:07 2018

@author: praveen
"""
from models.common import *
from models.homeworks import *

activities = [
    Homework(**{
      "courseId": "14721899513",
      "id": "1",
      "title":"course 1 - assignment 1",
      "description":"course 1 - assignment 1 - ",
      "activity": Video(**{
          "title":'Planets of our Solar System',
          "url":'https://www.youtube.com/watch?v=libKVRa01L8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/8/8c/Systeme_solaire_fr.jpg'
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "type": ActivityType.VIDEO.value,
      "creatorUserId":"116353579384483626788"
    }),
    Homework(**{
      "courseId": "14721899513",
      "id": "2",
      "title":"course 1 - multiple choice 1",
      "description":"course 1 - multiple choice 1 - ",
      "activity": Quiz(**{ 
        "title":'Quiz on our planets',
        "questions":[
            Question(**{
                "question":'which planet is the farthest from the sun?',
                "answers":["neptune"],
                "choices":["mercury","uranus","neptune","pluto"]
                }),
            Question(**{
                "question":'which planet is the largest number of natural satellites?',
                "answers":["jupiter"],
                "choices":["jupiter","uranus","neptune","saturn"]
                }),
            Question(**{
                "question":'how far is the earth from the sun?',
                "answers":["one au", "1 au", "one astronomial unit","1 astronomial unit", 
                           "149.6 million kilometers", "150 million kilometers"
                           "149600000 kilometers", "150000000 kilometers"
                           ],
                "choices":["1 million kilometers","149.6 million kilometers","57.91 million kilometers","108.2 million kilometers"]
                })
        ]
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "type": ActivityType.QUIZ.value,
      "creatorUserId":"116353579384483626788"
    }),
    Homework(**{
      "courseId": "14722160639",
      "id": "3",
      "title":"course 2 - assignment 1",
      "description":"course 2 - assignment 1 - ",
      "activity": Text(**{
          "title":'The Cell',
          "text":'''The cell is the basic smallest unit structure of all organisms. All cells are made by the division of other cells. 
          The cell membrane is a thin flexible layer around the cell and seperates the outside environment from the cytoplasm inside the cell. It is sometimes called the plasma membrane or cytoplasmic membrane. 
          Cytoplasm is the gel-like material inside the cell, which along with other parts called organelles (like small organs) are inside the cell membrane.
          Organelles each do different things in the cell. Examples are the nucleus which is the most important like our brain and mitochondria which generates chemical energy for the cell.''',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png'
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "type": ActivityType.TEXT.value,
      "creatorUserId":"116353579384483626788"
    }),  
    Homework(**{
      "courseId": "14722164289",
      "id": "4",
      "title":"course 3 - multiple choice 1",
      "description":"course 3 - multiple choice 1 - ",
      "activity": Quiz(**{ 
        "title":'Quiz on cells',
        "questions":[
            Question(**{
                "question":'I protect the cell from the harsh external world, who am I?',
                "answers":["cell wall", "cell membrane", "membrane", "plasma membrane", "cytoplasmic membrane"],
                "choices":["nucleus","cell membrane","cytoplasm","mitochondria"]
                }),
            Question(**{
                "question":'I am the brains of the cell, who am I?',
                "answers":["nucleus"],
                "choices":["cell membrane","cytoplasm","nucleus","mitochondria"]
                })
        ]
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "type": ActivityType.QUIZ.value,
      "creatorUserId":"116353579384483626788"
    }),  
    Homework(**{
      "courseId": "14722164289",
      "id": "5",
      "title":"course 3 - multiple choice 2",
      "description":"course 3 - multiple choice 2 - ",
      "activity": Video(**{
          "title":'Cell structure and function',
          "url":'https://www.youtube.com/watch?v=URUJD5NEXC8',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Simple_diagram_of_animal_cell_%28en%29.svg/512px-Simple_diagram_of_animal_cell_%28en%29.svg.png'
       }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "type": ActivityType.VIDEO.value,
      "creatorUserId":"116353579384483626788"
    })  
  ]

homework_id_dict=dict()
for h in activities:
  homework_id_dict[h.id]=h

if __name__ == '__main__':
  print('homeworks: '+len(activities))