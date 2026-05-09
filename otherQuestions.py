'''
First Python HW:
The 2nd part of the HW covers file handling, deep understanding of strings in python and
the difference between Sets, Lists and Dictionaries.
The code lists all mandatory questions 2-5 and the optional question number 6.
'''

import random
import os

LOWEST_NUM = 1
HIGHEST_NUM = 1000

def GetFileSize (filename):
    '''
    A function that is called GetFileSize that receives a string representing a filename
    :param filename: the file name to check its size
    :return:
    returns the file size
    '''
    try:
        return os.path.getsize(filename)
    except FileNotFoundError:
        print(f"File {filename} not found")

def ValidateStringFormat (text:str):
    '''
    A function called ValidateStringFormat that receives a string
    and validates that it matches a specific pattern.

    Starts with 3 uppercase letters
    Followed by 4 digits
    Followed by 2 lowercase letters

    :param text: The string to validate

    :return:
    Return True if valid, otherwise False. Do not use regular expressions.
    '''
    if len(text) < 9:
        return False
    return text[0:3].isupper() and text[3:7].isdigit() and text[7:9].islower()

def GetSumSize(files):
    '''
    A function called GetSumSize that receives a list of files
    :param files: the list of files to calculate the sum of
    :return: The sum of all the files sizes
    '''
    sum_size = 0
    for file in files:
        size = GetFileSize(file)
        if size is None:
            continue
        sum_size += size
    return sum_size

def GetListOfFiles():
    '''
    A function called GetListOfFiles that generates a list of files
    :return: A list of file names
    '''
    filenames = []
    while True:
        user_input = input("Please enter a filename. Enter empty input to finish: ")
        if user_input == '':
            break
        filenames.append(user_input)
    return filenames

def GetWordsFromFile(filename):
    '''
    a function called GetWordsFromFile that receives a string representing a
    filename
    :param filename: the file name
    :return:  a list of all unique
    words that appeared in the file (no duplicates).
    '''
    words = set()
    try:
        with open(filename, "r") as file:
            for line in file:
                for word in line.split():
                    words.add(word.lower())
    except FileNotFoundError:
        print(f"File {filename} not found")

    return list(words)

def GenerateRandomNumber():
    '''
    A function called GenerateRandomNumber that generates a random number between LOWEST_NUM and HIGHEST_NUM
    :return: a random number between LOWEST_NUM and HIGHEST_NUM
    '''
    random_number = random.randint(LOWEST_NUM, HIGHEST_NUM)
    return random_number

def CalculateAverage(num_list):
    '''
    A function called CalculateAverage that calculates the average of Num_list
    :param num_list: list of numbers
    :return: the average of the numbers
    '''
    return sum(num_list) / len(num_list)

def CalculateStandardDeviation(num_list):
    '''
    A function called CalculateStandardDeviation that calculates the standard deviation
    :param num_list: list of numbers
    :return: the standard deviation of the numbers
    '''
    avg = CalculateAverage(num_list)
    return ((1/len(num_list))*sum(((num - avg)**2) for num in num_list))**0.5

def CalculateMedian(num_list):
    '''
    A function called CalculateMedian that calculates the median of the Num_list
    :param num_list: the list of numbers
    :return: the median of the numbers
    '''
    sorted_list = sorted(num_list)
    if len(num_list) % 2 == 1: #Odd
        return sorted_list[len(num_list) // 2]
    else:  #Even
        return CalculateAverage([sorted_list[len(sorted_list) // 2], sorted_list[len(sorted_list) // 2 + 1]])

def CalculateMode(num_list):
    '''
    A function called CalculateMode that calculates the mode of the Num_list
    :param num_list: the list of numbers
    :return: the mode of the numbers
    '''
    count_dict = {}
    for num in set(num_list):
        count_dict[num] = num_list.count(num)
    max_value = max(count_dict.values())
    return [key for key, value in count_dict.items() if value == max_value]

def GenerateRandomNumbersFile(filename :str, n:int):
    '''
    a function called GenerateRandomNumbersFile that receives a filename
     and an integer n. Generate n random integers between 1 and 1000.
     than calculate their: Average, Standard deviation, Median and Mode.
     Then writing all results (the generated numbers + statistics) to the file.
     Using only the random module (no NumPy or statistics module).
    :param filename: the file name.
    :param n: the number of random numbers to generate.
    :return:  None
    '''
    num_list = []
    for i in range(n):
        num_list.append(GenerateRandomNumber())
    avg = CalculateAverage(num_list)
    std_dev = CalculateStandardDeviation(num_list)
    median = CalculateMedian(num_list)
    mode = CalculateMode(num_list)

    with open(filename, "w") as file:
        file.write(f"{num_list}\n")
        file.write(f"Average = {avg}\n")
        file.write(f"Standard Deviation = {std_dev}\n")
        file.write(f"Median = {median}\n")
        file.write(f"Mode = {mode}\n")

print("Question 2: Get File Size:")
file = input("Enter file name: ")
print(GetFileSize(file))

print("Question 3: Validate String Format:")
text = input("Enter string to validate: ")
print(f"The result for the text you entered is {ValidateStringFormat(text)}")

print("Question 4: Get Sum Size:")
result = GetSumSize(GetListOfFiles())
print(f"The size for all the files you have entered is {result}")

print("Question 5: Get Words From File:")
result = GetWordsFromFile(input ("Enter file name: "))
print (f"Here is the list of unique words from the file: {result}")

print ("Question 6: Generate Random Numbers File:")
file_name = input("Enter file name: ")
n = int(input("Enter number of random numbers to generate: "))
GenerateRandomNumbersFile(file_name, n)