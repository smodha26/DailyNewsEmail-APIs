from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the weather data
weather_data = pd.read_csv('weather_data.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/weather')
def get_weather():
    day = request.args.get('day')
    month = request.args.get('month')
    year = request.args.get('year')

    if not day or not month or not year:
        return jsonify({'error': 'Date is incomplete. Please select day, month, and year.'}), 400

    # Filter the data for the selected date
    date_str = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    filtered_data = weather_data[weather_data['date'] == date_str]

    if filtered_data.empty:
        return jsonify({'error': 'No data available for the selected date.'}), 404

    weather_info = filtered_data.iloc[0].to_dict()
    return jsonify({
        'date': weather_info['date'],
        'temperature': weather_info['temperature'],
        'humidity': weather_info['humidity'],
        'condition': weather_info['condition']
    })

if __name__ == '__main__':
    app.run(debug=True)
