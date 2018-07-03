#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from action_handlers.session import *
from action_handlers.activity import do_activity

from response_generators.response import *
from response_generators.messages import *

from models.common import *
from models.mock import sample_announcements, sample_homeworks, sample_lessons, sample_courses


def list_all(session, request):
  subject = request.get('queryResult').get('parameters').get('subject')
  grade = request.get('queryResult').get('parameters').get('grade') #TODO use students current grade
  grade = grade if grade is not None else 8
  
  logging.info('subject=%s, grade=%d', subject, grade)
  if subject is None:
    error_text = 'Error, course not found'
    return Response(error_text).text(error_text).build()
  else:
    select_cards=[]
    quizzes=[]
    for homework in sample_homeworks.activities:
      course=sample_courses.courses_id_dict[homework.courseId]
      if (grade==course.grade and subject==course.subject and isinstance(homework.activity, Quiz)):
        logging.info('activity id=%s, title=%s', homework.activity.id, homework.activity.title)
        card=Item('activity '+homework.activity.id, homework.activity.title)
        select_cards.append(card)
        quizzes.append(homework.activity)
    
    if len(quizzes)==1:
      return do_activity(session, quizzes[0]).build()
    elif len(quizzes)>1:
      response_text = random.choice(QUIZ_SELECT)
      context = OutputContext(session, OUT_CONTEXT_QUIZ, type=OUT_CONTEXT_QUIZ)
      return Response(response_text).text(response_text).select(response_text, select_cards).outputContext(context).build()
  
  response_text='No quizzes'
  return Response(response_text).text(response_text).build()


def start(session, request):
  contexts, quiz, question, shuffled_question_ids, question_index = getContexts(session, request)        
  
  if quiz is None:
    error_text = 'Error, quiz not found'  
    return Response(error_text).text(error_text).build()
        
  description='{0} Questions in this quiz, each for 1 point. Ready to begin?'.format(len(quiz.questions))
  card = Card(quiz.title, description=description)
  response_text = quiz.title
  context = OutputContext(session, OUT_CONTEXT_QUIZ_DO, type=OUT_CONTEXT_QUIZ_DO, lifespan=2, id=quiz.id)
  return Response(response_text).text(description).card(card).suggestions(['Yes','No']).setOutputContexts(contexts).outputContext(context).build()


def start_yes(session, request):
  contexts, quiz, question, shuffled_question_ids, question_index = getContexts(session, request)
  
  if quiz is None:
    error_text = 'Error, developer error - quiz not found'  
    return Response(error_text).text(error_text).build()
    
  random.shuffle(quiz.questions)
  shuffled_question_ids = [q.id for q in quiz.questions]
  logging.info('shuffled questions - %s', str(shuffled_question_ids)) 
  question_index = 0

  question = quiz.questions[question_index]
  title = 'Question {0} of {1}'.format(question_index+1, len(shuffled_question_ids))
  
  card = Card(title, question.question)
  response_text = title +' :' + question.question
  context = OutputContext(session, OUT_CONTEXT_QUIZ_QUESTION, lifespan=1, 
                          shuffled=shuffled_question_ids, question_index=question_index, 
                          id=question.id)
  return Response(response_text).text(response_text).card(card).suggestions(question.choices).setOutputContexts(contexts).outputContext(context).build()
  

def answer(session, request):
  contexts, quiz, question, shuffled_question_ids, question_index = getContexts(session, request)
  
  if quiz is None:
    error_text = 'Error, developer error - quiz not found'  
    return Response(error_text).text(error_text).build()

  query = request.get('queryResult').get('queryText')
  
  score_cutoff = 95
  result = process.extractOne(query, question.answers, score_cutoff=score_cutoff, scorer=fuzz.token_set_ratio)
  
  
  if result is not None:
    response_text = 'Right answer {0}'.format(query)
  else:
    response_text = 'Your response {0}, should be {1}'.format(query, str(question.answers))
  
  context = OutputContext(session, OUT_CONTEXT_QUIZ_QUESTION, lifespan=1, 
                          shuffled=shuffled_question_ids, question_index=int(question_index), 
                          id=question.id, answer=query, isCorrect=(result is not None))
  return Response(response_text).text(response_text).followupEvent(EVENT_NEXT_QUESTION).setOutputContexts(contexts).outputContext(context).build()
  

def next_question(session, request):
  contexts, quiz, question, shuffled_question_ids, question_index = getContexts(session, request)
  
  if quiz is None:
    error_text = 'Error, developer error - quiz not found'  
    return Response(error_text).text(error_text).build()

  query = request.get('queryResult').get('queryText')
  if query == EVENT_NEXT_QUESTION:
    logging.debug('answered question {0} - {1}', question.id, question.question)
  else:
    logging.debug('skipped question {0} - {1}', question.id, question.question)

  result = getPrevQuestionResult(contexts, quiz)
  if result is None:
    error='Error, developer error - previous question context not found'
    return Response(error).text(error).build()
  
  questionId, question, student_answer, isCorrect, totalCorrect = result 
  prev_question_result=''
  if bool(isCorrect):
    prev_question_result=random.choice(CORRECT_ANSWER).format(question.question, question.answers[0])
    totalCorrect += 1 #TODO have question specific points
  else:
    prev_question_result=random.choice(INCORRECT_ANSWER).format(question.question, question.answers[0])
  
  question_index += 1 #next question
  if question_index >= len(quiz.questions):
    logging.debug('quiz end, printing report')          
    return Response('Quiz Completed').resetContexts().text(prev_question_result).text(random.choice(QUIZ_REPORT).format(totalCorrect, len(quiz.questions))).suggestions(WELCOME_SUGGESTIONS).build()
  else: 
    question = quiz.questions[question_index]
    logging.debug('display new question {0} - {1}', question.id, question.question)
    title = 'Question {0} of {1}'.format(question_index+1, len(shuffled_question_ids))
  
    card = Card(title, question.question)
    response_text = title +' : \n' + question.question
    context = OutputContext(session, OUT_CONTEXT_QUIZ_QUESTION, lifespan=1, 
                          shuffled=shuffled_question_ids, question_index=question_index, 
                          id=question.id)
    return Response(response_text).text(prev_question_result).card(card).suggestions(question.choices).setOutputContexts(contexts).outputContext(context).build()

def getPrevQuestionResult(contexts, quiz):
  for context in contexts:
    if str(context.name).endswith(OUT_CONTEXT_QUIZ_QUESTION):
      questionId=context.parameters.get('id')
      question=getQuestionById(quiz.questions, questionId)
      student_answer=context.parameters.get('answer')
      isCorrect=context.parameters.get('isCorrect')
      totalCorrect=context.parameters.get('totalCorrect')
      
      logging.debug('Question: {0}, response: {1}, answer:{2}, isCorrect={3}, totalCorrect={4}'.format(question.question, student_answer, str(question.answers), isCorrect, totalCorrect))      
      return (questionId, question, student_answer, isCorrect, totalCorrect)
  return None


def getQuestionById(questions, id):
  filtered = filter(lambda q: q.id == id, questions)  
  if filtered is not None or len(filtered)>0:
    return filtered[0]


def getContexts(session, request):
  contexts=[]
  quizId=None
  shuffled_question_ids=None
  question_index=0
  questionId=None
  
  for context in request.get('queryResult').get('outputContexts'):
    logging.debug('context: {0}, parameters: {1}', context.get('name'), str(context.get('parameters')))
    if context.get('name').endswith(OUT_CONTEXT_DO_HOMEWORK):
      homeworkId=context.get('parameters').get('id')
      contexts.append(OutputContext(session,OUT_CONTEXT_DO_HOMEWORK, lifespan=2, type=OUT_CONTEXT_DO_HOMEWORK, id=homeworkId))
    elif context.get('name').endswith(OUT_CONTEXT_LESSON_ACTIVITY_DO):
      quizId=context.get('parameters').get('id')
      contexts.append(OutputContext(session,OUT_CONTEXT_LESSON_ACTIVITY_DO, lifespan=2, type=OUT_CONTEXT_LESSON_ACTIVITY_DO, id=quizId))
    elif context.get('name').endswith(OUT_CONTEXT_QUIZ_QUESTION):
      questionId=context.get('parameters').get('id')
      shuffled_question_ids=context.get('parameters').get('shuffled')
      question_index=context.get('parameters').get('question_index')
      question_index=int(question_index) if question_index is not None else 0

  if quizId is None or not quizId.strip():
    return (contexts, None, None, None, 0)
  
  quiz = sample_homeworks.activity_id_dict.get(quizId) #from homework
  if quiz is None:
    quiz = sample_lessons.activity_id_dict.get(quizId) #from lesson

  if quiz is None:
    return (contexts, None, None, None, 0)

  question=None
  if questionId is not None and shuffled_question_ids is not None:
    question = getQuestionById(quiz.questions, shuffled_question_ids[question_index])  
  
  logging.info('quiz - %s, question - %s, question_index - %d, shuffled questions - %s', quizId, questionId, question_index, str(shuffled_question_ids))
  return (contexts, quiz, question, shuffled_question_ids, question_index)