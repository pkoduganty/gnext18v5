#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:21:07 2018

@author: praveen
"""
from models.common import Media
from models.courseworks import CourseWork, Assignment, Question

work_items = [
    CourseWork(**{
      "courseId": "14721899513",
      "id": "1",
      "title":"course 1 - assignment 1",
      "description":"course 1 - assignment 1 - ",
      "details": { 
        "studentWorkFolder": Assignment(studentWorkFolder=Media(
          id="1",
          title="folder: course1 - assignment1",
          alternativeLink="http://localhost:8080/course1/assignment1"
        ))
      },
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "workType": "ASSIGNMENT",
      "creatorUserId":"116353579384483626788"
    }),
    CourseWork(**{
      "courseId": "14721899513",
      "id": "2",
      "title":"course 1 - multiple choice 1",
      "description":"course 1 - multiple choice 1 - ",
      "details": { 
        "choices":Question(choices=[
          "choice1",
          "choice2",
          "choice3"
        ])
      },
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "workType": "MULTIPLE_CHOICE_QUESTION",
      "creatorUserId":"116353579384483626788"
    }),
    CourseWork(**{
      "courseId": "14722160639",
      "id": "3",
      "title":"course 2 - assignment 1",
      "description":"course 2 - assignment 1 - ",
      "details": { 
        "studentWorkFolder": Assignment(Media(
          id="1",
          title="folder: course2 - assignment1",
          alternativeLink="http://localhost:8080/course2/assignment1"
        ))
      },
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "workType": "ASSIGNMENT",
      "creatorUserId":"116353579384483626788"
    }),  
    CourseWork(**{
      "courseId": "14722164289",
      "id": "4",
      "title":"course 3 - multiple choice 1",
      "description":"course 3 - multiple choice 1 - ",
      "details": { 
        'choices':Question(choices=[
              "choice1",
              "choice2",
              "choice3"
          ]
        )
      },
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "workType": "MULTIPLE_CHOICE_QUESTION",
      "creatorUserId":"116353579384483626788"
    }),  
    CourseWork(**{
      "courseId": "14722164289",
      "id": "5",
      "title":"course 3 - multiple choice 2",
      "description":"course 3 - multiple choice 2 - ",
      "details": { 
        'choices':Question(choices=[
              "choice1",
              "choice2",
              "choice3"
          ]
        )
      },
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "dueDate":"2018-06-25",
      "dueTime":"15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "workType": "MULTIPLE_CHOICE_QUESTION",
      "creatorUserId":"116353579384483626788"
    })  
  ]
