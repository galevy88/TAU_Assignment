from flask import Flask, render_template, request
import plotly
import json
from plotly_module import plot_brain_areas_by_name  # Ensure this is correctly importing
from helpers import get_dicts

brain_areas, brain_area_colors = get_dicts()

app = Flask(__name__)


@app.route('/')
def index():
    # Pass brain_areas dict to the template
    return render_template('index.html', brain_areas=brain_areas)


@app.route('/plot', methods=['GET'])
def plot():
    # Fetch parameters from form submission
    area_name = request.args.get('area_name', 'All')
    mode = request.args.get('mode', 'color')
    color_sub = request.args.get('color_sub', 'false').lower() == 'true'

    # Call the plotting function and pass parameters
    fig = plot_brain_areas_by_name(area_name, mode, color_sub)  # This needs to return a figure

    # Convert the figure to JSON for rendering
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('plot.html', graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(debug=True)
