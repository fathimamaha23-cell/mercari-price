\# Mercari Price Prediction
## 🚀 Live Demo

Try the deployed application here: [Mercari Price Predictor](https://mercari-price-prediction-ycb6hayx4hjbnre58r8gmh.streamlit.app/)

**Source Code:** [GitHub Repository](https://github.com/eshagireesan/mercari-price-prediction)

Enter product details to receive an estimated selling price.


\## Project Overview

This project predicts the selling price of products listed on the Mercari marketplace using machine learning. It includes data exploration, preprocessing, feature engineering, model comparison, model evaluation, and a Streamlit web application for making predictions.



\## Objectives

\- Explore and clean the product listing dataset.

\- Handle missing values and engineer useful features.

\- Compare different regression models.

\- Evaluate model performance using MAE, RMSE, and R².

\- Interpret predictions using SHAP and LIME.

\- Save the trained model and use it for new predictions.

\- Provide an interactive interface using Streamlit.



\## Dataset

The project uses a 10,000-row sample of the Mercari price suggestion training dataset.



Features include product name, category, brand, item condition, shipping information, and item description. The target variable is `price`.



The raw dataset is not included in this repository.



\## Models Evaluated

\- Ridge Regression

\- Decision Tree Regressor

\- Random Forest Regressor

\- HistGradientBoosting Regressor



The selected model is a tuned HistGradientBoosting Regressor.



\## Model Performance



| Metric | Test Result |

|---|---:|

| MAE | 14.67 |

| RMSE | 29.73 |

| R² Score | 0.2342 |



These results are from the sampled dataset and test split. The model's performance may vary on other data.



\## Project Structure



```text

mercari-price-prediction/

├── 01\_Mercari\_EDA.ipynb

├── app/

│   └── app.py

├── models/

│   ├── mercari\_price\_model\_v1.joblib

│   └── model\_info.json

├── predict.py

├── requirements.txt

└── .gitignore

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/eshagireesan/mercari-price-prediction.git

cd mercari-price-prediction

```



Install the dependencies:



```bash

pip install -r requirements.txt

```



\## Run the Streamlit App



```bash

cd app

python -m streamlit run app.py

```



Enter the product details in the app to obtain an estimated price.



\## Batch Prediction



Place a `new\_listings.csv` file in the project root with the columns expected by `predict.py`, then run:



```bash

python predict.py

```



The script generates `predictions.csv`.



\## Tools and Technologies

\- Python

\- Pandas and NumPy

\- Scikit-learn

\- Matplotlib and Seaborn

\- SHAP and LIME

\- Joblib

\- Streamlit

\- Jupyter Notebook

\- Git and GitHub



\## Limitations

The model was trained on a sample of the dataset and does not use the product text features in the selected final model. Predictions are estimates, not guaranteed selling prices.



\## Author

Esha Gireesan



