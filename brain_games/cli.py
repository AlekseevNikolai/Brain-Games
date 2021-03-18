import prompt

def welcome_user():
    print('Welocme to the Brain Games')
    name = prompt.string('May I have your name? ')
    print('Hello {}'.format(name))