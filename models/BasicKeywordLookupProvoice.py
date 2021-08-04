'''

  A basic model that looks up multiple keywords.

'''
import json


corpus = {
    "army, military, Iraq, Bosnia, helicopters" : "Yeah, I used to be in the Army!",    
    "mac, linux, pc, windows, computer, program, hacking, code" : "Man that sounds just like my job..",    
    "nfl, football, Cowboys" : "There's only one team:  GO GIANTS!",
    "watching, streaming, TV, Movies, Netflix, HBO, ESPN" : "Actually, I only watch one thing:  Magnum PI (the orig)"
}

class BasicKeywordLookupProvoice():

    # Constructor
    def __init__(self):
        self.id = "basic_keyword_lookup_provoice"
        self.description = "A basic multi keyword Provoice model."
        self.flat_corpus = {}
        for keywords, response in corpus.items():
            for keyword in keywords.split(","):
                # force the keyword to be stored as lowercase; also strip any leading/trailing spaces
                keyword_flat = keyword.lower().strip()
                self.flat_corpus[keyword_flat] = response
        
        print("Loaded flat corpus: {}".format(self.flat_corpus))

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
            if wlower in self.flat_corpus:
                responses.append(self.flat_corpus[wlower])
        
        result['response'] = responses

        return result


