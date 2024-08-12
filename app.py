from flask import Flask, jsonify
from minicheftracker import get_synapse_values
from flask import render_template
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_emissions', methods=['GET'])
def get_emissions():
    values = get_synapse_values()
    result_text = ""
    total_emissions = 0
    error_occurred = False
    for value in values:
        if value['value'] == 'RPC error':
            error_occurred = True
        result_text += f"Monthly $SYN emissions on {value['network_name']}: {value['value']}<br>"
        if value['value'] != 'RPC error':
            total_emissions += float(value['value'].replace(',', ''))
    
    if not error_occurred:
        result_text += f"Total Monthly Emissions: {total_emissions:,.0f}"
    else:
        result_text += "Error occurred in retrieving some data."
    return result_text



if __name__ == '__main__':
    app.run(port=5000, debug=True)
