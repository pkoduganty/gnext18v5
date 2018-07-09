#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 00:35:02 2018

@author: praveen
"""

# -*- coding: utf-8 -*-
import os
import sys
import json
import importlib
import logging

from response_generators import response

from flask import Flask, jsonify, session, request, render_template

app = Flask(__name__, static_url_path='', static_folder='web/static')
app.secret_key = r'Dronacharya, the great royal teacher from mahabharata'

root = logging.getLogger()
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

@app.route('/auth', methods=['GET','POST'])
def auth():
  return render_template('index.htm')

@app.route('/privacy')
def privacy_policy():
  return render_template('privacy.htm')

@app.route('/', methods=['POST'])
def webhook():
  # Get request parameters
  req = request.get_json(force=True)
  logging.info('request = %s', json.dumps(req))
  
  sessionId = req.get('session')
  intent = req.get('queryResult').get('intent')
  intent_name = intent.get('displayName') if intent is not None else None
  action = req.get('queryResult').get('action')
  slots_filled = req.get('queryResult').get('allRequiredParamsPresent')
  
  logging.info('invoking action handler for intent %s, action %s', intent, action)
  
  try:
    if intent_name.find('.')>0:
      action=intent_name
      
    handler, method = action.rsplit('.',1)
    
    if not slots_filled:
      method = 'slot_filler'
      
    action_handler = importlib.import_module('action_handlers.' + handler)
    func = getattr(action_handler, method)
    
    res = func(sessionId, req) # ex. call action_handler.courses.list
  except ImportError:
    logging.error('Unexpected intent: %s for request: %s', action, json.dumps(req))
    logging.exception('Import Error')
    
    res = response.Response('Error').text('Unexpected intent: ' + action).build()
  except:
    logging.exception('Error')
    raise
  
  logging.info('Response: \n %s', str(res))
  return jsonify(res)

@app.route('/play/<path:fileName>')
def sound(fileName):
  return app.send_static_file(fileName)

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
  """Return a custom 404 error."""
  return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
  """Return a custom 500 error."""
  return 'Sorry, unexpected error: {}'.format(e), 500

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification.
  # ACTION ITEM for developers:
  #     When running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  # Specify a hostname and port that are set as a valid redirect URI
  # for your API project in the Google API Console.
  app.run('localhost', 8080, debug=True)
