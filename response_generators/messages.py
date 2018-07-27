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
    (
        u'You might want to do your homework, or review a lesson or maybe a quick quiz',
        u'<speak><prosody rate="90%">You might want to do your homework, \
        <break time="300ms"/> or review a lesson,\
        <break time="300ms"/> and <emphasis strength="strong">or</emphasis> \
        maybe a quick quiz</prosody></speak>'
    ),
    (
        u'Let us start with your homework, and then a quick quiz perhaps',
        u'<speak><prosody rate="90%">Let us start with your homework,<break time="300ms"/> \
        and then a quick quiz perhaps</prosody></speak>'
    ),
    (
        u'Do your homework, or read a lesson, then maybe a quick quiz',
        u'<speak><prosody rate="90%">Do your homework,<break time="300ms"/> \
        or read a lesson,<break time="300ms"/>\
        then maybe a quick quiz</prosody></speak>'
    )
]


ANTHEM=[
    (
        u'You have brains in your head,\
You have feet in your shoes,\
You can steer yourself any direction you choose,\
You’re on your own and you know what you know,\
And you’re the guy who will decide where to go,\
Oh the places you’ll go.',

        u'''
        <speak>
            <par>
              <media>
                  <audio src="https://gnext18-v5.appspot.com/play/all-by-myself_z1Xv2LBO.mp3" soundLevel="-5dB"></audio>
              </media>
              <media>
                <speak>
                    <p>
                        <s>You have brains in your head</s>
                        <s><prosody rate="80%">You have feet in your shoes</prosody>
                            <break strength="weak"/></s>
                    </p>
                    <p>
                        <s>You can steer yourself any direction you choose</s>
                        <s><prosody rate="80%">You’re on your own and you know what you know</prosody></s>
                    </p>
                    <p>
                        <s>And you’re the guy who will decide where to go<break time="600ms"/></s>
                        <s><prosody rate="slow">
                            <emphasis>Oh the places you’ll go</emphasis>
                          </prosody>
                        </s>
                    </p>
                </speak>
              </media>
            </par>
        </speak>'''
    )
]


# 0:user 
WELCOME_BASIC=[
    (
        u'Hello {0}, How was your day at school? You know, every day is a learning day.',
        u'<speak><par>\
            <media>\
              <speak><prosody rate="90%">\
                <emphasis strength="strong">Hello {0}</emphasis>,\
                How was your day at school? You know, every day is a learning day </prosody>\
              </speak>\
            </media>\
            <media soundLevel="-10dB" fadeInDur="3s" fadeOutDur="1s">\
              <audio clipEnd="7s" src="https://gnext18-v5.appspot.com/play/snow-white-logo_fy1ZYrVd.mp3">\
              the learning bugle\
              </audio>\
            </media>\
        </par></speak>'
    ),
    (
        u'Padawan {0}, so eager to learn you are, let the learning begin this morning, enjoy your day at school. ',
        u'<speak><par>\
            <media>\
              <speak>\
                <prosody rate="90%">\
                <emphasis strength="strong">Padawan {0}</emphasis>, \
                so eager to learn you are \
                <break time="500ms"/> let the learning begin this morning, enjoy your day at school. </prosody>\
              </speak>\
            </media>\
            <media soundLevel="-10dB" fadeInDur="3s" fadeOutDur="1s">\
              <audio clipEnd="7s" src="https://gnext18-v5.appspot.com/play/paradise-on-earth_GJ6JNIBO.mp3">\
              the learning bugle\
              </audio>\
            </media>\
        </par></speak>'
    ),
    (
        u'{0}, ready for school? an opportunity to learn something new today, pinch of curiosity will help.',
        u'<speak><par>\
            <media><speak><prosody rate="90%">\
              <emphasis strength="strong">{0}</emphasis>, \
              ready for school? an opportunity to learn something new today, pinch of curiosity will help.\
              </prosody></speak>\
            </media>\
            <media soundLevel="-10dB" fadeInDur="3s" fadeOutDur="1s">\
              <audio clipEnd="7s" src="https://gnext18-v5.appspot.com/play/ultimate-victory_fyiYEQB_.mp3">\
              the learning bugle\
              </audio>\
            </media>\
        </par></speak>'
    )
]

WELCOME_SECOND_LOGON=[
    (
        u"Welcome back {0},  ",
        u'<speak><par>\
            <media><speak><prosody rate="90%">\
              Welcome back <emphasis strength="strong">{0}</emphasis></prosody></speak>\
            </media>\
            <media soundLevel="-10dB" fadeInDur="3s" fadeOutDur="1s">\
              <audio clipEnd="7s" src="https://gnext18-v5.appspot.com/play/ultimate-victory_fyiYEQB_.mp3">\
              the learning bugle\
              </audio>\
            </media>\
        </par></speak>'
    ),
    (
        u"Welcome back, I know you are very curious to learn.\n Do you want to start where you left off?",
        u'<speak><par>\
            <media><speak><prosody rate="90%">\
              start where you left off?</prosody></speak>\
            </media>\
            <media soundLevel="-10dB" fadeInDur="3s" fadeOutDur="1s">\
              <audio clipEnd="7s" src="https://gnext18-v5.appspot.com/play/ultimate-victory_fyiYEQB_.mp3">\
              the learning bugle\
              </audio>\
            </media>\
        </par></speak>'
    )
]

# 0:user, 1:# of announcements
UNREAD_ANNOUNCEMENTS=[
    (
        u'Hey {0}, you have {1} new announcements',
        u'<speak><prosody rate="90%"><emphasis strength="strong">Hey {0}</emphasis>,\
      you have {1} new announcements</prosody></speak>'
      ),
      (
           u'{0}, {1} new announcements',
          u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, \
      {1} new announcements</prosody></speak>'
      )
    
    
    
]

# 0:user, 1:announcement
UNREAD_ANNOUNCEMENT=[
    (
        u'Hey {0}, an announcement for you',
    u'<speak><prosody rate="90%"><emphasis strength="strong">Hey {0}</emphasis>,\
      an announcement for you</prosody></speak>',
    ),
    (
        u'{0}, you have one announcement',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>,\
      you have one announcement</prosody></speak>'
    )
]

NO_UNREAD_ANNOUNCEMENTS=[
    u'No new announcements for you'
]

NO_HOMEWORK=[
    (
        u'{0}, you have no homework today.',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, \
      <audio src="https://gnext18-v5.appspot.com/play/cartoon-male-hooray-shouts_MJiAcHEO.mp3" clipEnd="1">Hooray!</audio> \
      you have no homework today</prosody></speak>',
    ),
    (
         u'{0}, no homework today.',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, \
      <audio src="https://gnext18-v5.appspot.com/play/cartoon-male-hooray-shouts_MJiAcHEO.mp3" clipEnd="1">Hooray!</audio> \
      no homework today</prosody></speak>'
    )
]

# 0:user, 1:#of assignments
PENDING_HOMEWORKS=[
    (
        u'{0}, you have {1} assignments pending, choose to get started',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, you have {1} assignments pending, choose to get started</prosody></speak>',
    ) ,
    (
        u'{0}, {1} assignments due',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, {1} assignments due</prosody></speak>'
    )
    ]

# 0:user, 1:assignment-title
PENDING_HOMEWORK=[
    (
        u'{0}, homework on {1} is due today, begin now?',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, homework on {1} is due today, begin now?</prosody></speak>',
    ) ,
    (
        u'{0}, let us do your homework on {1} now?',
    u'<speak><prosody rate="90%"><emphasis strength="strong">{0}</emphasis>, let us do your homework on {1} now?</prosody></speak>'
    )
]

COURSE_SELECT=[
    u'which subject would you want to begin with ?',
    u'you"re enrolled for the following courses, select one'
]

LESSON_SELECT=[
    u'which lesson do you want to study?',
    u'Here are your lessons in school, select one'
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

QUIZ_DESCRIPTION=[
    u'{0} Questions in this quiz with 10 points for each. Ready to begin?'
]

INCORRECT_ANSWER=[
    u'Oh!! Sorry that\'s a wrong answer \n Correct answer is\n  {0}',
    u'Oh!! that\'s a incorrect answer \n Right answer is\n {0}',
    u'Wrong answer! Right answer for previous question is \n  {0}'
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
    u'Sorry, don"t know what {0} is'
]

GENERAL_FALLBACKS=[
    u'<speak>I didn\'t get that. <break time="300ms"/><prosody rate="medium" pitch="-2st">\
      Can you say it again?</prosody></speak>',
    u'<speak>Ohh! I missed what you said.<break time="300ms"/> \
      <prosody rate="medium" pitch="-2st">Say it again?</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/> <prosody rate="medium" pitch="-2st"> could you say that again?</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/>  <prosody rate="medium" pitch="-2st">can you say that again?</prosody></speak>',
    u'<speak><prosody rate="slow" pitch="-2st">Can you say that again?</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/>  <prosody rate="medium" pitch="-2st">I didn\'t get that.</prosody></speak>',
    u'<speak>Sorry, <break time="200ms"/>  <prosody rate="medium" pitch="-2st">what was that?</prosody></speak>',
    u'<speak>One more time?</speak>',
    u'<speak>Say that again?</speak>',
    u'<speak>I didn"t get that.</speak>',
    u'<speak>I missed that.</speak>',
    u'<speak>Couldn"t understand, <break time="200ms"/> try again?</speak>'
]

QUIZ_GOLD_BADGE_TITLE=[
    (
        u'<speak>Wow! you got a gold badge</speak>',
        u'Wow! you got a gold badge'
    ),
     (
        u'<speak>Great! you have got a gold badge</speak>',
        u'Great! you have got a gold badge'
    ),
     (
        u'<speak>Very good, you added a gold badge</speak>',
        u'Very good, you added a gold badge'
    )
]

QUIZ_GOLD_BADGE_DESC=[
        u'You are awesome, you achievd one gold badge in quiz',
        u'Great! you got a gold badge in the quiz',
        u'Awesome got a gold badge for the quiz, keep doing more to get more of such badges'
]

QUIZ_SILVER_BADGE_DESC=[
        u'Here you go... there is a silver badge added to your bucket',
        u'Hey! you got a silver badge for the quiz',
        u'Good you got a silver badge, keep doing more and more and get more such badges'
]

QUIZ_BRONZE_BADGE_DESC=[
        u'You got a bronze for the quiz, you can do better',
        u'Hey! you got a bronze badge for the quiz',
        u'Good you just got a bronze badge, keep doing more and more and get more such badges'
]

QUIZ_SILVER_BADGE_TITLE=[
    (
        u'<speak>Good you got a silver badge</speak>',
        u'Good you got a silver badge'
    ),
     (
        u'<speak>Alright! you have got a silver badge</speak>',
        u'Alright! you have got a silver badge'
    ),
]

QUIZ_BRONZE_BADGE_TITLE=[
    (
        u'<speak>It\'s ok, you got a bronze badge</speak>',
        u'It\'s ok, you got a bronze badge'
    ),
     (
        u'<speak>You have got a bronze badge</speak>',
        u'You have got a bronze badge'
    ),
]

QUIZ_BADGE_TITLE = [
    QUIZ_BRONZE_BADGE_TITLE,
    QUIZ_SILVER_BADGE_TITLE,
    QUIZ_GOLD_BADGE_TITLE
]

QUIZ_BADGE_DESC = [
    QUIZ_BRONZE_BADGE_DESC,
    QUIZ_SILVER_BADGE_DESC,
    QUIZ_GOLD_BADGE_DESC
]

SHIELD_GOLD_BADGE_TITLE=[
    (
        u'<speak>Wow! you got a gold shield</speak>',
        u'Wow! you got a gold shield'
    ),
     (
        u'<speak>Great! you have got a gold shield</speak>',
        u'Great! you have got a gold shield'
    ),
     (
        u'<speak>Very good, you added a gold shield</speak>',
        u'Very good, you added a gold shield'
    )
]

SHIELD_SILVER_BADGE_TITLE=[
    (
        u'<speak>Good you got a silver shield</speak>',
        u'Good you got a silver shield'
    ),
     (
        u'<speak>Alright! you have got a silver shield</speak>',
        u'Alright! you have got a silver shield'
    ),
]

SHIELD_BRONZE_BADGE_TITLE=[
    (
        u'<speak>It\'s ok, you got a bronze shield</speak>',
        u'It\'s ok, you got a bronze shield'
    ),
     (
        u'<speak>You have got a bronze shield</speak>',
        u'You have got a bronze shield'
    ),
]

SHIELD_BADGE_TITLE = {
   'BRONZE' : SHIELD_BRONZE_BADGE_TITLE,
   'SILVER' : SHIELD_SILVER_BADGE_TITLE,
    'GOLD' :  SHIELD_GOLD_BADGE_TITLE
}

SHIELD_BRONZE_BADGE_DESC = [
        u'You have got a bronze shield based on your quiz performances, keep doing more quizes to achieve next level shield',
        u'This bronze shield is for your quiz scores, you can improve by doing more quizes'
]

SHIELD_SILVER_BADGE_DESC = [
        u'Here is your silver shield in the quiz achievement',
        u'This bronze shield is for your quiz scores, you can improve by doing more quizes'
]

SHIELD_GOLD_BADGE_DESC = [
        u'Hey!! Congratulations on the gold shield you achieved, well done',
        u'You are awesome you got a fold sheild, keep it up.'
]

SHIELD_BADGE_DESC = {
   'BRONZE' : SHIELD_BRONZE_BADGE_DESC,
   'SILVER' : SHIELD_SILVER_BADGE_DESC,
    'GOLD' :  SHIELD_GOLD_BADGE_DESC
}

QUIZ_BADGE_TYPE= dict()
QUIZ_BADGE_TYPE[0] = 'BRONZE'
QUIZ_BADGE_TYPE[1] = 'SILVER'
QUIZ_BADGE_TYPE[2] = 'GOLD'
