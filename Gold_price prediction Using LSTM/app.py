import streamlit as st
import pandas as pd
import numpy as np
import datetime
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px
import pickle

# -------------------------------
# Load trained model and scaler
# -------------------------------
model = load_model("gold_price_model.h5")

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

scaled_data = np.load("scaled_data.npy")

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Gold Price Predictor 2026",
    page_icon="💰",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
        }
        .main-title {
            font-size: 36px;
            color: #D4AF37;
            text-align: center;
            font-weight: bold;
        }
        .price-card {
            padding: 20px;
            border-radius: 15px;
            background: #fff8e1;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            text-align: center;
        }
        .price-value {
            font-size: 32px;
            font-weight: bold;
            color: #1a1a1a;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Title Section
# -------------------------------
st.markdown("<div class='main-title'>💰 Gold Price Prediction App - 2026</div>", unsafe_allow_html=True)
st.write("This app predicts **daily gold prices for 2026**. Select a date to see the exact price, or explore the chart below 📈.")

# -------------------------------
# Generate future predictions
# -------------------------------
last_60_days = scaled_data[-60:]
input_seq = last_60_days.reshape(1, -1)[0].tolist()

future_output = []
for _ in range(366):  # Leap year
    x_input = np.array(input_seq[-60:]).reshape(1, 60, 1)
    prediction = model.predict(x_input, verbose=0)
    input_seq.append(prediction[0][0])
    future_output.append(prediction[0][0])

future_prices = scaler.inverse_transform(np.array(future_output).reshape(-1, 1))
future_dates = pd.date_range(start="2026-01-01", periods=366)
future_df = pd.DataFrame({"Date": future_dates, "Predicted Price": future_prices.flatten()})

# -------------------------------
# Interactive Chart
# -------------------------------
fig = px.line(
    future_df, 
    x="Date", 
    y="Predicted Price", 
    title="📈 Predicted Gold Prices for 2026",
    template="plotly_dark"
)
fig.update_traces(line=dict(width=3, color="#D4AF37"))
fig.update_layout(
    title_x=0.5,
    font=dict(size=14),
    plot_bgcolor="#1a1a1a",
    paper_bgcolor="#1a1a1a"
)
st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Date Selector
# -------------------------------
selected_date = st.date_input(
    "📅 Select a date in 2026:",
    min_value=datetime.date(2026, 1, 1),
    max_value=datetime.date(2026, 12, 31),
)

# -------------------------------
# Show Predicted Price
# -------------------------------
if selected_date:
    price = future_df.loc[future_df["Date"] == pd.to_datetime(selected_date), "Predicted Price"].values[0]
    st.markdown(
        f"""
        <div class="price-card">
            <h4>Predicted Gold Price on <b>{selected_date}</b></h4>
            <div class="price-value">{price:.2f} USD</div>
        </div>
        """,
        unsafe_allow_html=True
    )
