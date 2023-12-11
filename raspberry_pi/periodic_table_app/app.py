from flask import Flask, render_template
from database.database import * # Import the get_elements function from database.py

#include all necessary packages to get LEDs to work with Raspberry Pi
import time
import board
import neopixel

#Initialise a strips variable, provide the GPIO Data Pin
#utilised and the amount of LED Nodes on strip and brightness (0 to 1 value)
pixels1 = neopixel.NeoPixel(board.D18, 4, brightness=0.25)



app = Flask(__name__)

@app.route('/')
def home():
    pixels1.fill((0, 220, 0)) #Turn all leds on (RED)
    element_ids = get_element_ids()
    elements = get_elements()
    indexed_periodic_table = [(i, row) for i, row in enumerate(periodic_table)]
    #return render_template('periodic_table.html', periodic_table=indexed_periodic_table)
    return render_template('periodic_table.html', periodic_table=indexed_periodic_table, element_ids=element_ids)

@app.route('/led/<action>/<int:element_id>')
def led_action(action, element_id):
    if action == "on":
        pixels1[element_id] = (0, 20, 255)  # Set to desired color
    elif action == "off":
        pixels1[element_id] = (0, 0, 0)  # Turn off
    return 'OK', 200


@app.route('/led_on/<int:element_id>')
def led_on(element_id):
    print(f"Turning on LED for element ID: {element_id}")
    pixels1[element_id - 1] = (0, 20, 255) # Turn on the LED (Blue)
    return 'OK', 200

@app.route('/led_off/<int:element_id>')
def led_off(element_id):
    print(f"Turning off LED for element ID: {element_id}")
    pixels1[element_id - 1] = (0,0,0)  # Turn off the LED
    return 'OK', 200






if __name__ == '__main__':
    app.run(host='192.168.1.12', port=5000, debug=True)
    elements = get_elements()
    if elements:
        print(elements[0].keys())  # This will print the column names of the first element
