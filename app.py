from flask import Flask, render_template
import requests

app = Flask(__name__)

# Mock function for now - replace with your real logic
def get_kreta_grades():
    # In a real scenario, this returns a list of dictionaries
    return [
        {"subject": "Digitalis kultura", "grade": 5},
        {"subject": "Matematika", "grade": 4}
    ]

@app.route('/')
def home():
    grades = get_kreta_grades()
    # This sends the 'grades' list to index2.html
    return render_template('index2.1.html', grades=grades)

if __name__ == '__main__':
    app.run(debug=True)