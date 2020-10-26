import json
# Fájl kezelése

# Beolvasás
friends = json.load(open('friends.txt', 'r'))

request_body = {"from": "from"}

# Listába helyezés és a lista fájlba írása
if request_body['from'] not in friends:
    friends.append(request_body['from'])
    with open('friends.txt', 'w') as filehandle:
        json.dump(friends, filehandle)
