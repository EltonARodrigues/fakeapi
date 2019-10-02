from flask_restful import Api, Resource, reqparse
from flask import Flask
import os

app = Flask(__name__)
api = Api(app)

id = 40

messages = {
    'messages': [
        {
        "id": 0,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "PRIMEIRA",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/test.ogg",
        "media_id": ""
    },
    {
        "id": 1,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/test.ogg",
        "media_id": ""
    },
    {
        "id": 2,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "texto texto texto texto 1",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
    {
        "id": 3,
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
        "id": 4,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 3",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 5,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "teste 4",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/test.ogg",
        "media_id": ""
    },
        {
        "id": 7,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 4",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 8,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 5",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 9,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 6",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
       {
        "id": 10,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "teste 7",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 11,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "teste 8",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/test.ogg",
        "media_id": ""
    },
            {
        "id": 12,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "FIM",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/test.ogg",
        "media_id": ""
    },
       {
        "id": 15,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "INICIO",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 16,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "test 1",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
        {
        "id": 17,
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
        "id": 18,
        "from": "6666666666666",
        "to": "stet",
        "type": "text",
        "text": "ULTIMA",
        "caption": "",
        "mime": "",
        "file": "",
        "media_id": ""
    },
    {
        "id": 19,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/audio3.ogg",
        "media_id": ""
    },
    {
        "id": 20,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/audio2.ogg",
        "media_id": ""
    },
        {
        "id": 21,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/audio1.ogg",
        "media_id": ""
    },

        {
        "id": 22,
        "from": "5514981007074",
        "to": "stet",
        "type": "text",
        "text": "Texto normal sem ser uma transcrição de audio",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/audio4.ogg",
        "media_id": ""
    },
        {
        "id": 23,
        "from": "5514981007074",
        "to": "stet",
        "type": "audio",
        "text": "",
        "caption": "",
        "mime": "",
        "file": "https://testpurecloudelton.s3.sa-east-1.amazonaws.com/audio4.ogg",
        "media_id": ""
    }
]
}


class Message(Resource):
    def get(self, number):
        response = {'messages': [] }
        if number != 'all':
            for message in messages['messages']:
                if(number == message["from"]):
                    response['messages'].append(message)
            return response, 200
        return messages, 200

    def post(self, number):
        global id
        parser = reqparse.RequestParser()
        parser.add_argument("from")
        parser.add_argument("to")
        parser.add_argument("message")
        args = parser.parse_args()

        id += 1
        message = {
            "id": int(id),
            "from": args['from'],
            "to": args['to'],
            "type": "text",
            "text": args['message'],
            "caption": "",
            "mime": "",
            "file": "",
            "media_id": ""
        }
        messages['messages'].append(message)
        return message, 201

    def delete(self, number):
        global messages
        for i in range(len(messages['messages'])):
            if messages['messages'][i]['id'] == int(number):
                del messages['messages'][i]
                break

        return "{} is deleted.".format(number), 200

api.add_resource(Message, "/message/<string:number>")

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)