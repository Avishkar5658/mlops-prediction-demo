from flask import Flask, request, render_template_string
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.joblib")

PAGE = """
<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PredictLab | ML Demo</title>
<style>
:root{--navy:#132238;--blue:#3a67f2;--mint:#dff8ed;--ink:#172435;--muted:#657386}
*{box-sizing:border-box}body{margin:0;background:#f4f7fb;color:var(--ink);font-family:Arial,sans-serif}
header{background:linear-gradient(120deg,#132238,#254c78);color:#fff;padding:38px 22px}
.wrap{max-width:980px;margin:auto}header .tag{font-size:11px;letter-spacing:2px;color:#bcebd8;font-weight:bold}
h1{font-size:clamp(30px,5vw,48px);margin:12px 0}header p{color:#d7e4f2;max-width:650px;line-height:1.6}
main{max-width:980px;margin:28px auto;padding:0 18px;display:grid;grid-template-columns:1.1fr .9fr;gap:18px}
.card{background:#fff;border:1px solid #e2e9f1;border-radius:18px;padding:24px;box-shadow:0 8px 25px #18314b0a}
h2{margin:0 0 8px;font-size:21px}.sub{font-size:13px;color:var(--muted);line-height:1.6}
label{display:block;margin:18px 0 7px;font-size:13px;font-weight:bold}
input{width:100%;padding:13px;border:1px solid #d7e0eb;border-radius:10px;font-size:15px}
button{margin-top:18px;width:100%;border:0;border-radius:10px;padding:14px;background:var(--blue);color:white;font-weight:bold;font-size:15px;cursor:pointer}
.result{background:var(--mint);border:1px solid #b9ebd5;border-radius:14px;padding:18px;margin-top:20px}
.pred{font-size:30px;color:#126342;font-weight:bold;margin:8px 0}.badge{display:inline-block;background:#edf2ff;color:#3558bb;padding:7px 10px;border-radius:20px;font-size:11px;font-weight:bold}
.steps{display:grid;gap:10px;margin-top:18px}.step{padding:13px;border:1px solid #e5ebf2;border-radius:12px;font-size:13px}.step strong{display:block;margin-bottom:4px}.foot{max-width:980px;margin:0 auto;padding:0 18px 30px;color:var(--muted);font-size:12px}
@media(max-width:720px){main{grid-template-columns:1fr}header{padding-top:28px}}
</style></head><body>
<header><div class="wrap"><div class="tag">PREDICTLAB · MACHINE LEARNING DEMO</div>
<h1>Turn sample data into a prediction.</h1><p>A beginner-friendly example of a trained machine learning model served through a Python web application—with Docker and CI automation.</p></div></header>
<main><section class="card"><span class="badge">LIVE LOCAL DEMO</span><h2 style="margin-top:14px">Try a prediction</h2>
<p class="sub">Enter two numeric inputs. This demo uses a small sample model trained on synthetic data, not a real-world business dataset.</p>
<form method="post"><label for="hours">Study hours (0–12)</label><input id="hours" name="hours" type="number" min="0" max="12" step="0.5" value="{{ hours }}" required>
<label for="practice">Practice tests completed (0–10)</label><input id="practice" name="practice" type="number" min="0" max="10" step="1" value="{{ practice }}" required>
<button type="submit">Generate prediction</button></form>
{% if prediction is not none %}<div class="result"><div class="sub">Sample model prediction</div><div class="pred">{{ prediction }} / 100</div><div class="sub">Illustrative score only; not a validated prediction for actual students.</div></div>{% endif %}
</section><aside class="card"><h2>How the workflow works</h2><p class="sub">From model training to serving predictions.</p><div class="steps">
<div class="step"><strong>01 · Data preparation</strong>Generate and prepare a small sample dataset.</div>
<div class="step"><strong>02 · Model training</strong>Train a regression model and save it as <code>model.joblib</code>.</div>
<div class="step"><strong>03 · Model serving</strong>Flask loads the saved model and returns a prediction.</div>
<div class="step"><strong>04 · DevOps packaging</strong>Docker packages the app; GitHub Actions runs checks and builds the image.</div>
</div></aside></main><div class="foot">Learning project · Synthetic sample data · No external prediction API</div></body></html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    hours = request.form.get("hours", "5")
    practice = request.form.get("practice", "3")
    if request.method == "POST":
        try:
            h, p = float(hours), float(practice)
            if not (0 <= h <= 12 and 0 <= p <= 10):
                raise ValueError("Input outside allowed range")
            prediction = round(float(model.predict(np.array([[h, p]]))[0]), 1)
        except (ValueError, TypeError):
            prediction = None
    return render_template_string(PAGE, prediction=prediction, hours=hours, practice=practice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
