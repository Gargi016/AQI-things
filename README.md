<p align="center">
  <img src="https://github.com/Gargi016/AQI-things/raw/main/docs/images/Project%20banner.png" alt="Project Banner">
</p>

<h1 align="center">AI-Powered Air Quality Index (AQI) Prediction</h1>
<p align="center">
  <i>A data-driven system to analyze and forecast air quality.</i>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
    <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
</p>

<p align="center">
  <a href="#-live-demo">Live Demo</a> •
  <a href="#-project-overview">Overview</a> •
  <a href="#-key-features">Key Features</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-getting-started">Getting Started</a>
</p>

---

## 🚀 Live Demo

[![Live Demo on Render](https://img.shields.io/badge/Live_Demo-Render-brightgreen?style=for-the-badge&logo=render)](https://aqi-things-1.onrender.com/)

**Click the badge above or follow this link to try the live application, hosted on Render:** [https://aqi-things-1.onrender.com/](https://aqi-things-1.onrender.com/)

---

## 📖 Project Overview

This project is an end-to-end data science application designed to analyze and predict the **Air Quality Index (AQI)**. Using a dataset of various atmospheric pollutants, this system employs the Prophet time-series forecasting model to predict future AQI levels, providing valuable insights into environmental health and pollution trends. The entire application is deployed as an interactive web service with a Flask back-end.

---

## ✨ Key Features

-  AI-Powered Forecasting: Utilizes the Prophet library to predict the AQI for the next 24 hours based on recent trends.

-  Interactive Map: A fully interactive Leaflet.js map allows users to click any location on the globe to get an instant AQI reading and forecast.

-  Dynamic UI: The background elegantly transitions between a day and night sky based on the user's local time, enhancing the user experience.

-  Detailed Data Visualization: Displays the current AQI on an animated gauge, breaks down key pollutants (PM₂.₅, O₃, NO₂), and shows the forecast on a clear Chart.js graph.

-  Responsive Design: A modern, two-column dashboard layout that works seamlessly on both desktop and mobile devices.



---
## ⚙️ How It Works

The application follows a simple but powerful full-stack architecture:

1.  **Front-End (Client):** The user interacts with the `index.html` page, either searching for a city or clicking on the map. This action triggers a JavaScript function.
2.  **API Request:** The JavaScript front-end sends a `fetch` request to the appropriate API endpoint on the Flask back-end (e.g., `/forecast/london` or `/forecast/geo/51.5/-0.12`).
3.  **Back-End (Server):** The Flask application receives the request.
    * It calls the external **WAQI API** to get real-time air quality data.
    * It simulates a 72-hour history based on the current AQI.
    * It feeds this historical data into the **Prophet model** to generate a 24-hour forecast.
4.  **API Response:** The Flask server packages the current data, pollutant info, and the forecast into a JSON object and sends it back to the front-end.
5.  **UI Update:** The front-end JavaScript receives the JSON data and dynamically updates the map, gauge, pollutant cards, and forecast chart.

---


## 🛠️ Tech Stack

This project was built using the following technologies:

| Python | Flask | Prophet | Pandas | JavaScript | Render |
| :---: | :---: | :---: | :---: | :---: | :---: |
| <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="48" height="48"/> | <img src="https://github.com/Gargi016/AQI-things/raw/main/docs/images/flask.jpeg" alt="flask" width="48" height="48"/> | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/facebook/facebook-original.svg" alt="prophet" width="48" height="48"/> | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" alt="pandas" width="48" height="48"/> | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="48" height="48"/> | <img src="https://github.com/Gargi016/AQI-things/raw/main/docs/images/render.jpeg" alt="render" width="48" height="48"/> |

---

## 🚀 Getting Started

<details>
<summary>Click here for instructions to run this project yourself.</summary>

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Gargi016/AQI-things.git](https://github.com/Gargi016/AQI-things.git)
    cd AQI-things
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Explore the Analysis**
    Open and run the Jupyter notebooks (`.ipynb` files) in the repository to see the full data analysis and model training process.

</details>

---

## 🤝 How to Contribute

Contributions are welcome! If you're interested in data science for environmental impact, please feel free to fork the repository and submit a pull request.

### Areas for Contribution
* **Data:** Integrate new data sources (e.g., weather data, traffic data) to improve model accuracy.
* **Model:** Experiment with different time-series models (like ARIMA or LSTMs) to compare performance against Prophet.
* **Front-End:** Enhance the interactivity of the Leaflet.js map or add new visualizations with Chart.js.
* **Back-End:** Optimize the Flask API for faster performance or add unit tests.

---

## 🔗 Connect with the Author

<p align="left">
<a href="https://github.com/Gargi016" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Gargi's Github" height="30" width="40" /></a>
<a href="http://www.linkedin.com/in/gargi-das-0026b331a" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="Gargi's LinkedIn" height="30" width="40" /></a>
</p>
