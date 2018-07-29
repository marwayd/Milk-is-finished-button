# Milk-is-finished-button
Simple button reflex which when pressed will alert us via sms that we need to get more milk

## 1) Twilio account setup and python script to send a SMS text message

## 2) Amazon Dash button setup > The first thing you need to do is configure your buttons to send messages when you push them but not actually order anything. When you get a Dash button, Amazon gives you a list of setup instructions to get going. **Don’t complete the final step — don’t select the particular product you want ordered.** The best way to do this is: Amazon App > Setting > Dash > Setup button as per instructions without selecting a product.

## 3) Work out the MAC address of the Amazon Dash button - Two ways of doing this, either via Amazon Dash and IP address method or via use of WireShark. I prefer option 2.

   1) Press the amazon Dash button for 5 seconds until you see a blue light > Then go to the wireless icon and select the Amazon... option > in a seperate web browser after a few seconds access 'http://192.168.0.1/' > MAC address is listed - make a note.

   2) Access Wireshark > Select the wi-fi option on the splash screen > in the search at the top enter ARP and press enter > press the button > Look for Amazon... > Select 'Address resoultion protocol' > Make a note of the 'Sender Mac address XX:XX:XX:XX:XX:XX'
