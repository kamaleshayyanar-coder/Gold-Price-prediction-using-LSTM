💰 Gold Price Prediction App 2026
A machine learning-powered web application that predicts daily gold prices for 2026 using deep learning models and time series analysis.

📋 Table of Contents
Overview
Features
Technology Stack
Installation
Usage
Project Structure
Model Details
Requirements
License
Author

🎯 Overview
This project leverages TensorFlow/Keras neural networks and time series forecasting techniques to predict gold prices throughout 2026. The application features an interactive web interface built with Streamlit, allowing users to visualize predictions and query specific dates.

Key Highlights
✅ Predicts 366 days of gold prices (leap year)
✅ Interactive date selector for specific price lookups
✅ Beautiful data visualizations with Plotly
✅ Pre-trained deep learning model
✅ Real-time price calculations

✨ Features
1. Interactive Dashboard
Clean, professional UI with gold-themed styling
Responsive layout optimized for all devices
Dark mode visualization for better readability
2. Price Predictions
Daily predictions for all 366 days of 2026
Sequence-based LSTM/RNN model for accurate forecasting
Normalized data using MinMaxScaler for optimal performance
3. Visualization Tools
Interactive line chart showing price trends
Date-based filtering and exploration
Plotly charts for enhanced interactivity
4. Date-Specific Lookup
Select any date in 2026 to view predicted gold price
Formatted price display in USD
Real-time calculations
🛠️ Technology Stack
Technology	Purpose
Python 3.8+	Programming language
Streamlit	Web application framework
TensorFlow/Keras	Deep learning model
Scikit-learn	Data preprocessing (MinMaxScaler)
Pandas	Data manipulation & analysis
NumPy	Numerical computations
Plotly	Interactive visualizations
Pickle	Model serialization

📦 Installation
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Step 1: Clone the Repository
git clone https://github.com/kamaleshayyanar-coder/gold-price-predictor.git
cd gold-price-predictor
Step 2: Create Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Verify Required Files
Ensure these files are in the project directory:

gold_price_model.h5 - Pre-trained Keras model
scaler.pkl - MinMaxScaler for data normalization
scaled_data.npy - Historical scaled price data
🚀 Usage
Running the Application
streamlit run app.py
The application will start and open in your default browser at http://localhost:8501

Using the App
View Chart: The main dashboard displays a continuous line chart of predicted gold prices for 2026
Select Date: Use the calendar widget to pick any date in 2026
View Price: The predicted gold price for that date appears below the chart
Explore Trends: Interact with the chart to zoom, pan, and identify patterns

📁 Project Structure
gold-price-predictor/
├── app.py                      # Main Streamlit application
├── gold_price_model.h5         # Pre-trained neural network model
├── scaler.pkl                  # MinMaxScaler for data preprocessing
├── scaled_data.npy             # Historical scaled price data
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore file

🧠 Model Details
Architecture
Model Type: Recurrent Neural Network (LSTM)
Input Sequence Length: 60 days of historical data
Output: Single-step prediction
Preprocessing: MinMax scaling (0-1 normalization)
Training Approach
Historical Data: Used past gold price data
Time Series: Sliding window approach with 60-day lookback period
Prediction Method: Sequential generation for 366 future days
Accuracy Considerations
Model based on historical patterns up to training date
External factors (geopolitical events, market sentiment) not captured
Use predictions as reference, not financial advice

📋 Requirements
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
tensorflow>=2.13.0
scikit-learn>=1.3.0
plotly>=5.17.0
Install all dependencies:

pip install -r requirements.txt

📊 Data Flow
Historical Data
      ↓
MinMaxScaler (Normalization)
      ↓
Last 60 Days (Input Sequence)
      ↓
LSTM Model (Sequential Prediction)
      ↓
Inverse Transform (De-normalization)
      ↓
Predicted Prices (2026)
      ↓
Streamlit Dashboard
🔒 File Descriptions
File	Description
app.py	Main application with UI and prediction logic
gold_price_model.h5	Trained Keras model (Binary HDF5 format)
scaler.pkl	Saved MinMaxScaler object for consistent preprocessing
scaled_data.npy	NumPy array of normalized historical prices

⚠️ Disclaimer
This application provides predictions based on historical patterns only. Gold prices are influenced by numerous factors including:

Economic indicators
Geopolitical events
Inflation rates
Currency fluctuations
Market sentiment
Do not use these predictions for financial decision-making without consulting financial advisors.

🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository
Create feature branches
Submit pull requests
Report issues and suggestions
📝 License
This project is open source and available under the MIT License.

👤 Author
Kamalesh Ayyanar A

GitHub: @kamaleshayyanar-coder
Final Year Project 2026
📧 Contact:kaqmalesha16122004@gmail.com
For questions, feedback, or suggestions, please reach out through GitHub issues or contact directly.

Last Updated: May 24, 2026

Made with ❤️ for gold price forecasting
