from flask import Flask, Response, request
import json

# Response body json
body = {
    "name": "Molnár Roland",
    "statements": statements,
    "friends": friends
}
response = Response(json.dumps(body))


# Response header beállítás
response = Response()
response.headers['Content-Type'] = 'application/json; charset=utf-8'

# Request body kiolvasás
request_body = request.get_json()


# Fájl kezelése

# Beolvasás
friends = json.load(open('friends.txt', 'r'))

request_body = {"from": "from"}

# Listába helyezés és a lista fájlba írása
if request_body['from'] not in friends:
    friends.append(request_body['from'])
    with open('friends.txt', 'w') as filehandle:
        json.dump(friends, filehandle)

