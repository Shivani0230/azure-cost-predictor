 Azure Cost Predictor (Simulated)
📘 Introduction:
This project is a machine learning-based cost predictor for Azure resources — built without using any actual Azure subscription. It simulates cost data, trains a model, and provides a simple web interface to predict daily cloud costs.
Azure Cost Predictor is a simulated machine learning project that forecasts daily Azure cloud costs using synthetic data. It allows users to experiment with cost prediction without requiring an actual Azure subscription.
This project is ideal for:
- Learning cloud cost prediction modeling
- Practicing end-to-end ML workflows (from data to web app)
- Prototyping DevOps or FinOps dashboards

✅ No Azure subscription required — everything runs locally with synthetic data.

🧠 How It Works (Architecture):

1. Synthetic Data Generator 
   - `generate_data.py` creates daily Azure-like cost data over a 1-year period.
   - Adds natural fluctuations and patterns to simulate real billing trends.

2. Feature Engineering + Model Training
   - `train_model.py` processes dates, creates lag-based features, trains a Random Forest Regressor.
   - Outputs a serialized `.joblib` model in the `models/` folder.

3. Interactive Prediction Web App
   - `app.py` is a lightweight Streamlit app where users input date and past costs.
   - Predicts and displays the estimated Azure cost in real time.

4. No Azure Needed
   - Project is fully local with zero dependency on Azure APIs or cloud billing.

 🔧 Features:
- 📈 Simulated Azure cost data generation
- 🤖 Machine learning model (Random Forest) to predict cost
- 🧪 Interactive cost prediction via Streamlit app
- 📁 Organized project structure (scripts, models, data)
- 💾 Model saved using `joblib` for reuse

🗂️ Project Structure:
azure-cost-predictor/
├── app.py                     # Streamlit UI to predict cost
├── data/
│   └── simulated_cost_data.csv  # Auto-generated synthetic cost data
├── models/
│   └── cost_predictor.joblib    # Trained machine learning model
├── scripts/
│   ├── generate_data.py         # Script to generate synthetic Azure cost data
│   └── train_model.py           # Script to train ML model and save it
├── screenshots/
│   └── streamlit_app.png        # Screenshot of the web app (optional)
├── requirements.txt           # Project dependencies
└── README.md                  # Full project documentation

🔍 Description:
Component	Purpose
app.py	Runs the Streamlit web app for users to predict Azure costs
data/	Stores the generated synthetic dataset
models/	Stores the trained Random Forest model file
scripts/	Contains scripts to generate data and train the model
screenshots/	(Optional) Visuals for GitHub README or presentation
requirements.txt	Contains all dependencies used in the project
README.md	Detailed project description, usage, and structure


🛠️ Built With:
•	Python
•	pandas
•	scikit-learn
•	Streamlit
•	joblib


