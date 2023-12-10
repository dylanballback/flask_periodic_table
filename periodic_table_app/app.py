from flask import Flask, render_template
from database.database import get_elements # Import the get_elements function from database.py

app = Flask(__name__)

@app.route('/')
def home():
    elements = get_elements()  # Use the get_elements function to get the data
    return render_template('periodic_table.html', elements=elements)  # Pass the elements to the template

if __name__ == '__main__':
    app.run(debug=True)
