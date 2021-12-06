'''

  Third model that screens input for common greetings such as "Hello.

'''

import json
import re
import random



# Building dictionary of Intents & Keywords
keywords={}
keywords_dict={
    'greet_basic': re.compile('hi|hello|howdy|hey|how are you'),
    'doing': re.compile('what are you doing|what are you up to|doing today|'),

}

# Building a dictionary of response

responses = {
    'greet_basic': ["Hello!", "Hi", "Hey", "Whats Up!",],
    'doing':["Not much", "Just hanging out", "Just working, you?", "No plans! How about you?"],
    'fallback':'ERROR no response from greeting screener'
}



class BasicGreetingProvoice():

    # Constructor
    def __init__(self):
        self.id = "wiki_search_two_provoice"
        self.description = "Second model that selects a difficult word from user input and returns" \
                           "a response from Wikipedia, slightly more refined than WikiSearchOne."

    # Helper method to make this class serializable
    def toJson(self):
        response = {}
        response['id'] = self.id
        response['description'] = self.description
        return response

    # The main function of the class.  Works with the API to return a response
    def get_provoice_response(self, input):
        result = {}
        result['input'] = input
        result['model'] = self.toJson()


        responses = []

        # Replace any commas with spaces, so we only have one delimeter character
        input = input.replace(",", " ")

        # Replace any other punctuation  (TODO: There are better ways to do this..)
        input = input.replace("?", " ")
        input = input.replace(".", " ")


        # break up each word in the input
        all_words = input.split(" ")


        # Takes the user input and converts all characters to lowercase
        user_input = input().lower()


        matched_lemma = None
        for keys, pattern in keywords_dict.items(): # pattern here is values of keyword_dict
            # Using the regular expression search function to look for keywords in user input
            if re.search(pattern, user_input):
                # if a keyword matches, select the corresponding key from the keywords_dict dictionary
                matched_lemma=keys #keys here is lemma word


        key='fallback' # default key is fallback response incase there is no response for this chatbot etc... not needed for provoice so much
        if matched_lemma in responses:
            # If a keyword matches, the fallback response key is replaced by the matched_lemma as the key for the responses dictionary
            key = matched_lemma
            # The chatbot prints the response from responses dictionary that matches the key found in both dictionaries, found from searching user input
        #print(responses[key])
        final_response_list = list(responses[key])
        chosen_response = random.choice(final_response_list)
        result['response'] = (chosen_response)
        return result
