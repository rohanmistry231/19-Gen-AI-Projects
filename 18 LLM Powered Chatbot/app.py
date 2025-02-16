from flask import Flask, render_template, request, jsonify
import os
from vertexai.preview.generative_models import GenerativeModel
from dotenv import load_dotenv
import vertexai

load_dotenv()

app = Flask(__name__)


project_id = os.getenv("project_id")
region = os.getenv("region")


#Authentication
vertexai.init(project= project_id, location= region)

model = GenerativeModel("gemini-1.0-pro")


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/gemini', methods=['GET', 'POST'])
def vertex_ai():
    user_input  = ""
    if request.method == 'GET':
        user_input = request.args.get('user_input')

    else:
        user_input = request.form('user_input')


    responses = model.generate_content(user_input, stream=True)

    res = [response.candidates[0].content.parts[0].text for response in responses]

    final_res = "".join(res)
    print(final_res)
    return jsonify(content=final_res)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)