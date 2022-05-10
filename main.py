import requests
username = input("Account username \n")
viewCount = input("How many views would you like to add? \n")
for x in range(0, int(viewCount)):
  response_API = requests.get('https://furaffinity.net/user/' + username)
  print(str(x+1) + " page view(s) added.")
