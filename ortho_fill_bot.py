# -*- coding: utf-8 -*-

#TODO Oauth2
#TODO Icon for bot

'''
Notes
http://www.datamuse.com/api/

'''
from __future__ import print_function
import praw
from json import load as jload, loads as jloads
from getpass import getpass
from requests import auth as rauth, post as  rpost

class OrthoFillBot:
	def __init__(self, testing=False):
		
		with open('config.json', 'r') as f:
			self.data = jload(f)

		while True:
			self.password = getpass(prompt='Enter password: ')			
			if self.auth():
				break
			else:
				print ('Error: Login failed')

		if testing:
			self.base_url='reddit.local'
			self.oauth_url='reddit.local'
		else:
			self.base_url='www.reddit.com'
			self.oauth_url='oauth.reddit.com'
		
		
	def auth(self):
		client_auth = rauth.HTTPBasicAuth(self.data['id'], self.data['secret'])
		post_data = {"grant_type": "password", "username": self.data['username'], "password": self.password}
		headers = {"User-Agent": "Ortho Fill Bot by ortho-fill-bot"}
		self.auth_response = rpost("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
		response = jloads(self.auth_response.content)
		if 'access_token' in response:
			self.access_token = response['access_token']
			return True
		else:
			return False
	
	def find_ortho(self):
		
		pass

	def 	
	
if __name__=='__main__':
	bot = OrthoFillBot()
	
