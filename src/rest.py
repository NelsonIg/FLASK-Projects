#!/usr/bin/env python3

from flask import Flask, jsonify, request
app = Flask(__name__)
app.config["DEBUG"] = True

questions = [{'text': 'What equals 4x4?',
		'answer': '16'}]

@app.route('/Questions', methods=['PUT', 'GET'])
def get_questions():
	if request.method=='GET':
		return jsonify(questions)
	if request.method=='PUT':
		text = request.json['text']
		answer = request.json['answer']
		questions.append({'text': text,
				'answer': answer})
		return jsonify(questions)

@app.route('/Questions/<int:id>', methods=['GET'])
def get_question_entry(id):
	if id>len(questions)-1:
		return 'Entry not Found/n'
	return jsonify(questions[id])

#@route('/Questions/<int:id>', methods=['GET'])

if __name__=='__main__':
	app.run(port=8888)

# curl -X PUT -H "Content-Type: application/json" -d '{"text": "How long is a day in hours", "answer": "24"}' localhost:8888/Questions
# curl localhost:8888/Questions/0
# curl localhost:8888/Questions/
