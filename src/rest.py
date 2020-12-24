#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request

import requests
import random as rd
app = Flask(__name__)
app.config["DEBUG"] = True

questions = [{'text': 'What equals 4x4?',
        'answer': '16'}]
questions_api = list()

def init():
    resp = requests.get('https://opentdb.com/api.php?amount=10')
    questions_api.extend(resp.json()['results'])

# Handle PUT and GET for all questions
@app.route('/Questions', methods=['PUT', 'GET'])
def get_put_question():
    if request.method=='GET':
        return jsonify(questions)
    if request.method=='PUT':
        text = request.json['text']
        answer = request.json['answer']
        questions.append({'text': text,
                'answer': answer})
        return jsonify(questions)

# Handle POST and GET for entry
@app.route('/Questions/<int:id>', methods=['POST', 'GET'])
def get_post_question_entry(id):
    if id>len(questions)-1: # return last entry if id is out of range
        id = len(questions)-1
    if request.method=='GET':
        return jsonify(questions[id])
    if request.method=='POST':
        text = request.json['text']
        answer = request.json['answer']
        questions[id] = {'text': text,'answer': answer}
        return jsonify(questions[id])

@app.route('/OpenTriviaDB', methods=['GET'])
def get_trivia_question():
    ''' pick random question'''
    return jsonify(rd.choice(questions_api))
if __name__=='__main__':
    init()
    app.run(port=8888, threaded=True)

# curl -X PUT -H "Content-Type: application/json" -d '{"text": "How long is a day in hours", "answer": "24"}' localhost:8888/Questions
# curl localhost:8888/Questions/0
# curl localhost:8888/Questions/
