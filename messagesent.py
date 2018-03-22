from flask import Flask ,jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient


class MessageSent(Resource):

	def post(self):
		client= MongoClient()
		db= client.devcoders
		messages= db.messages

		username = request.json['uid']
		to = request.json['from']
		message = request.json['message']

		msg={'uid':username, 'from':to, 'message':message}

		messages.insert_one(msg)

		return {'message':'sent'},201

	def get(self):
		client= MongoClient()
		db= client.devcoders
		messages= db.messages

		result = messages.find()

		final = []
		for i in result:
			i.pop('_id')
			final.append(i)

		return {'msgs':final},200