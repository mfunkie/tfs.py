#!/usr/bin/env python
import requests
from requests_ntlm import HttpNtlmAuth
import simplejson as json
import getpass

TFS_URL = "" # Your TFS URL e.x. https://tfs.yourCompany.com
TFS_TEAM_PROJECT_COLLECTION = "" # Your TFS Collection e.g. DefaultCollection
TFS_TEAM_PROJECT = "" # Your TFS Project e.g. Products

apiForQueuedBuilds = '_api/_build/queuedBuilds'

def getResponse(url, username, password):
  response = requests.get(url, auth=HttpNtlmAuth(username, password))
  jsonResponse = json.loads(response.text)
  return jsonResponse["__wrappedArray"]

def getFullTFSURL():
  return '/'.join([TFS_URL,TFS_TEAM_PROJECT_COLLECTION,TFS_TEAM_PROJECT])

def getQueuedBuilds(username, password=''):
  fullQueuedBuildsAPI = '/'.join([getFullTFSURL(), apiForQueuedBuilds])
  fullQueuedBuildsAPI += "?__v=1&status=63"
  
  if password == '':
    password = getpass.getpass("Please enter your password: ")

  builds = getResponse(fullQueuedBuildsAPI, username, password)

  return builds
