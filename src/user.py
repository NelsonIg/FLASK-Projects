#!/usr/bin/env python3
import requests, json


def get_questions():
	# get all questions from API
	resp = requests.get('http://localhost:8888/Questions')
	return resp.json()

def get_question_entry(id: int):
	#  request single entry
	resp = requests.get(f'http://localhost:8888/Questions/{id}')
	return resp.json()

def add_question(text: str, answer: str):
    # PUT request to add questions
    resp = requests.put('http://localhost:8888/Questions', data={'text': text,
                                                                'answer': answer})
    return resp.json()

def main():
    while True:
        inp = input('1: get_questions()\n'+
                '2: get_question_entry(id)\n'+
                '3: add_question(text, answer\n)'+
                'STOP: Close program\n')
        if inp == '1':
            print(get_questions())
        if inp == '2':
            id = int(input('Enter id for element starting by 0: '))
            print(get_question_entry(id))
        if inp == '3':
            text = input('Enter text: ')
            answer = input('Enter answer: ')
            print(add_question(text, answer))
        if inp == 'STOP' or inp == 'stop':
            break
    print('closing...')

if __name__=='__main__':
	main()

