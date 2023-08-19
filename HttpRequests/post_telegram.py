import requests
import time
import os
#5382390963


TOKEN = '5936063047:AAEegGclhoRYVF2AnKsnWlAn-g0uwgLvT6o'
chat_id = 672670660   #chat id pengguna
image_name = os.getcwd() + "/" + "python_logo.png"

list_chat_id = ["672670660", "5382390963"]

#url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
#url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}'   #query  
                                                                            #endpoint

#resp = requests.post(url, files={'photo':image})

# if int(resp.status_code) == 200:
#     print("succes send image")

for chat_id in list_chat_id:
    image = open(image_name,'rb')
    #print(chat_id)
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={chat_id}'   #query  
    resp = requests.post(url, files={'photo':image})

    #res = requests.post(url , json=payload)
    print(resp.status_code)
    #if int(resp.status_code) == 200:
    #    print("succes send image")
    time.sleep(2)
