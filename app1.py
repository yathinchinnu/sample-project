from flask import Flask, request, render_template
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler 
model = pickle.load(open('cardiac_arrest_prediction_model.pkl', 'rb'))
app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            age = float(request.form['age'])
            gender = int(request.form['gender'])
            smoking = int(request.form['smoking'])
            hypertension = int(request.form['hypertension'])
            stroke = int(request.form['stroke'])
            ap_hi = float(request.form['ap_hi'])
            ap_lo = float(request.form['ap_lo'])
            bmi = float(request.form['bmi'])
            hr = float(request.form['hr'])
            glucose = float(request.form['glucose'])
            input_data = np.array([[gender, age, smoking, stroke, hypertension, ap_hi, ap_lo, bmi, hr, glucose]])
            prediction = model.predict(input_data)
            if prediction[0] == 1:
                statement = "Cardiac arrest may occur."
                color = "red"
            else:
                statement = "Cardiac arrest may not occur."
                color = "green"
            return render_template('prediction.html', prediction=statement, colour=color)
        except Exception as e:
            return f"Error: {str(e)}"
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)
