from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route('/')
def home():
    # Fetch data from external site
    response = requests.get('[api.example.com](https://api.example.com/data)')
    data = response.json()  # or response.text for raw HTML
    
    # Pass it to your HTML template
    return render_template('index.html', data=data)
if __name__ == '__main__':
    app.run(debug=True)