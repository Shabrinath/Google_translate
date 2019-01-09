from flask import Flask, jsonify, request, json
import json, requests
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route('/translate', methods=['POST'])
def kube():
    responseFromDialogflow = request.get_json()
    response1 = json.dumps(responseFromDialogflow)
    response_json = json.loads(response1)
    Users_response = response_json['queryResult']['parameters']['text']
    Users_response_only = Users_response[0]
    print Users_response_only
    url = "https://translation.googleapis.com/language/translate/v2"

    payload = "{\r\n \"format\": \"text\",\r\n \"source\": \"en\",\r\n \"target\": \"te\",\r\n \"q\": [\r\n  \""+Users_response_only+"\"\r\n ]\r\n}"

    headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer ya29.GluMBu0x-biODTudSQgJB6VijLSts6WZnUwFNu4RMb8hGIgTxh-jR5jRdvmqDJoNyQcl5cGayjg9r_EeeH-dSvoAimPuU9N2aDRKRlREd5zOlgZlNf38-WB3ygT0",
    'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    Target_Json = response.text
    Target_text = Target_Json[71:75]
    print Target_text

    return jsonify ({
             "payload": {
    "webhook": {
      "text": "translation is successful by shabari's translation app "
    }
  },
  "fulfillmentText": Target_text,
  "source": "webhook"
}), 201

if __name__ == '__main__':
    app.run(host="10.0.0.31", debug=True, port=8080)
