import openai 
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', )
  

@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=5, size="256x256") 
  print(response)
  return jsonify(response)



app.run(host='0.0.0.0', debug= True, port=8080)