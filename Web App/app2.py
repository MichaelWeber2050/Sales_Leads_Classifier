from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(__name__)


with open("clf_catboost1.pkl", "rb") as f:
    clf_catboost1 = pickle.load(f)

@app.route('/') # the site to route to, index/main in this case
def load_page():
    return render_template("index.html")

@app.route('/input-page')
def load_input_page():
    return render_template("predictor.html", feature_names=['Supplies Subgroup', 'Supplies Group', 'Region', 'Route To Market',
       'Opportunity Amount USD', 'Client Size By Revenue',
       'Client Size By Employee Count', 'Revenue From Client Past Two Years',
       'Competitor Type', 'Deal Size Category'], x_input=[0]*10)

@app.route('/doing-stuff', methods=['Post'])
def in_process():
    x_input, predictions = make_prediction(request.args)
    return render_template("predictor_api.py", x_input=x_input,
                            feature_names=feature_names,
                            prediction=predictions)

if __name__ == '__main__':
    app.run(debug=True)
