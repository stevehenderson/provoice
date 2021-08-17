'''

  A basic model that looks up multiple keywords.

'''
import glob
import json
import os
from random import randrange


dictionary_folder_path = "./data/dictionary"

class DictionaryModel():

    # Constructor
    def __init__(self):
        self.id = "dictionary_model"
        self.description = "A multi keyword Provoice model that matches words in dictionary."

        self.corpus = {}

        #Read the dictionary CSVs
        for filename in glob.glob(os.path.join(dictionary_folder_path, '*.csv')):
            with open(filename, 'r', errors='replace') as f:                
                count = 0
                for line in f:             
                    if len(line) > 1:
                        next_dict = self.process_line(line)
                        next_word = next_dict["word"]
                        if next_word in self.corpus:
                            self.corpus[next_word].append(next_dict)
                        else:
                            self.corpus[next_word] = [next_dict]
                        count=count+1
                        if count % 250 ==0:
                            print("Loaded {} lines from {}".format(filename,count))
        
        
        with open(os.path.join(dictionary_folder_path, 'formatted_dictionary.json'), 'w') as f2:                
            f2.write(json.dumps(self.corpus))

    #
    # Process a line from a dictionary and return a word, POS, definition
    #
    #
    # Ex: Babble (v. i.) To talk incoherently; to utter unmeaning words.
    #
    # { word: babble,
    #   pos: verb-indefinite,
    #   definition: "to talk incoherently; to utter unmeaning words."
    # }
    #    
    #
    def process_line(self,line):        

        #Clean fwd and trailing quotes (if present)
        if line[0] == "\"":
            line=line[1:len(line)-2]

        #Split line on close parens
        line_parts = line.split(")")    
        word = line_parts[0].split("(")[0].strip().lower()
        pos = line_parts[0].split("(")[1].strip().lower()
        definition = ")".join(line_parts[1:]).strip().lower()

        result = {}
        result["word"] = word
        result["pos"] = pos
        result["definition"] = definition
        print(result)
        return result

        return True
        #print(line)

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

        #Replace any commas with spaces, so we only have one delimeter character
        input = input.replace(",", " ")

        #Replace any other punctuation  (TODO: There are better ways to do this..)
        input = input.replace("?", " ")
        input = input.replace(".", " ")

        
        #break up each word in the input
        all_words = input.split(" ")

        for w in all_words:
            #print("checking word: {}".format(w))
            wlower = w.lower()
            if wlower in self.corpus:
                word_dicts = self.corpus[wlower]
                pick = randrange(len(word_dicts))
                def_to_add = word_dicts[pick]["definition"]
                responses.append(def_to_add)
        
        result['response'] = responses

        return result


