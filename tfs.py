#!/usr/bin/env python
import urllib2
import getpass
from ntlm import HTTPNtlmAuthHandler
import simplejson as json

TFS_URL = "" # Your TFS URL e.x. https://tfs.yourCompany.com
TFS_TEAM_PROJECT_COLLECTION = "" # Your TFS Collection e.g. DefaultCollection
TFS_TEAM_PROJECT = "" # Your TFS Project e.g. Products

apiForQueuedBuilds = '_api/_build/queuedBuilds'

def getAuthNTLM(url, username, password=''):
  if password == '':
    password = getpass.getpass("Please enter your password: ")

  passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
  passman.add_password(None, url, username, password)
  return HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

def getResponse(url, auth):
  # create and install the opener
  opener = urllib2.build_opener(auth)
  urllib2.install_opener(opener)

  # retrieve the result
  response = urllib2.urlopen(url)
  jsonResponse = json.loads(response.read())
  return jsonResponse["__wrappedArray"]

def getFullTFSURL():
  return '/'.join([TFS_URL,TFS_TEAM_PROJECT_COLLECTION,TFS_TEAM_PROJECT])

def getQueuedBuilds(username, password=''):
  fullQueuedBuildsAPI = '/'.join([getFullTFSURL(), apiForQueuedBuilds])
  fullQueuedBuildsAPI += "?__v=1&status=63"

  auth = getAuthNTLM(fullQueuedBuildsAPI, username, password)
  builds = getResponse(fullQueuedBuildsAPI, auth)

  return builds
