'''
First Python HW:
The first task is a small game - generating a random string filled with
 random numbers and a TREASURE word within the numbers.
 The user will need to seek for the TREASURE word.
 The code creates and writes to a file the game text, and reads back
 from the file.
'''
import random
import os
from io import TextIOWrapper

FORWARD = 1
BACKWARD = 2
MAX_RANDOM_REPEAT = 20
MIN_RANDOM_REPEAT = 1
GAME_TEXT = "TREASURE"
HIGHSCORE_FILE = "highscore.txt"

def read_from_highscore_file(file:TextIOWrapper):
    highscore_list = []
    for line in file:
        read = line.split("\t")
        score = int(read[0])
        name = read[1]
        highscore_list.append((score, name))
    return highscore_list

def check_position(score, highscores):
    for n in range(len(highscores)):
        if score < highscores[n][0]:
            return n
    return len(highscores)


def insert_highscore(score, highscores):
    player_name = input("You got a new highscore!\nPlease enter your name: ")
    high_score_position = check_position(score, highscores)
    highscores.insert(high_score_position, (score, player_name))
    if len(highscores) > 10:
        highscores.pop()
    with open(HIGHSCORE_FILE, "w") as file:
        for item in highscores:
            file.write(str(item[0]) + "\t" + str(item[1]) + "\n")

def check_highscore(score):
    if not os.path.exists(HIGHSCORE_FILE):
        open(HIGHSCORE_FILE, "w").close()
    with open(HIGHSCORE_FILE, "r") as file:
        highscores = read_from_highscore_file(file)
        if len(highscores) < 10:
            insert_highscore(score, highscores)
        else:
            if score < highscores[-1][0]:
                insert_highscore(score, highscores)


def create_file(file_name, text):
    '''
    A function which creates a text file and writes it to it the text it got.
    :param file_name: the name of the file to create.
    :param text: the text to write.
    :return: None.
    '''
    with open(file_name, "w") as file:
        file.write(text)

def read_file_line(file_name):
    '''
    A function which reads a line from the text file and returns it.
    :param file_name: The name of the file to read.
    :return: One line from the file as String.
    '''
    with open(file_name, "r") as file:
        return file.readline()

def create_text():
    '''
    This function generates a new string according to the game rules:
    A sequence of digits from 0 to 9. Each digit appears a random number of times (1-20 times).
    After the last digit 9, write the word TREASURE.
    Then, write the digits again in descending order (from 9 to 0),
    each appearing a random number of times (1-20 times).
    :return:
    the game string
    '''
    game_text = ""
    for i in range(0, 10):
        random_times = random.randint(MIN_RANDOM_REPEAT, MAX_RANDOM_REPEAT)
        game_text += str(i) * random_times
    game_text = game_text + GAME_TEXT
    for i in range(9, -1, -1):
        random_times = random.randint(MIN_RANDOM_REPEAT, MAX_RANDOM_REPEAT)
        game_text += str(i) * random_times
    return game_text

def check_winning_condition(goal, cursor_position):
    '''
    This function checks if the player's cursor is between the Treasure word's characters
    :param goal: The position of the starting indice of the Treasure within the game text
    :param cursor_position: The current cursor position within the game text.
    :return: True if the cursor hits any of the Characters in the "TREASURE" word, False otherwise.
    '''
    return goal <= cursor_position <= goal + len(GAME_TEXT) - 1

def game_handler(game_text):
    '''
    This function handles the game according to the game rules
    :param game_text: The game text.
    :return: None.
    '''
    goal = game_text.find(GAME_TEXT)
    is_win = False
    total_moves = 0
    cursor_position = 0
    while not is_win:

        movement_direction = int(input("Where do you want to move? [1- Forward 2- Backwards]:\n"))
        while movement_direction != FORWARD and movement_direction != BACKWARD:
            movement_direction = int(input("Input error!\nWhere do you want to move? [1- Forward 2- Backwards]:\n"))
        print(f"Your current cursor position is {cursor_position}")
        movement_step = int(input("How many characters do you want to move?"))
        cursor_position = cursor_position + movement_step if movement_direction == 1 else cursor_position - movement_step
        if cursor_position >= len(game_text):
            cursor_position = cursor_position % len(game_text)
            print("Since you entered a number higher than the length of the game text, you have been automatically wrapped around to the start position.")
        if cursor_position < 0:
            print("You hit a negative number. The cursor has been reset to the start position.")
            cursor_position = 0
        print(f"You hit \"{game_text[cursor_position]}\"")
        total_moves = total_moves + 1
        if check_winning_condition(goal, cursor_position):
            is_win = True
        else:
            print(f"Try again until you hit the {GAME_TEXT}")

    print(f"Congratulations, you hit the treasure!\nIt took you {total_moves} moves.")
    check_highscore(total_moves)

create_file("treasure.txt", create_text())
game_text = read_file_line("treasure.txt")
print(game_text)
game_handler(game_text)



