
from flask import render_template

import pywhatkit

class SenderController:

    def send_message(self):

        # Same as above but Closes the Tab in 2 Seconds after Sending the Message
        pywhatkit.sendwhatmsg("+55091981502481", "Hi", 16, 55, 15, True, 2)

        