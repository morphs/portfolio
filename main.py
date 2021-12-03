from flask import Flask, jsonify, request

app = Flask(__name__)

msg = [
  { 'aboutus': "hate is the fuel of life." }
]


@app.route('/msg')
def get_msg():msg)


@app.route('/msg', methods=['POST'])
def add_income():
  msg.append(request.get_json())
  return '', 204
