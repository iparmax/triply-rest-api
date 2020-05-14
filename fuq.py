import requests
import json

url = 'http://localhost:8000/api/trips/'
# myobj = {"email": "iparmaksizoglou@gmail.com","user_id" :"6969696969","origin": "(69.696969,69.6969696)"\
#     ,"destination": "(69.696969,69.6969696)","dep_time":"12:00"}

# x = requests.post(url, data = myobj)







x = requests.get(url).json()
print(x)
