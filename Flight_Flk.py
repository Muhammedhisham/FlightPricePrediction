from flask import Flask, request, render_template
import pickle
# import sklearn
# print(sklearn.__version__)
# import pandas as pd
# Load the pickled model
with open(r'C:\Users\hisha\Desktop\Python\Flight_Price_Prediction\FPP.pkl', 'rb') as f:
    model = pickle.load(f)
# data=pd.read_csv('')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        airline = float(request.form['airline'])
        Wclass = float(request.form['Wclass'])
        Dcity = float(request.form['Dcity'])
        Atime = float(request.form['Atime'])
        Dtime = float(request.form['Dtime'])
        stop = float(request.form['stop'])
        Acity = float(request.form['Acity'])
        # print("sdsdtfhg***********************88",airline)
        prediction = model.predict([[airline, Wclass, Dcity, Atime, Dtime, stop, Acity]])
        prediction = int(prediction[0])
        print('prediction=', prediction)
        return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
