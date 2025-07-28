
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS


import requests
import pandas as pd
from datetime import datetime, timedelta


from prophet import Prophet


import random
import logging
import os


app = Flask(__name__)
CORS(app) 
logging.getLogger('prophet').setLevel(logging.ERROR)
logging.getLogger('cmdstanpy').setLevel(logging.ERROR)


API_KEY = "6bd1df1634a84e8b9ea3281d82d1f870b3ed3c8c"





def generate_simulated_data(current_aqi, hours=72):
    """
    Generates a DataFrame of simulated historical AQI data for the last 72 hours.
    The WAQI API does not provide free historical data, so we simulate it.
    """
    timestamps = [datetime.utcnow() - timedelta(hours=i) for i in range(hours, -1, -1)]
  
    values = [max(0, current_aqi + random.randint(-25, 25) - int(5 * (i % 24 - 12))) for i in range(hours + 1)]
    df = pd.DataFrame({"ds": timestamps, "y": values})
    return df.sort_values("ds")

def format_dataframe_for_json(df, columns):
    """
    Converts specific columns of a Pandas DataFrame into a JSON-serializable dictionary.
    """
    data = {"labels": df["ds"].dt.strftime('%Y-%m-%d %H:%M:%S').tolist()}
    for col in columns:
       
        data[col] = [round(v, 2) if pd.notna(v) else None for v in df[col].tolist()]
    return data



@app.route("/forecast/<city>")
def get_aqi_forecast_by_city(city):
    """API endpoint to get AQI data for a named city."""
    try:
        print(f"🔄 Received request for city: {city.title()}...")
        url = f"https://api.waqi.info/feed/{city}/?token={API_KEY}"
        response = requests.get(url)
        return process_waqi_response(response)
    except Exception as e:
        print(f"🚨 An unexpected error occurred: {e}")
        return jsonify({"status": "error", "message": "An internal server error occurred."}), 500

@app.route("/forecast/geo/<lat>/<lon>")
def get_aqi_forecast_by_geo(lat, lon):
    """API endpoint to get AQI data using latitude and longitude."""
    try:
        print(f"🔄 Received request for geo: {lat}, {lon}...")
        url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={API_KEY}"
        response = requests.get(url)
        return process_waqi_response(response)
    except Exception as e:
        print(f"🚨 An unexpected error occurred: {e}")
        return jsonify({"status": "error", "message": "An internal server error occurred."}), 500

def process_waqi_response(response):
    """
    Processes a response from the WAQI API, runs a forecast, and returns the
    complete data packet. This function is used by both city and geo endpoints.
    """
    api_data = response.json()

  
    if api_data.get("status") != "ok" or "aqi" not in api_data.get("data", {}):
        return jsonify({"status": "error", "message": "Could not find AQI data for this location."}), 404

    
    data_payload = api_data["data"]
    current_aqi = data_payload["aqi"]
    pollutants = data_payload.get("iaqi", {})
    df_simulated = generate_simulated_data(current_aqi)

    if df_simulated.shape[0] < 2:
        return jsonify({"status": "error", "message": "Not enough historical data to create a forecast."}), 500

   
    model = Prophet(daily_seasonality=True, yearly_seasonality=False, weekly_seasonality=False)
    model.fit(df_simulated)
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    
   
    response_data = {
        "status": "ok",
        "city": data_payload["city"], 
        "current_aqi": current_aqi,
        "pollutants": {k: v.get('v') for k, v in pollutants.items()},
        "history": format_dataframe_for_json(df_simulated, ["y"]),
        "forecast": format_dataframe_for_json(forecast[forecast['ds'] > df_simulated['ds'].max()], ["yhat", "yhat_lower", "yhat_upper"]),
        "timestamp": datetime.now().isoformat()
    }
    
    print(f"✅ Successfully generated forecast for {data_payload['city']['name']}.")
    return jsonify(response_data)



@app.route('/')
def serve_index():
    """Serves the main index.html file."""
    return send_from_directory('.', 'index.html')

@app.errorhandler(404)
def not_found(e):
    """Serves index.html for any route not found (for single-page apps)."""
    return send_from_directory('.', 'index.html')

