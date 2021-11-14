import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)

print('listing the name of the people:')
for person in json['people']:
    print(person['name'])