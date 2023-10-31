from flask import Flask, jsonify
from minicheftracker import get_synapse_values
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_emissions', methods=['GET'])
def get_emissions():
    values = get_synapse_values()
    result_text = ""
    total_emissions = 140000
    for value in values:
        result_text += f"Monthly $SYN emissions on {value['network_name']}: {value['value']}<br>"
        total_emissions += float(value['value'].replace(',', ''))
    result_text += f"Total Monthly Emissions with 140,000 monthly bribes: {total_emissions:,.0f}"
    return result_text

if __name__ == '__main__':
    app.run(port=5000, debug=True)
