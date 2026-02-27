# 🎬 YouTube Engagement Revenue Optimizer

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange.svg)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-green.svg)

## 📌 Overview
The **YouTube Engagement AI Lab** is a full-stack data science and machine learning project designed to maximize YouTube's Average Revenue Per User (ARPU). By analyzing real-world interactions between users and recommended videos, this project predicts engagement probabilities and simulates strategic revenue lifts.

The project encompasses the entire data pipeline: from fetching and cleaning messy real-world data to building predictive models and deploying an interactive premium Streamlit dashboard.

## ✨ Features
*   **Automated Data Ingestion:** Uses `kagglehub` to dynamically pull the latest YouTube recommendation dataset.
*   **Robust Data Wrangling:** A comprehensive cleaning pipeline that handles mixed data types, out-of-bounds dates, and categorical inconsistencies (typos).
*   **Viewer Segmentation:** Utilizes **K-Means Clustering** to segment users into 'Surface Browsers', 'Casual Viewers', and 'Power Users' based on watch percentages and interaction density.
*   **Predictive Modeling:** Employs **Logistic Regression** to forecast the probability of high engagement (watch percentage > 50% or explicit 'likes') based on video parameters.
*   **Premium Interactive Dashboard:** A highly stylized, glassmorphism-themed Streamlit application that allows users to input video parameters and instantly visualize engagement probability, estimated views, and projected revenue.

## 🛠️ Technology Stack
*   **Language:** Python
*   **Data Manipulation:** Pandas, NumPy
*   **Machine Learning:** Scikit-Learn (K-Means, Logistic Regression)
*   **Data Visualization:** Plotly, Matplotlib, Seaborn
*   **Deployment:** Streamlit
*   **Data Sourcing:** KaggleHub

## 📊 Data Source
This project uses the **YouTube Recommendation Data (For Cleaning & ML)** dataset from Kaggle.
*   **Author:** iitanshravan
*   **Content:** Synthetic but highly realistic dataset containing user-video interactions deliberately injected with real-world data quality issues (typos, outliers, nulls) for robust pipeline testing.

## 🚀 How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Meet-6226/youtube-recommendation-ai.git
cd youtube-recommendation-ai
```

### 2. Install dependencies
Ensure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Run the Jupyter Notebook (Optional but Recommended)
Open `notebook.ipynb` to view the entire data science workflow. Running all cells will sequentially:
1. Download the Kaggle dataset.
2. Clean and preprocess the data.
3. Train the clustering and classification models.
4. Auto-generate the production `app.py` script.

### 4. Launch the Streamlit Dashboard
Run the following command in your terminal to start the AI Lab interface:
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`.

## 📂 Project Structure
```text
youtube-recommendation-ai/
│
├── notebook.ipynb       # Core data science workflow (Cleaning, EDA, ML, code generation)
├── app.py               # Auto-generated Streamlit dashboard script
├── requirements.txt     # Python package dependencies
├── notebook_update.json # Notebook state history backup
└── README.md            # Project documentation
```

## 💡 Key Business Insights
Based on the dashboard simulation:
*   **Algorithmic Recommendations** yield the highest probability boost (+18%) for content engagement.
*   **Educational Content on Mobile Devices** demonstrates the highest Return on Investment (ROI) and represents an optimal ad-placement segment.
*   Optimizing for engagements rather than raw clicks increases modeled revenue yield by conservatively 20% vs baseline metrics.

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).
