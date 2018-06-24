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

GENERAL_FALLBACKS=[
    u"I didn't get that. Can you say it again?",
    u"I missed what you said. Say it again?",
    u"Sorry, could you say that again?",
    u"Sorry, can you say that again?",
    u"Can you say that again?",
    u"Sorry, I didn't get that.",
    u"Sorry, what was that?",
    u"One more time?",
    u"Say that again?",
    u"I didn't get that.",
    u"I missed that.",
    u"Couldn\'t understand, try again?"
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

NO_HOMEWORK=[
    u'{0}, you have no homework today',
    u'{0}, no homework today'
]

# 0:user, 1:#of assignments
PENDING_HOMEWORKS=[
    u'{0}, you have {1} assignments pending, start with the first ?',
    u'{0}, {1} assignments due, do them now ?'
]

# 0:user, 1:assignment-title
PENDING_HOMEWORK=[
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

LESSON_MATERIAL_SELECT=[
    u'Lesson has these study materials, choose one?',
    u'Here are your study materials, select one'
]