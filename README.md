# Telnyx-Flooder
# NOT MAINTAINED ANYMORE
Uses the Telnyx API to flood numbers. Good for taking down scam call centers temporarily. Please don't use it on anyone innocent. I mean... if they ask to get flooded and they know what would happen, then go ahead. THIS IS FOR EDUCATIONAL PURPOSES.
Inspired by https://github.com/Jfaler/soup
Will suck up all the money in your telnyx account eventually due to the nature of call flooding

# Setup
- Make sure to have python 3 installed
- Type in pip install telnyx, then type in pip install six
- Go into your telnyx portal, go onto Call Control and set up your application. For the webhook URL, just type in any website you want since you won't need this. Make sure to also select your outbound call profile (Create one if you don't have one).
- Modify the flood.py file to include your API Key and your Call Control ID (To get your Call Control ID, click on the edit button on the call control page, then copy the ID that's there.

**You're done! Right click on flood.py, then open it with python 3, or python3.10  or whatever python3 version you have**
