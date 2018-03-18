# Basic import for game
from sys import exit
from random import randint
from textwrap import dedent # This allows for """Text""

# The play is in a Game Show
# (S)he needs to answer a list of QUESTIONS
# (S)he also needs to guess a CODE correctly to receive a GRAND PRICE

class GameShow(object):
    def enter(self):
        exit(1)

class Engine(object):
    def __init__(self, gameshow_map):
        self.gameshow_map = gameshow_map
    
    def play(self):
        current_question = self.gameshow_map.opening_question()
        last_question = self.gameshow_map.next_question('grand_price')
    
        while current_question != last_question:
            next_question_name = current_question.enter()
            current_question = self.gameshow_map.next_question(next_question_name)

        current_question.enter()

class Death(GameShow):
    die_reason = [
        "You died.",
        "You should know this easily ... But you died!"
        "You should eat more chocolate ... then you'll know the answer!"
        "LOSE!"
        "See you next time!"
    ]

    def enter(self):
        print(Death.die_reason[randint(0, len(self.die_reason)-1)])
        exit(1)

class Question1(GameShow):
    def enter(self):
        print(dedent("""
        This is Game Show, you are to answer a list of QUESTIONS
        and finally guess a 3-digit CODE to win the GRAND PRICE
        """))

        print("Who owns the largest chocolate factory in the World?")

        answer = input("Answer >> ").lower()

        if answer == "Willy Wonka".lower():
            print("Correct!")
            return 'question_2'
        else:
            return 'death'

class Question2(GameShow):
    def enter(self):
        print("\nWhat takes you to his factory?")

        answer = input("Answer >> ").lower()

        if answer == "Golden Ticket".lower():
            print("Correct!")
            return 'question_3'
        else:
            return 'death'

class Question3(GameShow):
    def enter(self):
        print("\nWho is the main character in this movie?")

        answer = input("Answer >> ").lower()

        if answer == "Charlie".lower():
            print("Correct!")
            return 'question_4'
        else:
            return 'death'

class Question4(GameShow):
    def enter(self):
        print("\nWhere did he find the Gold Ticket?")

        answer = input("Answer >> ").lower()

        if answer == "Inside Wrapper".lower():
            print("Correct!")
            return 'code'
        elif answer == "Convinent Store".lower():
            print("Nice try ... but try again!")
            return 'question_4'
        else:
            return 'death'

class Code(GameShow):
    def enter(self):
        print(dedent("""
        Nice job!
        You completed all the question correctly.
        Now, to win the grand price, you need some LUCK!
        You are to enter a 3-digit code correctly.
        You have 5 attempts.
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print("The Code:" , code)
        guess = input("Gues the code >> ")
        guesses = 0

        while guess != code and guesses < 6:
            print("BZZZEDDD!")
            print("Try again!")
            guesses += 1
            guess = input("Gues the code >> ")
        
        if guess == code:
            print("\nCongratulation! YOU WIN!!!")
            return 'grand_price'
        else:
            return 'death'

class GrandPrice(GameShow):
    def enter(self):
        print("\nYour Grand Price: -- 1-year unlimitted chocolate from Willy Wonka! --\n")
        return 'grand_price'

class Map(object):
    gameshow = {
        'question_1': Question1(),
        'question_2': Question2(),
        'question_3': Question3(),
        'question_4': Question4(),
        'code': Code(),
        'grand_price': GrandPrice(),
    }

    def __init__(self, start_question):
        self.start_question = start_question
    
    def next_question(self, question_name):
        val = Map.gameshow.get(question_name)
        return val
    
    def opening_question(self):
        return self.next_question(self.start_question)

a_map = Map('question_1')
a_game = Engine(a_map)
a_game.play()