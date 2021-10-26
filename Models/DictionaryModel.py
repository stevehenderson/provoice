'''

  A basic model that looks up multiple keywords.

  Dictionary credit:  https://www.bragitoff.com/2016/03/english-dictionary-in-csv-format/

'''
import glob
import json
import os
from random import randrange


dictionary_folder_path = "/_attic_/provoice_v2/data/dictionary"

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
                        if next_dict is not None:
                            next_word = next_dict["word"]
                            if next_word in self.corpus:
                                self.corpus[next_word].append(next_dict)
                            else:
                                self.corpus[next_word] = [next_dict]
                            count=count+1
                            if count % 250 ==0:
                                pass
                                #print("Loaded {} lines from {}".format(filename,count))
                               #return("Loaded {} lines from {}".format(filename,count))
        

        # with open(os.path.join(dictionary_folder_path), 'w') as f2:
        #     f2.write(json.dumps(self.corpus))

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

        try:
            #Split line on close parens
            ## Babble (v. i.) To talk incoherently; to utter unmeaning words.
            line_parts = line.split(")")    
            word = line_parts[0].split("(")[0].strip().lower()
            pos = line_parts[0].split("(")[1].strip().lower()
            definition = ")".join(line_parts[1:]).strip().lower()

            result = {}
            result["word"] = word
            result["pos"] = pos
            result["definition"] = definition
            #print(result)
            return result
        except Exception as e:
            #print("ERROR processing {}".format(line))
            return None
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

            #Only pick longer words
            if len(wlower) > 4 and wlower in self.corpus:
                word_dicts = self.corpus[wlower]

                #If a word has multiple definitions -- pick randomly
                #TODO:  Could use another strategy here, such as a richer text, or college reading level
                pick = randrange(len(word_dicts))
                word_to_add = word_dicts[pick]["word"]
                def_to_add = word_dicts[pick]["definition"]
                responses.append("({}): {}".format(word_to_add,def_to_add))
        
        result['response'] = responses
       # print(result)

        return result

