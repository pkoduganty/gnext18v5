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
      "courseId": "14721899513",
      "id": "1",
      "text":"course 1 - announcement 1",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    Announcement(**{
      "courseId": "14721899513",
      "id": "2",
      "text":"course 1 - announcement 2",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),
    Announcement(**{
      "courseId": "14722160639",
      "id": "3",
      "text":"course 2 - announcement 1",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),  
    Announcement(**{
      "courseId": "14722164289",
      "id": "4",
      "text":"course 3 - announcement 1",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    }),  
    Announcement(**{
      "courseId": "14722164289",
      "id": "5",
      "text":"course 3 - announcement 2",
      "state":"PUBLISHED",
      "creationTime":"2018-06-25T15:01:23.045123456Z",
      "updateTime":"2018-06-25T15:01:23.045123456Z",
      "scheduledTime":"2018-07-05T15:01:23.045123456Z",
      "creatorUserId":"116353579384483626788"
    })  
  ]

if __name__ == '__main__':
  print('announcements: '+len(announcements))