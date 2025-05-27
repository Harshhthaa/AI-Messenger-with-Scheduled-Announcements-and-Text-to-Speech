from flask import Flask, render_template, request, jsonify
import pyttsx3
import datetime
import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234@localhost/radio'
db = SQLAlchemy(app)

'''print("database connected!")

name = "D Shanti Priya"
empid = 10644'''

def text_to_speech(class_name, content):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(f"Class {class_name}. {content}")
    engine.runAndWait()

@app.route('/')
def index():
    return render_template('frontPage.html')           

@app.route('/process_data', methods=['POST'])
def process_data():
    if request.method == 'POST':
        # Get data from HTML form
        class_name = request.form.get('class')
        content = request.form.get('content')
        timings = request.form.get('time')

        print("class_name:", class_name)
        print("content:", content)
        print("timings:", timings)

        # Wait until the target time
        wait_until_target_time(timings)

        # Perform text-to-speech
        text_to_speech(class_name, content)

        # Perform the show content
        store_content(class_name, content, timings)

        return render_template('app-container.html')

'''

def validate(name,empid):
    flag = False
    s1 = text("select * from faculty_confirmation")
    db.session.execute(s1)
    print(s1)

validate(name,empid)
'''
def wait_until_target_time(target_time_str):
    if target_time_str is None:
        print("Timings not provided.")
        return

    try:
        target_time = datetime.datetime.strptime(target_time_str, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Please provide time in the format 'HH:MM'")
        return

    while True:
        current_time = datetime.datetime.now().time()
        if current_time >= target_time:
            break
        time.sleep(1)



def store_content(class_name,content,timings):
    sql_query = text("INSERT INTO content (class_name, content, timings) VALUES (:class_name, :content,:timings)")
    db.session.execute(sql_query, {"class_name": class_name, "content": content, "timings": timings})
    db.session.commit()

@app.route('/show_schedule')
def show_schedule():
    schedule_data = content.query.all()

    return render_template('frontend.html',schedule_data=schedule_data)
    

if __name__ == '__main__':
    app.run(debug=True)
