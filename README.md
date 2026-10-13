# PredictLab — Beginner MLOps / DevOps Demo

A small learning project connecting basic machine learning with application serving and DevOps practices.

## What it does
- Generates synthetic sample data and trains a simple Linear Regression model.
- Saves the model as `model.joblib`.
- Serves predictions through a Flask web page.
- Uses Docker and Docker Compose to package and run the app.
- Uses GitHub Actions to install dependencies, train the model, run tests, and build a Docker image.

> Important: The data is synthetic and the score is illustrative only. This is not a validated model and should not be used for real decisions. The project does not deploy to AWS or publish a Docker image automatically.

## Run with Docker
```bash
docker compose up -d --build
```
Open http://localhost:5000

Check the container and logs:
```bash
docker compose ps
docker compose logs
```
Stop:
```bash
docker compose down
```

## Run locally without Docker
```bash
python -m venv .venv
# Linux/macOS:
source .venv/bin/activate
# Windows PowerShell:
# .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python train_model.py
python app.py
```
Open http://localhost:5000

Run tests:
```bash
pytest -q
```

## DevOps workflow
Developer pushes code to GitHub -> GitHub Actions installs dependencies -> trains the sample model -> runs tests -> builds the Docker image.

## Resume project entry — only after you run and verify it
**Containerized Machine Learning Prediction App | Python, Flask, Scikit-learn, Docker, Docker Compose, GitHub Actions**
- Trained a basic regression model on synthetic data and served sample predictions through a Flask web interface.
- Packaged the application and model-training step in Docker; used Docker Compose for consistent local execution.
- Automated dependency installation, model training, test execution, and Docker image builds using GitHub Actions.

## Future improvements
- Use a real, appropriately licensed dataset and evaluate model quality.
- Add model metrics and structured application logging.
- Deploy to AWS only after practicing IAM, networking, security, and cost controls.
- Add monitoring for application health and resource usage.
