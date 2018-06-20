#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:21:07 2018

@author: praveen
"""
from models.courses import Course
from models.common import Media, CourseMaterial

courses=[
    Course(**{
        "id": "14721899513", 
        "name": "8th Grade Social Studies", 
        "section": "A", 
        "descriptionHeading": "8th Grade Social Studies A", 
        "description": "Geography - Earth’s Hemispheres, Continents, Cartography", 
        "ownerId": "116353579384483626788", 
        "creationTime": "2018-05-26T20:10:12.481Z", 
        "updateTime": "2018-05-26T20:14:03.185Z", 
        "enrollmentCode": "wtzc5q", 
        "courseState": "ACTIVE", 
        "alternateLink": "https://web.usd475.org/school/jchs/departments/socialstudies/SiteAssets/SitePages/Home/socialstudies.gif", 
        "teacherGroupEmail": "8th_Grade_Social_Studies_A_teachers_b044feea@classroom.google.com", 
        "courseGroupEmail": "8th_Grade_Social_Studies_A_44aa2f5e@classroom.google.com", 
        "guardiansEnabled": "False", 
        "calendarId": "classroom104678386445181366460@group.calendar.google.com",
        "teacherFolder": Media(id="0Bw-peBXvH-SJflJncDJFemtQRzdVNW9rVjdwOXl5V0taQkRyRkwyRUNCNFFKT3dPQ3lhZkk", 
            title="8th Grade Social Studies A", 
            alternateLink="https://drive.google.com/drive/folders/0Bw-peBXvH-SJflJncDJFemtQRzdVNW9rVjdwOXl5V0taQkRyRkwyRUNCNFFKT3dPQ3lhZkk"
        )
    }),
    Course(**{
        "id": "14722160639", 
        "name": "7th Grade Social Studies", 
        "section": "B", 
        "descriptionHeading": "7th Grade Social Studies B", 
        "description": "Geography - Earth’s Hemispheres, Continents, Cartography", 
        "ownerId": "116353579384483626788", 
        "creationTime": "2018-05-26T20:05:37.787Z", 
        "updateTime": "2018-05-26T20:08:36.400Z", 
        "enrollmentCode": "reqjla", 
        "courseState": "ACTIVE", 
        "alternateLink": "https://web.usd475.org/school/jchs/departments/socialstudies/SiteAssets/SitePages/Home/socialstudies.gif", 
        "teacherGroupEmail": "7th_Grade_Social_Studies_B_teachers_7a5c7a12@classroom.google.com", 
        "courseGroupEmail": "7th_Grade_Social_Studies_B_eccb6487@classroom.google.com", 
        "guardiansEnabled": "False", 
        "calendarId": "classroom106976519441482224282@group.calendar.google.com",
        "teacherFolder": Media(id="0Bw-peBXvH-SJfmd2X2dWNDJXUjFnMTFLOVVWUU5hZUdJMWtqbmVZeHZNWERfcFJGekZwQlU", 
            title="7th Grade Social Studies B", 
            alternateLink="https://drive.google.com/drive/folders/0Bw-peBXvH-SJfmd2X2dWNDJXUjFnMTFLOVVWUU5hZUdJMWtqbmVZeHZNWERfcFJGekZwQlU"
         )
    }),
    Course(**{
        "id": "14722164289", 
        "name": "8th Grade Science", 
        "section": "A", 
        "descriptionHeading": "8th Grade Biology A", 
        "description":"Biology - Animal and Plant cell, Cell division",
        "ownerId": "116353579384483626788", 
        "creationTime": "2018-05-26T19:52:24.427Z", 
        "updateTime": "2018-05-26T20:09:34.010Z", 
        "enrollmentCode": "jll9jn6", 
        "courseState": "ACTIVE", 
        "alternateLink": "https://www.greatschools.org/gk/wp-content/uploads/2014/08/Science-resized-750x325.jpg", 
        "teacherGroupEmail": "8th_Grade_Biology_A_teachers_d26277fc@classroom.google.com", 
        "courseGroupEmail": "8th_Grade_Biology_A_c7f4b95f@classroom.google.com", 
        "guardiansEnabled": "False", 
        "calendarId": "classroom109210969298598032477@group.calendar.google.com",
        "teacherFolder": Media(id="0Bw-peBXvH-SJflY2eU9DWUk0MjJWekNvZkRmdlZJd3I1OHd6TGphTDFGUlJ0eUNIZlo1UUU", 
            title="8th Grade Biology A", 
            alternateLink="https://drive.google.com/drive/folders/0Bw-peBXvH-SJflY2eU9DWUk0MjJWekNvZkRmdlZJd3I1OHd6TGphTDFGUlJ0eUNIZlo1UUU"
         )
    })
  ]

courses_id_dict=dict()
for c in courses:
  courses_id_dict[c.id]=c