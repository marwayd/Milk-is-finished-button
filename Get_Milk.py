# Main python program to send SMS once the Amazon dash button has been pressed.
# Pre-requisites are: SMS functionality has been setup first and has been tested for functioning; Amazon dash button setup, apart from selecting a product, 

from twilio.rest import Client
from scapy.all import * #this may need to be installed

account = "" #The Account SID you copied from your Twilio account dashboard
token = "" #The Auth Token you copied from the same place
client = Client(account, token)

MAC_ADDRESS = '' # enter Dash Button's MAC Address here.

def detect_button(pkt):
    if pkt.haslayer(DHCP) and pkt[Ether].src == MAC_ADDRESS:
            print "Button Press Detected" #so that I can then expect a SMS, added for troubleshooting initially
            message = client.messages.create(to="", from_="", #number from and to - twilio
                                 body="We are out of milk...get some milk!")

sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0)