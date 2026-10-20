# Mercari Price Prediction

## 🚀 Live Demo

Try the deployed application here: [Mercari Price Predictor](https://mercari-price-5xer7zpatqjd8hjxucm4dq.streamlit.app/)

**Source Code:** [GitHub Repository](https://github.com/fathimamaha23-cell/mercari-price)

Enter product details to receive an estimated selling price.

## 📌 Project Overview

This project predicts the selling prices of products listed on the Mercari marketplace using machine learning. It includes data exploration, preprocessing, feature engineering, model comparison, model evaluation, and a Streamlit web application for making predictions.

## 🎯 Objectives

- Explore and clean the product listing dataset.
- Handle missing values and engineer useful features.
- Compare different regression models.
- Evaluate model performance using MAE, RMSE, and R².
- Interpret predictions using SHAP and LIME.
- Save the trained model and use it for new predictions.
- Develop an interactive web application using Streamlit.

## 📊 Dataset

The project uses a 10,000-row sample of the Mercari price suggestion training dataset.

The features include:

- Product name
- Product category
- Brand
- Item condition
- Shipping information
- Item description

The target variable is `price`.

**Note:** The raw dataset is not included in this repository.

## 🤖 Models Evaluated

The following regression models were evaluated:

- Ridge Regression
- Decision Tree Regressor
- Random Forest Regressor
- HistGradientBoosting Regressor

The selected model is a tuned HistGradientBoosting Regressor.

## 📈 Model Performance

The model was evaluated on a test split using the following metrics:

| Metric | Test Result |
|---|---:|
| MAE | 14.67 |
| RMSE | 29.73 |
| R² Score | 0.2342 |

These results are based on the sampled dataset and test split. Performance may vary on other datasets.

## 📁 Project Structure

```text
mercari-price/
├── 01_Mercari_EDA.ipynb
├── app/
│   └── app.py
├── models/
│   ├── mercari_price_model_v1.joblib
│   └── model_info.json
├── predict.py
├── requirements.txt
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/fathimamaha23-cell/mercari-price.git
cd mercari-price
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Streamlit Application

From the project root directory, run:

```bash
python -m streamlit run app/app.py
```

The application will open in your browser. Enter the product details to obtain an estimated selling price.

## 📦 Batch Prediction

The project also supports batch predictions using a CSV file.

1. Place a file named `new_listings.csv` in the project root.
2. Include the columns expected by `predict.py`.
3. Run the following command:

```bash
python predict.py
```

The script generates a file named `predictions.csv`.

## 🛠️ Tools and Technologies

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib, Seaborn
- **Model Explainability:** SHAP, LIME
- **Model Serialization:** Joblib
- **Web Application:** Streamlit
- **Development Environment:** Jupyter Notebook
- **Version Control:** Git and GitHub

## ⚠️ Limitations

- The model was trained on a sample of the dataset.
- The selected final model does not use product text features.
- Predictions are estimates and are not guaranteed selling prices.
- Model performance may vary for products with different characteristics or price distributions.

## 👩‍💻 Author

Fathima Maha

