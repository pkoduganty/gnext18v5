#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:49:03 2018

@author: praveen
"""
WELCOME_SUGGESTIONS=[
    u"do your homework",
    u"go to class",
    u"take a quiz",
    u"list my classes",
    u"read announcements"
]

WELCOME_TEXT=[
    u'<speak><prosody rate="80%">You might want to do your homework, \
        <break time="300ms"/> or review a lesson,\
        <break time="300ms"/> <emphasis strength="strong">oh</emphasis> \
        or maybe a quick quiz</prosody></speak>',
    u'<speak>Do your homework,<break time="300ms"/> or read a lesson,<break time="300ms"/>\
        ah maybe a quick quiz</speak>',
    u'<speak>Do your homework,<break time="300ms"/> or read a lesson,<break time="300ms"/>\
        ah maybe a quick qu iz</speak>',
    u'<speak>Do your homework,<break time="300ms"/> or read a lesson,<break time="300ms"/>\
        ah maybe a quick quiz</speak>',
    u'<speak>Do your homework,<break time="300ms"/> or read a lesson,<break time="300ms"/>\
        ah maybe a quick quiz</speak>',
    u'<speak>Do your homework,<break time="300ms"/> or read a lesson,<break time="300ms"/>\
        ah maybe a quick quiz</speak>'
]

# 0:user 
WELCOME_BASIC=[
    u'<speak>Hello <emphasis>{0}</emphasis>, every day is a learning day \
      <audio src="https://actions.google.com/sounds/v1/alarms/bugle_tune.ogg">\
      the learning bugle</audio></speak>',
    u'<speak>Padawan <emphasis>{0}</emphasis>, so eager to learn you are <break time="200ms"/> let the learning begin</speak>',
    u'<speak><emphasis>{0}</emphasis>, kindle your curiosity</speak>',
    u'<speak><emphasis>{0}</emphasis>, I can help you with </speak>',
    u'<speak><emphasis>{0}</emphasis>, let us begin with </speak>'
]

WELCOME_SECOND_LOGON=[
    u"Welcome back {0}, how can I help you?", 
    u"Welcome back, start from where you left off?"
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
    u'{0}, you have {1} assignments pending, choose to get started',
    u'{0}, {1} assignments due'
]

# 0:user, 1:assignment-title
PENDING_HOMEWORK=[
    u'{0}, assignment {1} pending, begin now?',
    u'{0}, do you want to start your assignment {1} now ?'
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

QUIZ_SELECT=[
    u'which quiz do you want to take?',
    u'Here are your quizzes, select one'
]

LESSON_ACTIVITY_SELECT=[
    u'Lesson has these study materials, choose one',
    u'Here are your study materials, select one'
]

LESSON_ACTIVITY_DO=[
    u'Do this activity now'
]

INCORRECT_ANSWER=[
    u'INCORRECT\nCorrect answer for question - {0} is {1}'
]

CORRECT_ANSWER=[
    u'CORRECT\nCorrect answer for - {0} is indeed {1}',
    u'RIGHT\nanswer for - {0} is {1}'
]

QUIZ_REPORT=[
    u'You got {0} out of {1} right'
]

CONCEPT_DEFINITION_UNKNOWN=[
    u'I am afraid, I don\'t know what {0} means, do check with your teacher or elders.',
    u'Sorry, don\'t know what {0} is'
]

GENERAL_FALLBACKS=[
    u'<speak>I didn\'t get that. <break time="300ms"/> <prosody rate="medium" pitch="-2st">Can you say it again?</prosody></speak>',
    u'<speak>Ohh! I missed what you said.<break time="300ms"/> <prosody rate="medium" pitch="-2st">Say it again?</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/> <prosody rate="medium" pitch="-2st"> could you say that again?</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/>  <prosody rate="medium" pitch="-2st">can you say that again?</prosody></speak>',
    u'<speak><prosody rate="slow" pitch="-2st">Can you say that again?</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/>  <prosody rate="medium" pitch="-2st">I didn\'t get that.</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/>  <prosody rate="medium" pitch="-2st">what was that?</prosody></speak>',
    u'<speak>One more time?</speak>',
    u'<speak>Say that again?</speak>',
    u'<speak>I didn\'t get that.</speak>',
    u'<speak>I missed that.</speak>',
    u'<speak>Couldn\'t understand, <break time="200ms"/> try again?</speak>'
]
