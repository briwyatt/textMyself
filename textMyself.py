#! python3.6
from twilio.rest import Client
from creds import *


def textmyself(message):
    """
    texts a message passed to it as a string.


    Whenever you want one of your programs to text you, just add the following code:
    import textmyself
    textmyself.textmyself('The boring task is finished.')

    args: string
    returns: None

    # make a Client object ➋,
    # and call create() with the message you passed ➌.
    """
    message1 = message
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message1, from_=twilioNumber, to=myNumber)


    # If you want to make the textmyself() function available to your other programs,
    # place the textMyself.py file in the same folder as your Python script.




