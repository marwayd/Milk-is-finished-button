# Test that twilio has been setup correctly and that a SMS message can be sent via us of the account, token, from number and to number
# Go to twilio.com and setup a new account. 
# After you’ve signed up, assign a number. 
# Make a note of the phone number you’ve bought, your Account SID, and your Auth Token.
# Go to the list of Verified Caller IDs and make sure the number you want the button to call is listed. If not, add it.

from twilio.rest import Client

account = "" #The Account SID you copied from your Twilio account dashboard
token = "" #The Auth Token you copied from the same place
client = Client(account, token)

message = client.messages.create(to="", from_="",
                                 body="We are out of milk...get some milk!")