#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json
import random as rd
from html import unescape
# =============================================================================
# Functions that send requests to rest.py
# =============================================================================
def get_trivia_question():
	resp = requests.get('http://localhost:8888/OpenTriviaDB')
	return resp.json()

def get_questions():
	# get all questions from API
	resp = requests.get('http://localhost:8888/Questions')
	return resp.json()

def get_question_entry(idx: int):
	#  request single entry
	resp = requests.get(f'http://localhost:8888/Questions/{idx}')
	return resp.json()

def put_question(text: str, answer: str):
    # PUT request to add questions
    # rest.py expects json data
    resp = requests.put('http://localhost:8888/Questions', json={'text':text,
                                                                'answer':answer})
    return resp.json()

def post_question(idx: int, text: str, answer: str):
        # PUT request to add questions
        # rest.py expects json data
    resp = requests.post(f'http://localhost:8888/Questions/{idx}', json={'text':text,
                                                                'answer':answer})
    return resp.json()

# =============================================================================
# Functions controlling the Quiz
# =============================================================================
def print_menu():
    print('0: Open Trivia API Quiz\n'+
        '1: Start Quiz\n'+
        '2: Add Question\n'+
        '3: View Questions\n'+
        '4: Edit Question\n'+ 
        'STOP: Leave Quiz\n')

def start_quiz():
    quiz = get_questions()
    print(f'\n{len(quiz)} Questions to be posed!')
    for question in quiz:
        for _try in range(3,0,-1):
            print(question['text']+'\n',
                  f'{_try}',' tries left' if _try>1 else  'try left')
            inp = input('[YOU]: ')
            if inp==question['answer']:
                print('correct!')
                break
            else:
                print('Not correct!')
            print('\n')
    print('\nQuiz finished!')

def add_question():
    text = input('Enter text: ')
    answer = input('Enter answer: ')
    quiz = put_question(text, answer)
    print('\nQuestions:\n')
    for q in quiz:
        print(q)
    print('\n')

def show_questions():
    quiz = get_questions()
    print('\nQuestions:\n')
    for q in quiz:
        print(q)
    print('\n')

def edit_question():
    idx = int(input('Enter index of element starting by 0: '))
    text = input('Enter text: ')
    answer = input('Enter answer: ')
    q = post_question(idx, text, answer)
    print('\nQuestion:\n')
    print(q)
    print('\n')

def start_trivia_quiz():
    for rnd in range(1,6):
        question = get_trivia_question()
        print(f'Question {rnd} of 6: ')
        print(unescape(question['question']))
        options = question['incorrect_answers'] + [question['correct_answer']]
        rd.shuffle(options)
        for opt in options:
            print(opt)
        inp = input('[YOU]: ')
        print(inp == question['correct_answer'], '\nCorrect answer is:' ,question['correct_answer'])

def main():
    while True:
        print_menu()
        inp = input('[YOU]: ')
        if inp == '0':
            start_trivia_quiz()
        if inp == '1':
            start_quiz()
        if inp == '2':
            add_question()
        if inp == '3':
            show_questions()
        if inp == '4':
            edit_question()
        if inp == 'STOP' or inp == 'stop':
            break
    print('closing...')

if __name__=='__main__':
	main()

