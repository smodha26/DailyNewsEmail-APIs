# Weather Data API Project

## Overview

This project is a simple web application that displays weather information based on user-selected dates. The user selects a day, month, and year from dropdown menus, and the application retrieves and displays weather data for that date. The project showcases skills in working with APIs, Python backend development using Flask, and frontend development with HTML and JavaScript.

## Files

### 1. `main.py`

This is the main Python script for the project. It uses Flask to handle routing and serve the web application. Key functionalities include:

- **Routing**:
  - `/`: The root route that renders the `home.html` template.
  - `/api/weather`: An API route that processes the selected date, filters weather data from a CSV file, and returns the corresponding weather information as JSON.

- **Logic**:
  - Parses and validates the user input (day, month, year).
  - Filters weather data based on the selected date.
  - Returns weather details such as temperature, humidity, and other information.

### 2. `weather_data.csv`

This CSV file contains mock weather data that the application uses to respond to user queries. The data includes:

- **Columns**:
  - `date`: The date in `YYYY-MM-DD` format.
  - `temperature`: The temperature on that date.
  - `humidity`: The humidity percentage.
  - `condition`: The weather condition (e.g., sunny, cloudy).

- The file is read into a Pandas DataFrame in `main.py` to facilitate filtering based on the user's selected date.

### 3. `home.html`

This is the HTML file that serves as the frontend of the application. It contains:

- **User Interface**:
  - Three dropdown menus for selecting day, month, and year.
  - A submit button that triggers the weather data fetch based on the selected date.

- **JavaScript**:
  - A script that sends an API request to `/api/weather` with the selected date.
  - Handles responses by displaying the weather data or an error message if the date is incomplete or invalid.

### 4. `How to run the project`

   ```bash
   python main.py
   ```

### 5. `Don't forget to install required dependencies`

   ```bash
   pip install flask pandas
   ```
