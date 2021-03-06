import recastai
from pprint import pprint
from . import replies as message_handler



RECAST_ACCESS_TOKEN = '95bed182f2b541ccefc1084bd76826bb'
LANG = 'en'


class Recast(object):
    """
    An object responsible for all recast related functionality
    """

    INTENT_TYPE = {
        'greetings': 'text',
        'goodbyes': 'text',
        'showfilters': 'image',
        'help-intent':'text',
        'recommend':'image',
        'server-downtime':'text',
        'theme':'text',
    }

    def __init__(self):
        self.client = recastai.Client(RECAST_ACCESS_TOKEN, LANG)

    def understand_intent(self, text):
        """
        Takes as input text and return the intent.
        """

        response = self.client.text_request(text)


        if response.intent() is not None:
            return response.intent().slug, Recast.INTENT_TYPE[response.intent().slug], response.intent().confidence
        else:
            return None, None, 0.0

    def parse_response_from_intent(self, intent):
        """
        Takes as input the users' intent and return a response
        """

        replies = message_handler.Replies()

        reply = replies.handle_intent(intent)

        print "Response: %s" % reply
        if reply:
            return reply
        else:
            return "Sorry. Unfortunately I couldn't understand you!"

