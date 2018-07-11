#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:21:07 2018

@author: praveen
"""

from models.common import *
from models.announcements import Announcement

announcements=[
    Announcement(**{
      "courseId": "8Scnce",
      "id": "1",
      "text":"Today\'s Science class is cancelled, instead the Social Studies class will extend till lunch.",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    Announcement(**{
      "courseId": "8Scnce",
      "id": "2",
      "text":"Do remember your Science assignments are due this Friday.",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    Announcement(**{
      "courseId": "8SoStds",
      "id": "3",
      "text":"Gym will be closed today for routine maintenance and repairs.",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),  
    Announcement(**{
      "courseId": "8SoStds",
      "id": "4",
      "text":"Come prepared on a planet of your choice, we will play a trivia game in class.",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),  
    Announcement(**{
      "courseId": "8SoStds",
      "id": "5",
      "text":"Next thursday is the due date for submitting your essays on our solar system.",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    })  
  ]

if __name__ == '__main__':
  print('announcements: '+len(announcements))