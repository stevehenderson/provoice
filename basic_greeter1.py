# Importing modules

import re
import nltk
from nltk.corpus import wordnet
import random

# Building a list of Keywords

list_words=['hello','timings']
#TODO print all lines so you understand whats happening. Then add more 'key words'
#TODO for provoice, remove stop words, then pull keywords and send to 'greeter'
# rerouteo thers to wiki model or dictionary model
# long term, figure out 'deep learning model' or even  just model that processes text such as shakespeare,
# or whats app or text convos from net
list_syn={}

for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word): # finds synonyms of user designated words using wordset library
        #print(syn.definition())
        for lem in syn.lemmas(): # finds lemma (canonical form of word) for all synonyms in list
            #print(lem) # Raw lemma info example : Lemma('hello.n.01.hello')
            # Remove any special characters from synonym strings AND pulls lemma name from raw lemma info
            lem_name = re.sub('[^a-zA-Z0-9 \n\.]', ' ', lem.name())
            #print(lem_name)
            synonyms.append(lem_name)
    print(synonyms)
    list_syn[word]=set(synonyms) # uses word from list_words as key in dictionary. Value is a 'set' from synonyms list

print(list_syn)

# Building dictionary of Intents & Keywords
keywords={}
keywords_dict={}

# Defining a new key in the keywords dictionary
keywords['greet']=[]

# TODO what are RegEx metacharacters and why are they important
# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['hello']):
    keywords['greet'].append('.*\\b'+synonym+'\\b.*') # note + signs are required syntax here. Not sure why.
# Defining a new key in the keywords dictionary
keywords['timings']=[]

# Populating the values in the keywords dictionary with synonyms of keywords formatted with RegEx metacharacters
for synonym in list(list_syn['timings']):
    keywords['timings'].append('.*\\b'+synonym+'\\b.*')
print("------keywords `plain` dict_____")
print(keywords)

for keys, values in keywords.items(): # jared changes this to `for keys, values` from intent, keys.
# Shouldn't be keys as that is values that is being iterated over
    # Joining the values in the keywords dictionary with the OR (|) operator updating them in keywords_dict dictionary
    print("intent is {}, keys is {}".format(keys, values))
    keywords_dict[keys]=re.compile('|'.join(values))
print("-------keywords_dict________")
print (keywords_dict)

#{'greet': re.compile('.*\\bhullo\\b.*|.*\\bhow-do-you-do\\b.*|.*\\bhowdy\\b.*|.*\\bhello\\b.*|.*\\bhi\\b.*')}

# Building a dictionary of responses

responses = {
    'greet': ["Hello! How can I help you?", "hi", "hey", "whats up",],
    'timings':'We are open from 9AM to 5PM, Monday to Friday. We are closed on weekends and public holidays.',
    'fallback':'I dont quite understand. Could you repeat that?',}


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
            matched_lemma=keys #keys here is lemma word
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