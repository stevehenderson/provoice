# Importing modules

import re
import nltk
from nltk.corpus import wordnet
import random


# Building dictionary of Intents & Keywords
keywords={}
keywords_dict={
    'greet_basic': re.compile('.*\\bhi\\b.*|.*\\bhello\\b.*|.*\\bhowdy\\b.|.*\\bhey\\b.*|.*\\bhow are you\\b.*'),
    'doing': re.compile('.*\\bwhat are you doing\\b.*|.*\\bwhat are you up to\\b.*|.*\\bdoing today\\b.*')

}

# Building a dictionary of response

responses = {
    'greet_basic': ["Hello!", "Hi", "Hey", "Whats Up!",],
    'doing':["Not much", "Just hanging out", "Just working, you?", "No plans! How about you?"],
    'fallback':'ERROR no response from greeting screener'
}


print ("Welcome to MyBank. How may I help you?")


# While loop to run the chatbot indefinetely

while (True):
    # Takes the user input and converts all characters to lowercase
    user_input = input().lower()
    # Defining the Chatbot's exit condition
    if user_input == 'quit':
        print ("Thank you for visiting.")
        break

    matched_lemma = None
    for keys, pattern in keywords_dict.items(): # pattern here is values of keyword_dict
        # Using the regular expression search function to look for keywords in user input
        if re.search(pattern, user_input):
            # if a keyword matches, select the corresponding key from the keywords_dict dictionary
            matched_lemma=keys #keys here is lemma wordd
            print(matched_lemma)


    key='fallback' # default key is fallback response incase there is no response for this chatbot etc... not needed for provoice so much
    if matched_lemma in responses:
        # If a keyword matches, the fallback response key is replaced by the matched_lemma as the key for the responses dictionary
        key = matched_lemma
        # The chatbot prints the response from responses dictionary that matches the key found in both dictionaries, found from searching user input

    print(responses[key])
    final_response_list = list(responses[key])
    chosen_response = random.choice(final_response_list)
    print(chosen_response)