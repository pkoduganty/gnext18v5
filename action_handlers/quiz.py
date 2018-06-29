#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:56:03 2018

@author: praveen
"""
import random
import logging

from action_handlers.session import *
from action_handlers.activity import do_activity

from response_generators.response import *
from response_generators.messages import *

from models.common import *
from models.mock import sample_announcements, sample_homeworks, sample_lessons, sample_courses

def getQuestionById(questions, id):
  filtered = filter(lambda q: q.id == id, questions)  
  if filtered is not None or len(filtered)>0:
    return filtered[0]

def getContexts(session, request):
  contexts=[]
  homeworkId=None
  quizId=None
  shuffled_question_ids=None
  question_index=0
  questionId=None
  
  for context in request.get('queryResult').get('outputContexts'):
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
  
  quiz=None
  if homeworkId is not None and homeworkId: 
    quiz = sample_homeworks.activity_id_dict[quizId] #from homework
  else:
    quiz = sample_lessons.activity_id_dict[quizId] #from lesson

  question=None
  if questionId is not None and shuffled_question_ids is not None:
    question = getQuestionById(quiz.questions, shuffled_question_ids[question_index])  
  
  logging.info('homework - %s, quiz - %s, question - %s, question_index - %d, shuffled questions - %s', homeworkId, quizId, questionId, question_index, str(shuffled_question_ids))
  return (contexts, quiz, question, shuffled_question_ids, question_index)

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
  context = OutputContext(session, OUT_CONTEXT_QUIZ_QUESTION, lifespan=1, shuffled=shuffled_question_ids, question_index=question_index, id=question.id)
  return Response(response_text).text(response_text).card(card).suggestions(question.choices).setOutputContexts(contexts).outputContext(context).build()
  
def answer(session, request):
  contexts, quiz, question, shuffled_question_ids, question_index = getContexts(session, request)        
  
  if quiz is None:
    error_text = 'Error, developer error - quiz not found'  
    return Response(error_text).text(error_text).build()

  query = request.get('queryResult').get('queryText')
  response_text = 'Your response {0}, should be {1}'.format(query, str(question.answers))
  context = OutputContext(session, OUT_CONTEXT_QUIZ_QUESTION, lifespan=1, shuffled=shuffled_question_ids, question_index=question_index, id=question.id)
  return Response(response_text).text(response_text).followupEvent('action_next_question').setOutputContexts(contexts).outputContext(context).build()
  