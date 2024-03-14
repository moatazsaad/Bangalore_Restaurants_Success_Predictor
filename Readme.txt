1- Overview:
This project aims to predict restaurant success in Bangalore, India, using a dataset scraped from Zomato website on 2020. It involves thorough exploratory data analysis (EDA) and machine learning (ML) to create a classification model. The project covers data cleaning, feature engineering, model training, and hyperparameter tuning.

2-Exploratory Data Analysis:
The EDA investigates various aspects, such as online orders, table booking, ratings, votes, location, cuisines, cost, and more. Visualizations and statistical analysis provide insights into restaurant popularity, cuisine distribution, pricing, and customer satisfaction.

3-Feature Engineering:
The project includes creating new features like cuisine and restaurant type counts, as well as encoding categorical features for ML. Business questions are answered through analysis, such as popular restaurants, top cuisines, expensive restaurant types, and restaurant density in different locations.

4-Data Preparation for Machine Learning:
Target variable creation, dropping unnecessary columns, handling missing values, and encoding categorical features prepare the data for ML. A target variable is defined, representing successful or unsuccessful restaurants.

5- Machine Learning:
Various ML models, including Logistic Regression, Decision Trees, Random Forests, K-Nearest Neighbors, and XGBoost are trained and compared using cross-validation. Hyperparameter tuning is performed using GridSearchCV to optimize the XGBoost model.

6- Model Deployment:
The best-performing model is deployed using Streamlit, allowing users to interact with the model and receive real-time predictions. 
The project is connected to Streamlit Cloud for wider accessibility.

7- Usage
You can interact with the deployed application on the cloud by visiting the following link:
(https://bangalorerestaurantssuccesspredictor-hiqbmzqrb9e69wmcctdbbk.streamlit.app/)

