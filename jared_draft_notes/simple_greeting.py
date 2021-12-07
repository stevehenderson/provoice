import nltk
import random
import string


#raw_user_input = input("please enter some text")
#input_token_words = nltk.word_tokenize(raw_user_input)


wnlemmatizer = nltk.stem.WordNetLemmatizer()

def perform_lemmatization(tokens):
    return [wnlemmatizer.lemmatize(token) for token in tokens]

punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)

def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(punctuation_removal)))

# hard coded greetings list - move to csv or database or similar
standard_greeting = ["hello", "hi", "hey", "good morning", "good afternoon"]
standard_greeting_Q = ["how are you", "how are you doing"]
standard_greeting_Q2 = ["hows it going", "how are things", "whats"]

# hard coded responses - move to csv or database?
standard_greeting_resp = ["Hi!", "Hey!", "Hello!", "Great to hear from you!"]
standard_greeting_Q_resp = ["Im well, how are you", "I'm doing great! You?"]
standard_greeting_Q2_resp = ["Everything's good, just hangin", "Not much, how are you?"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in standard_greeting:
            return random.choice(standard_greeting_resp)
        elif token.lower() in standard_greeting_Q:
            return random.choice(standard_greeting_Q_resp)
        elif token.lower() in standard_greeting_Q2:
            return random.choice(standard_greeting_Q2_resp)


#print(generate_greeting_response(input_token_words))

continue_dialogue = True
print("Hello, I am your friend TennisRobo. You can ask me any question regarding tennis:")
while(continue_dialogue == True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
            continue_dialogue = False
            print("TennisRobo: Most welcome")
        else:
            if generate_greeting_response(human_text) != None:
                print("TennisRobo: " + generate_greeting_response(human_text))
            else:
                print("TennisRobo: ", end="")
                print("no response")
                #print(generate_response(human_text))
                #article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("TennisRobo: Good bye and take care of yourself...")

#TODO doesn't like multi word input
