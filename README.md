TFS.py
======

tfs.py is a python module for interfacing with TFS 2012 via undocumented REST APIs

Features
--------

- Find currently queued builds

Usage
-----
	import tfs

	tfs.TFS_URL = 'https://tfs.mycompany.com/tfs'
	tfs.TFS_TEAM_PROJECT_COLLECTION = 'DefaultCollection'
	tfs.TFS_TEAM_PROJECT = 'Unlimited'
	# If a password is not supplied, the user will be prompted
	builds = tfs.getQueuedBuilds('username','pass')
	for build in builds:
		print "%-20s:%15s" % (build["definition"], build["status"])

Requirements
------------

- python-ntlm