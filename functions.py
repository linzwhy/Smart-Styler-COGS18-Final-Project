"""
This module contains all the functions for the smart styler quiz.
"""

import os
from time import sleep
from PIL import Image

def are_there_duplicates(list_to_check):
    """
    Looks for duplicates in a list.

    Parameters
    ----------
    list_to_check : list
        the list to check for duplicates.

    Returns
    -------
    output : bool
        False if all elements are unique, True if otherwise.
    """

    if len(list_to_check) == len(set(list_to_check)):
        output = False
    else:
        output = True

    return output

def intro():
    """
    Starts the quiz.

    Parameters
    ----------
    none

    Returns
    -------
    start_quiz : str
        Continues to the rest of the quiz after user input.
    """

    intro_msg = "----------------------------------------------------------" + \
                "\nHello! Welcome to the Smart Styler." + \
                "\nI will choose an outfit for you based on your personality!" + \
                "\nReady? Press enter to get started. \n" + \
                "----------------------------------------------------------"
    start_quiz = input(intro_msg)

    return start_quiz

def get_name():
    """
    Gets the user's name.

    Parameters
    ----------
    none

    Returns
    -------
    name : str
        Stores user input in a variable to use later.
    """

    name = input("--> First off, what is your name? ").capitalize()
    print("Nice to meet you, " + name + ".\n")

    return name

def get_gender():
    """
    Gets the user's gender preference.

    Parameters
    ----------
    none

    Returns
    -------
    gender : str
        Stores the appropriate abbreviation for the gender preference.
    """

    gender_question = "(For all questions, please type the corresponding " + \
               "letter in lowercase to choose an answer.)\n" + \
               "\n--> What gender matches your style preference the most?\n" + \
               "f - feminine\nm - masculine\n"
    gender_answers = {"f" : "fem", "m" : "masc"}

    user_input = input(gender_question)
    gender = gender_answers[user_input]

    return gender

def get_color():
    """
    Gets the user's color palette preference.

    Parameters
    ----------
    none

    Returns
    -------
    color : str
        Stores the appropriate abbreviation for the color preference.
    """

    color_question = "--> What color palette are you drawn to the most?\n" + \
              "a - Cool colors: blues, greens, purples\n" + \
              "b - Warm colors: reds, oranges, yellows\n" + \
              "c - Neutral colors: black, white, browns\n"
    color_answers = {"a" : "cool", "b" : "warm", "c" : "neut"}

    user_input = input(color_question)
    color = color_answers[user_input]

    return color

def get_style():
    """
    Gets the user's style.

    Parameters
    ----------
    none

    Returns
    -------
    style : str
        Stores the appropriate abbreviation for the style preference based on answers.
    """

    user_choices = []

    style_questions = [("--> Choose the list of words that best describe you.\n"
                  "a - calm, homebody, laid back\n"
                  "b - hard worker, motivated, classy\n"
                  "c - upbeat, creative, free-spirit\n"),
                 ("--> Pick your perfect night out.\n"
                  "a - Night out? More like night in... binging my favorite show.\n"
                  "b - Fancy dinner, pampering myself, and a book/podcast before bed.\n"
                  "c - Watching a band perform live (probably one you've never heard of).\n"),
                 ("--> Choose your ideal job.\n"
                  "a - Working from home (while keeping an eye on my kids/pets)\n"
                  "b - CEO/founder of a corporation\n"
                  "c - Director of an art museum\n")]
    extra_question = "--> What brings you the most joy?\n" + \
                  "a - Spending time with friends and family.\n" + \
                  "b - Checking things off my to-do list, feeling accomplished for the day.\n" + \
                  "c - Creating/viewing art and/or music.\n"
    style_answers = {"a" : "cas", "b" : "prof", "c" : "creat"}

    for question in style_questions:
        choice = input(question)
        user_choices.append(choice)

    if are_there_duplicates(user_choices):
        pass
    else:
        user_choices.append(input(extra_question))

    #look at the list of answers and detemine the highest occurring one
    most_common = max(user_choices, key = user_choices.count)
    style = style_answers[most_common]

    return style

def determine_outfit(style, color, gender):
    """
    Concatenates the user's info into a corresponding jpg filename.

    Parameters
    ----------
    style : str
        The user's style determined from get_style().
    color : str
        The user's color preference determined from get_color().
    gender : str
        The user's gender preference determined from get_gender().

    Returns
    -------
    final_fit : str
        The concatenated string of info that matches a jpg filename.
    """

    final_fit = style + "_" + color + "_" + gender + ".jpg"

    return final_fit

def results_msg(name):
    """
    Prints a message preceding the quiz results.

    Parameters
    ----------
    name : str
        Used in a personalized message.

    Returns
    -------
    none
    """

    print("\n\nOkay, " + name + "! I think I got everything I need, give me a moment. :)")
    sleep(1.50)
    print("Compiling answers . . .")
    sleep(0.75)
    print("Generating outfit . . .")
    sleep(0.75)
    print("Having a snack . . .")
    sleep(0.75)
    print("Success!\n")
    sleep(0.75)

def restart_quiz():
    """
    Asks the user if they want to take the quiz again.

    Parameters
    ----------
    none

    Returns
    -------
    output : function call or print statement
        Based on user input, calls smart_styler() or shows a message to end running cell.
    """

    restart = input("--> Would you like to take the quiz again?\n" + \
                    "y for yes, n for no ")

    if restart == "y":
        output = smart_styler()
    else:
        output = print("Thanks for playing!")

    return output

def smart_styler():
    """
    The entire quiz from start to finish.

    Parameters
    ----------
    none

    Returns
    -------
    none
    """

    intro()

    name = get_name()
    gender = get_gender()
    color = get_color()
    style = get_style()
    outfit = determine_outfit(style, color, gender)

    results_msg(name)

    #get the user's current working directory to get to the image
    file_path = os.getcwd()
    final_outfit = Image.open(file_path + "/outfits/" + outfit)

    final_outfit.show()

    restart_quiz()
