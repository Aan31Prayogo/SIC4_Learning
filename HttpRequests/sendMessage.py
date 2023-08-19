import requests

def send_msg(text):
   token = "5936063047:AAEegGclhoRYVF2AnKsnWlAn-g0uwgLvT6o"
   chat_id = "672670660"
   url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text 
   results = requests.get(url_req)
   print(results.json())

send_msg("HEllo SIC4!")