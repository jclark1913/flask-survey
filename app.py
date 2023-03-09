from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

response = []


@app.get("/")
def index():
    title = survey.title
    instructions = survey.instructions
    return render_template('survey_start.html', title=title, instructions=instructions)

@app.post("/begin")
def start_survey():
    question_number = 0
    return redirect("/questions")

@app.route("/questions")
def show_question():
    prompt = survey.questions[0].prompt
    choices = survey.questions[0].choices
    print("Redirect successful")
    return render_template('question.html', prompt=prompt, choices=choices)

# @app.post("/answer")
# def answer_question():
