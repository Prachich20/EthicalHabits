from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

from sms.models import Sms

app = Flask(__name__)

message = "Dear Sender\nThank you for reaching out to us. We appreciate your time and effort in contacting us.\nTo " \
          "ensure we are able to resolve your concern or issue sufficiently, please send us the following information " \
          "if not already provided earlier.\nYour Name (optional)\nYour Location\nYour Address\nAlternate number\nIssue " \
          "Details\nPlease note that we have strict no-retaliation policy to protect the interests of all workers. " \
          "The information will be treated with utmost confidentiality and appropriate action will be taken to " \
          "address the concerns.\nThank you "


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    # Add a message
    resp.message(message)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
