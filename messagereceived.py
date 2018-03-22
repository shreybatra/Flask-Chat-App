from flask import Flask ,jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient


class MessageReceived(Resource):

	def post(self):
		client= MongoClient()
		db= client.devcoders
		messages= db.messages

		uid= request.json['uid']
		result = messages.find({'uid': uid},{'from':1, 'message':1})

		final = []
		for i in result:
			i.pop('_id')
			final.append(i)

		#res=  messages.delete_many(result)	
		return {'msgs':final},200

	