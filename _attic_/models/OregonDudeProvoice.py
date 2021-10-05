'''

    Jared's first model for ProVoice. Very basic model attempting to use
    function, dictionary and if statements.

'''

import json
import string
import random

class OregonDudeProvoice():

    # Constructor
    def __init__(self):
        self.id = "OregonDude_ProVoice"
        self.description = "An Oregon flavored ProVoice Model"

    # Helper method to make this class serializable
    def toJson(self):
        response = {}
        response['id'] = self.id
        response['description'] = self.description
        return response


    def get_oregon_response(self, user_input):
        keywords_fishing = ["fishing", "fish", "river", "lake", "boat", "pole",
                            "rod", "reel"]
        fishing_responses = ["Right on dude, catch any rainbows?", "What were you using?"]

        keywords_fire = ["standby", "evacuate", "smoke", "fire", "acres",
                        "dry", "smokey"]
        fire_responses = ["ya it sure is smokey", "I heard this smoke made it all the "
                                                "way to NY!", "This ain't nothing but a campfire"]

        keywords_oldtimer = ["crowded", "people", "traffic", "condos", "hipsters",
                            "california", "crowds", "lines", "no fish"]
        oldtimer_responses = ["Man I remember when this all used to be forest, not"
                            "condos for the californians.", "Ya there's a lot of "
                                                            "people on the roads."]

        keywords_daily = ["busy", "tired", "boss"]
        daily_responses = ["I feel ya brotha, just keep on keepin' on", "Sounds like "
                                                                        "you need a good cup of coffee!"]
        keywords_heatwave = ["hot", "heat", "A/C", "degrees", "deg", "fahrenheit"]
        heatwave_responses = ["Try to stay cool, sounds like a good time to hit "
                            "the lake!", "Yikes, don't forget your sunscreen"]
        result = {}
        if any(i in keywords_fishing for i in user_input.split()):
            result['response'] = random.choice(fishing_responses)

        if any(i in keywords_fire for i in user_input.split()):
            result['response2'] = random.choice(fire_responses)

        if any(i in keywords_oldtimer for i in user_input.split()):
            result['response3'] = random.choice(oldtimer_responses)

        if any(i in keywords_daily for i in user_input.split()):
            result['response4'] = random.choice(daily_responses)

        if any(i in keywords_heatwave for i in user_input.split()):
            result['response5'] = random.choice(heatwave_responses)
        if len(user_input) == 0:
            result['response6'] = ("Ok cool")
        result['model'] = self.toJson()
        return result

