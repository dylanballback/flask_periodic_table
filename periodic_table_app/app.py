from flask import Flask, render_template
from database.database import * # Import the get_elements function from database.py

app = Flask(__name__)

@app.route('/')
def home():
    elements = get_elements()
    indexed_periodic_table = [(i, row) for i, row in enumerate(periodic_table)]
    return render_template('periodic_table.html', periodic_table=indexed_periodic_table)

if __name__ == '__main__':
    app.run(debug=True)
    elements = get_elements()
    if elements:
        print(elements[0].keys())  # This will print the column names of the first element
