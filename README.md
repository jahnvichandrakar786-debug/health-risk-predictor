Health Risk Predictor 🏥
A Machine Learning application that predicts health risk levels based on user input metrics.
📌 Features
Interactive Web Interface built with Streamlit (app.py)
Machine Learning model trained in Jupyter Notebook (health_risk_predictor.ipynb)
Pre-trained model (health_risk_predictor.pkl) and label encoders (label_encoders.pkl) for quick deployment
📂 Project Structure
├── app.py                     # Streamlit application entry point
├── health_risk_predictor.ipynb # Notebook for EDA, preprocessing, and training
├── health_risk_predictor.pkl  # Saved machine learning model
└── label_encoders.pkl         # Saved encoders for categorical data
🛠️ Installation & Setup
Clone the repository:
git clone https://github.com/jahnvichandrakar786-debug/health-risk-predictor.git
cd health-risk-predictor
Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate
Install required dependencies:
pip install streamlit pandas numpy scikit-learn
Run the application:
streamlit run app.py
🚀 Usage
Launch the app via Streamlit, fill in the required health metrics in the web interface, and get an instant assessment of predicted health risk.
