from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

response = []
# question_number = 0

@app.get("/")
def index():
    title = survey.title
    instructions = survey.instructions
    return render_template('survey_start.html', title=title, instructions=instructions)

@app.post("/begin")
def start_survey():
    
    return redirect("/questions/0")

@app.get("/questions/<int:question_number>")
def show_question(question_number):

    prompt = survey.questions[question_number].prompt
    choices = survey.questions[question_number].choices
    print("Redirect successful")
    return render_template('question.html', prompt=prompt, choices=choices)

@app.post("/answer")
def answer_question():
    answer = request.form.get("answer")
    print('answer', answer)
    response.append(answer)
    page_number = len(response)
    return redirect("/questions/")

