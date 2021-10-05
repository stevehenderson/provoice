class Suggestion():
    def __init__(self):
        self.text = None

    def __init__(self, new_suggestion):
        self.text = new_suggestion

    def to_json(self):
        data = {}
        data["text"]=self.text
        return data
