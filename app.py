from flask import Flask, render_template
# Import your grade-fetching function here
from app import get_kreta_grades 

app = Flask(__name__)

@app.route('/')
def home():
    # Call your function to get the data
    my_grades = get_kreta_grades() 
    # Send the data to the HTML file
    return render_template('dsfa.html', grades=my_grades)

if __name__ == '__main__':
    app.run(debug=True)
html_content = f"<html><body><h1>My Grade: {grades[0]}</h1></body></html>"
with open("dsfa.html", "w") as f:
    f.write(html_content)