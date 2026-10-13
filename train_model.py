"""Train a tiny regression model on synthetic sample data."""
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

rng = np.random.default_rng(7)
hours = rng.uniform(0, 12, 200)
practice = rng.uniform(0, 10, 200)
noise = rng.normal(0, 5, 200)
score = np.clip(35 + hours * 4 + practice * 2.2 + noise, 0, 100)
X = np.column_stack((hours, practice))
model = LinearRegression().fit(X, score)
joblib.dump(model, "model.joblib")
print("Model trained and saved to model.joblib")
