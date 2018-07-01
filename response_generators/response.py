#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 09:23:19 2018

@author: praveen
"""
import json
import logging
logger = logging.getLogger('root')
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)

class ResponseType(object):
  def toJson(self):
    return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=6))
  
class Item(ResponseType):
  def __init__(self, id, title, description='', imageUri=None, imageText=None, synonyms=[]):
    self.title=title
    self.description=description
    if id is not None:
      self.info=SelectItemInfo(id)
      self.info.synonyms=synonyms
    if imageUri is not None:
      self.image={
          "imageUri": imageUri,
          "accessibilityText": imageText if imageText is not None else title
      }
    logging.debug('Created Item %s', str(self.__dict__))
      
class SelectItemInfo(ResponseType):
  def __init__(self, key, synonyms=[]):
    self.key=key
    self.synonyms=synonyms
    logging.debug('Created SelectItemInfo %s', str(self.__dict__))

class Speech(ResponseType):
  def __init__(self, ssml, displayText):
    self.platform="ACTIONS_ON_GOOGLE"
    self.simpleResponses={
          "simpleResponses": [
              {
                  "ssml":ssml,
                  "displayText":displayText
              }
          ]
    }
    logging.debug('Created SelectItemInfo %s', str(self.__dict__))
    
class Text(ResponseType):
  def __init__(self, text):
    self.platform="ACTIONS_ON_GOOGLE"
    self.simpleResponses={
          "simpleResponses": [
              {
                  "textToSpeech":text
              }
          ]
    }
    logging.debug('Created Text %s', str(self.__dict__))

class Button(ResponseType):
  def __init__(self, title, uri):  
    self.title=title
    self.openUriAction={
        "uri": uri
    }
    logging.debug('Created Button %s', str(self.__dict__))
  
class Card(ResponseType):
  def __init__(self, title, description, subtitle=None, imageUri=None, imageText=None, buttons=[]):
    self.title=title
    if subtitle is not None:
      self.subtitle=subtitle
    self.formattedText=description
    if imageUri is not None:
      self.image={
          "imageUri": imageUri,
          "accessibilityText": imageText if imageText is not None else title
      }
    self.buttons=buttons
    logging.debug('Created Card %s', str(self.__dict__))

class RichResponse(ResponseType):
  def __init__(self):
    self.items=[]
    self.suggestions=[]
    logging.debug('Created RichResponse %s', str(self.__dict__))
    
class OutputContext(ResponseType):
  def __init__(self, session, name, lifespan="5", **kwargs):
    self.name="{0}/contexts/{1}".format(session, name)
    self.lifespanCount=lifespan
    self.parameters=kwargs
    logging.debug('Created OutputContext %s', str(self.__dict__))
    
class FollowupEvent(ResponseType):
  def __init__(self, event, parameterDict):
    self.languageCode = 'en'
    self.name = event
    self.parameters = parameterDict
    logging.debug('Created FollowupEvent %s', str(self.__dict__))
    
class Response(ResponseType):
  def __init__(self, text):
    self.outputContexts=[]
    self.fulfillmentText=text
    self.fulfillmentMessages=[]

  def speech(self, ssml, text):
    self.fulfillmentMessages.append(Speech(ssml, text))
    return self
  
  def text(self, text):
    self.fulfillmentMessages.append(Text(text))
    return self
  
  def link(self, title, url):
    response={
        "platform": "ACTIONS_ON_GOOGLE",
        "linkOutSuggestion": {
          "destinationName": title,
          "uri": url
        }
    }
    self.fulfillmentMessages.append(response)
    return self
    
  def card(self, card):
    response={
        "platform": "ACTIONS_ON_GOOGLE",
        "basicCard": card
    }
    self.fulfillmentMessages.append(response)
    return self

  def media(self, media):
    response={"mediaResponse":media}
    self.fulfillmentMessages.append(response)
    return self

  def carousel(self, items):
    response={
        "platform":"ACTIONS_ON_GOOGLE",            
        "carouselSelect": {
            "items":items
        }
    }
    self.fulfillmentMessages.append(response)
    return self
  
  def noInputPrompt(self, prompt):
    if isinstance(prompt, ResponseType):
      self.payload.google.noInputPrompts.append(prompt)
    else:
      self.payload.google.noInputPrompts.append(Text(prompt))
    return self
  
  def expectNoResponse(self):
    self.payload.google.expectUserResponse=False
    return self

  def suggestions(self, text_list):
    suggestion_list=[]
    for s in text_list:
      suggestion_list.append({"title":s})

    response={
        "platform":"ACTIONS_ON_GOOGLE",
        "suggestions": {
            "suggestions": suggestion_list
        }
    }
    self.fulfillmentMessages.append(response)
    return self
  
  def select(self, title, items):
    response={
        "platform":"ACTIONS_ON_GOOGLE",
        "listSelect": {
            "title":title, 
            "items":items
        }
    }
    self.fulfillmentMessages.append(response)
    return self

  def outputContext(self, context):
    self.outputContexts.append(context)
    return self
  
  def setOutputContexts(self, contextsList):
    self.outputContexts=contextsList
    return self
  
  def followupEvent(self, event, **kwargs):
    self.__dict__["followupEventInput"]=FollowupEvent(event, kwargs)
    return self
  
  def userStorage(self, obj):
    self.__dict__["userStorage"]=json.dumps(obj)
    return self
  
  def resetUserStorage(self):
    self.__dict__["resetUserStorage"]=True
    return self
  
  def permissions(self, permits):
    self.followupEvent('actions_intent_PERMISSION', PERMISSION=permits)
  
  def build(self):
    logging.info(self.toJson())
    return self.toJson()
