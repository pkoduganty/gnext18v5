#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:21:07 2018

@author: praveen
"""
from models.common import *
from models.activities import *
from models.homeworks import *

activities = [
    Homework(**{
      "courseId": "8SoStds",
      "id": "8SoStdsHW1",
      "title":"Video: Planets of our Solar System",
      "description":"A informative NatGeo video on our Solar System Planets",
      "activity": Video(**{
          "id":"v001",
          "title":'Video: Planets of our Solar System',
          "url":'https://www.youtube.com/watch?v=libKVRa01L8',
          "imageUri":'https://img.youtube.com/vi/libKVRa01L8/default.jpg'
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    Homework(**{
      "courseId": "8SoStds",
      "id": "8SoStdsHW2",
      "title":"Quiz: Our Planets",
      "description":"Test your understanding of our planets",
      "activity": Quiz(**{
        "id":"qz001",
        "title":'Quiz on our planets',
        "description":"Test your understanding of our planets, each question is worth 5 points.",
        "imageUri": 'https://upload.wikimedia.org/wikipedia/commons/2/22/Astronomy_Amateur_3_V2.jpg',
        "questions":[
            Question(**{
                "id":"qt001",
                "question":'which planet is the farthest from the sun?',
                "answers":["neptune"],
                "choices":["mercury","uranus","neptune","pluto"]
                }),
            Question(**{
                "id":"qt002",
                "question":'which planet has the largest number of natural satellites?',
                "answers":["jupiter"],
                "choices":["jupiter","uranus","neptune","saturn"]
                }),
            Question(**{
                "id":"qt003",
                "question":'which planets in our solar system have rings?',
                "answers":["all", "giant planets", "neptune","jupiter","uranus","saturn"],
                "choices":["neptune","jupiter","uranus","saturn","all giant planets"]
                })
        ]
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    Homework(**{
      "courseId": "8Scnce",
      "id": "8ScnceHW3",
      "title":"Read: The Cell - The building block of all organisms",
      "description":"Understand basic components of all cells",
      "activity": Text(**{
          "id":"t001",
          "title":'Read: The Cell',
          "text":'''The Cell is the smallest unit structure of all organisms. All cells are made by the division of other cells. 
            The cell membrane is a thin flexible layer around the cell and seperates the outside environment from the cytoplasm inside the cell. It is sometimes called the plasma membrane or cytoplasmic membrane. 
            Cytoplasm is the gel-like material inside the cell, which along with other parts called organelles (like small organs) are inside the cell membrane.
            Organelles each do different things in the cell. Examples are the nucleus which is the most important like our brain and mitochondria which generates chemical energy for the cell.''',
          "imageUri":'https://upload.wikimedia.org/wikipedia/commons/8/83/Celltypes.svg'
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),  
    Homework(**{
      "courseId": "8Scnce",
      "id": "8ScnceHW5",
      "title":"Video: Cell structure and function",
      "description":"Understand cell structure, parts and their function",
      "activity": Video(**{
          "id":"v022",
          "title":'Video: Cell structure and function',
          "url":'https://www.youtube.com/watch?v=URUJD5NEXC8',
          "imageUri":'https://img.youtube.com/vi/URUJD5NEXC8/default.jpg'
       }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    
    Homework(**{
      "courseId": "8Scnce",
      "id": "8ScnceHW4",
      "title":"Quiz: The Cell",
      "description":"Test your knowledge of the cell",
      "activity": Quiz(**{
        "id":"qz002",
        "title":'Quiz: The Cell',
        "description":"Test your knowledge of the cell, each question is worth 5 points.",
        "imageUri":'https://upload.wikimedia.org/wikipedia/commons/3/37/Wilson1900Fig2.jpg',
        "questions":[
            Question(**{
                "id":"qt011",
                "question":'I protect the cell from the harsh external world, who am I?',
                "answers":["cell wall", "cell membrane", "membrane", "plasma membrane", "cytoplasmic membrane"],
                "choices":["nucleus","cell membrane","cytoplasm","mitochondria",]
                }),
            Question(**{
                "id":"qt012",
                "question":'I am the brains of the cell, who am I?',
                "answers":["nucleus"],
                "choices":["cell membrane","cytoplasm","nucleus","mitochondria"]
                }),
            Question(**{
                "id":"qt013",
                "question":'What organelle provides support for the cell, who is that?',
                "answers":["cell wall"],
                "choices":["cytoplasm","cell wall","ribosomes","nucleus"]
            }),
            Question(**{
                "id":"qt014",
                "question":'Which one of the follwing are made up of genes and protein, which contain DNA?',
                "answers":["chromosomes"],
                "choices":["chromosomes","cytoplasm","ribosomes","nucleus"]
            })
        ]
      }),
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    })
  ]

homework_id_dict=dict()
for h in activities:
  homework_id_dict[h.id]=h
  
activity_id_dict=dict()
for h in activities:
  activity_id_dict[h.activity.id]=h.activity

if __name__ == '__main__':
  print('homeworks: '+len(activities))