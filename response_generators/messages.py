#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:49:03 2018

@author: praveen
"""

WELCOME_SUGGESTIONS=[
    u"list my classes",
    u"read announcements",
    u"pending assignments",
    u"take quiz",
    u"go to class"
]

# 0:user, 1:# of announcements
UNREAD_ANNOUNCEMENTS=[
    u'Hey {0}, you have {1} new announcements',
    u'{0}, {1} new announcements'
]

# 0:user, 1:announcement
UNREAD_ANNOUNCEMENT=[
    u'Hey {0}, an announcement for you',
    u'{0}, you have one announcement'
]

NO_UNREAD_ANNOUNCEMENTS=[
    u'No new announcements for you'
]

# 0:user, 1:#of assignments
PENDING_ASSIGNMENTS=[
    u'{0}, you have {1} assignments pending, start with the first ?',
    u'{0}, {1} assignments due, do them now ?'
]

# 0:user, 1:assignment-title
PENDING_ASSIGNMENT=[
    u'{0}, assignment {1} pending, begin now?',
    u'{0}, do you want to start your assignment {1} now ?'
]

# 0:user 
WELCOME_BASIC=[
    u'Hello {0}, every day\'s a learning day, what can I help you with ?',
    u'Dear {0}, let the learning begin, here\'s what we can do ?',
    u'{0}, kindle your curiosity, let us begin with ',
    u'{0}, I can help you with ',
    u'{0}, let us begin with ',
    u'what do you want to do first '
]

COURSE_SELECT=[
    u'which class would you want to begin with ?',
    u'select a class to start ',
    u'you\'re enrolled for the following, select one'
]

LESSON_SELECT=[
    u'which lesson do you want to study?',
    u'Here are your lessons, select one'
]
