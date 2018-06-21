#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 09:23:19 2018

@author: praveen
"""
import json
import logging


class ResponseType(object):
  def toJson(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4))
  
class Item(ResponseType):
  def __init__(self, id, title, description='', imageUri=None, imageText='', synonyms=[]):
    self.title=title
    self.description=description
    if id is not None:
      self.info=SelectItemInfo(id)
      self.info.synonyms=synonyms
    if imageUri is not None:
      self.image={"imageUri":imageUri, "accessibilityText": imageText}

class SelectItemInfo(ResponseType):
  def __init__(self, key, synonyms=[]):
    self.key=key
    self.synonyms=synonyms
    
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

class Button(ResponseType):
  def __init__(self, title, uri):  
    self.title=title
    self.openUriAction={
        "uri": uri
    }
  
class Card(ResponseType):
  def __init__(self, title, description, subtitle=None, imageUri=None, imageText='', buttons=[]):
    self.title=title
    if subtitle is not None:
      self.subtitle=subtitle
    self.formattedText=description
    if imageUri is not None:
      self.image={
          "imageUri": imageUri,
          "accessibilityText": imageText
      }
    self.buttons=buttons    

class RichResponse(ResponseType):
  def __init__(self):
    self.items=[]
    self.suggestions=[]
    
class OutputContext(ResponseType):
  def __init__(self, session, name, lifespan="5", **kwargs):
    self.name="{0}/contexts/{1}".format(session, name)
    self.lifespanCount=lifespan
    self.parameters=kwargs
    
class FollowupIntent(ResponseType):
  def __init__(self, intent, parameterDict):
    self.languageCode = 'en'
    self.name = intent
    self.parameters = parameterDict
    
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
  
  def followupIntent(self, intent, **kwargs):
    self.__dict__["followupEventInput"]=FollowupIntent(intent, kwargs)
    return self
  
  def userStorage(self, obj):
    self.__dict__["userStorage"]=json.dumps(obj)
    return self
  
  def resetUserStorage(self):
    self.__dict__["resetUserStorage"]=True
    return self
  
  def build(self):
    logging.info(self.toJson())
    return self.toJson()
