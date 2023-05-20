#python text message sender automation
#pip install the library: schedule 1.0.0
#pip install the library: requests
#create a separate file with your cellphone number, name it credentials

from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        "phone": mobile_number,
        "message": "Hi, goodmorning",
        "key": "textbelt", #this key allows for a 1 free message on the site
    })
    print(resp.json())
    
schedule.every().day.at("06:00").do(send_message)

#for every few seconds here is the code

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
