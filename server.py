from flask import Flask, Response, request
import json

app = Flask(__name__)


statements = [
        "Voltam Grönlandon",
        "Zöldöves karatés vagyok",
        "Úsztam már óceánban"
    ]    

truestatement = 1

friends = json.load(open('friends.txt', 'r'))

@app.route('/', methods=['GET'])
def home():
    body = {
        "name": "Molnár Roland",
        "statements": statements,
        "friends": friends
    }
    response = Response(json.dumps(body))
    
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

@app.route('/statement/<number>', methods=['GET'])
def statement(number):
    number = int(number)
    if number < 0 or number > 2:
        return Response("Not found", 404)
    
    body = {
        "statement": statements[number],
        "istrue": number == truestatement
    }
    response = Response(json.dumps(body))
    
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


@app.route('/guess', methods=['POST'])
def guess():
    request_body = request.get_json()
    
    print(request_body)
    
    if request_body['truestatement'] == truestatement:
        if request_body['from'] not in friends:
            friends.append(request_body['from'])
        with open('friends.txt', 'w') as filehandle:
            json.dump(friends, filehandle)
        response = Response(json.dumps({'message': 'Helyes tipp, felvettelek a barátaim közé.', 'friends': friends}))
    else:
        response = Response(json.dumps({'message': "Sajnálom, nem jó a tipped."}), 400)
    
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


app.run(host='0.0.0.0', port=8080, debug=True)