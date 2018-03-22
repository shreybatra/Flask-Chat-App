from flask import Flask, jsonify
from flask_restful import Api, Resource
from messagereceived import MessageReceived
from messagesent import MessageSent

app=Flask(__name__)
api = Api(app)

api.add_resource(MessageReceived, '/msgrec', endpoint='msgrec')
api.add_resource(MessageSent, '/msgsent', endpoint='msgsent')


if __name__ == '__main__':
	app.run(port=5000, use_reloader=True)