import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
from lime.lime_tabular import LimeTabularExplainer
import matplotlib.pyplot as plt
import os


class MLModelTrainer:
    def __init__(self, df):
        self.df = df[df['totalclaims'] > 0].copy()
        self.models = {}
        self.results = []
        self.X_train = self.X_test = self.y_train = self.y_test = None
        os.makedirs("models", exist_ok=True)
        os.makedirs("reports", exist_ok=True)
        os.makedirs("plots", exist_ok=True)

    def prepare_features(self):
        df = self.df
        df['vehicle_age'] = 2015 - df['registrationyear']
        df['postcode_claim_freq'] = df.groupby('postalcode')['totalclaims'].transform(lambda x: (x > 0).mean())

        used_features = [
            'province', 'postalcode', 'gender', 'vehicletype', 'cubiccapacity',
            'registrationyear', 'covertype', 'maritalstatus', 'suminsured',
            'vehicle_age', 'postcode_claim_freq'
        ]

        cat_features = ['province', 'gender', 'vehicletype', 'covertype', 'maritalstatus']
        num_features = ['postalcode', 'cubiccapacity', 'registrationyear', 'suminsured', 'vehicle_age', 'postcode_claim_freq']

        for col in cat_features:
            df[col] = df[col].fillna(df[col].mode()[0]).str.strip().replace('', df[col].mode()[0])
        for col in num_features:
            df[col] = df[col].fillna(df[col].median())

        postcode_means = df.groupby('postalcode')['totalclaims'].mean()
        df['postalcode_encoded'] = df['postalcode'].map(postcode_means).fillna(postcode_means.mean())

        df = pd.get_dummies(df, columns=cat_features, drop_first=True)

        X = df.drop(columns=['totalclaims'])
        y = np.log1p(df['totalclaims'])

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print(f"Train shape: {self.X_train.shape}, Test shape: {self.X_test.shape}")

    def train_models(self):
        self.models = {
            'LinearRegression': LinearRegression(),
            'RandomForest': RandomForestRegressor(n_estimators=100, random_state=42),
            'XGBoost': XGBRegressor(n_estimators=100, random_state=42)
        }
        for name, model in self.models.items():
            model.fit(self.X_train, self.y_train)
            print(f"Trained: {name}")

    def evaluate(self):
        for name, model in self.models.items():
            pred = np.expm1(model.predict(self.X_test))
            true = np.expm1(self.y_test)
            rmse = np.sqrt(mean_squared_error(true, pred))
            r2 = r2_score(true, pred)
            self.results.append({"Model": name, "RMSE": rmse, "R2": r2})
            print(f"{name}: RMSE = {rmse:.2f}, R2 = {r2:.4f}")
        pd.DataFrame(self.results).to_csv("reports/model_evaluation.csv", index=False)

    def explain_with_lime(self, model_name='XGBoost'):
        model = self.models[model_name]
        explainer = LimeTabularExplainer(
            training_data=self.X_train.values,
            feature_names=self.X_train.columns.tolist(),
            mode='regression'
        )
        exp = explainer.explain_instance(self.X_test.iloc[0].values, model.predict, num_features=10)
        exp.save_to_file('plots/lime_explanation.html')
        print("Saved LIME explanation for one instance to 'plots/lime_explanation.html'")
