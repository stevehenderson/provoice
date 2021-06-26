# ProVoice

## Overview 

ProVoice is an intelligent chat assistant designed to give you that 
"perfect thing to say" in repsonse to any text input  (text, tweet, Slack, etc).
This works much like typing suggestions, but is slightly more suggestive and 
also configurable and context aware to fit the particular communications scenario.

For example, assume a friend  tweets the following:

   * "I hate public bathrooms! why is the door so short?"

ProVoice would be able to give you context-sensitive responses based on your mood, time of day, 
your relationship to the sender, etc.

So, if this is your mother, ProVoice might suggest the following response:

   * "LOL reminds me of some great potty training moment :)"

If it was your college roommate, and you're set to "playful mood" it might suggest:

   * "WHOA, how many times avae you sent that exact same tweet?  Are you tweeting us from while doing the deed?"


## Components

ProVoice consists of the following components:

  * A RESTful Web Application Program Interface (API).   This is the main brain of ProVoice.  You send 
it input, it cranks the repsponse, and returns it to you as a json object.  It's up to you to
    format and render.
    
  * A Test web-based UI where you can test the API 

## Roadmap

   * July 2020 :  Get a basic API up with some very simple responses, assuming a single user.  Focus on an architecture
that is modular and allows expansion based on various capability.
     
   * August 2020 :  Establish multi-tennent/multi-user capability.  Individuals get their own experiences.

   * September 2020:  Add increasingly complex AI modules.  Leverage Alexa and Google Voice APIs.  Search and sentiment.





