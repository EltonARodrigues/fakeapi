from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

messages = [
    {
        "id": 1,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 1",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
    {
        "id": 2,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "teste 1",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 3,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "teste 2",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 4,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 2",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 5,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "teste 3",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 6,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "teste 4",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 7,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "teste 5",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 8,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "teste 6",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    }
]


class Message(Resource):
    def get(self, number):
        response = []
        if number != 'all':
            for message in messages:
                if(number == message["from"]):
                    response.append(message)
            return response, 200
        return messages, 200

    def post(self, number):
        parser = reqparse.RequestParser()
        parser.add_argument("from")
        parser.add_argument("to")
        parser.add_argument("message")
        args = parser.parse_args()

        for message in messages:
            if(number    == message["id"]):
                return "User with name {} already exists".format(name), 400
        message = {
            "id": int(number),
            "from": args['from'],
            "to": args['to'],
            "type": "text",
            "text": args['message'],
            "caption": "",
            "mime": "",
            "file": "",
            "media_id": ""
        }
        messages.append(message)
        return message, 201

    def delete(self, number):
        global messages
        messages = [message for message in messages if message["id"] != int(number)]
        print(messages)
        return "{} is deleted.".format(number), 200

api.add_resource(Message, "/message/<string:number>")

app.run(debug=True)