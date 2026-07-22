from flask import Flask, render_template, request, jsonify
import pandas as pd

application = Flask(__name__)
app = application

@app.route("/")
def welcome():
    return render_template('home.html')

@app.route("/index", methods = ['POST', 'GET'])
def choose():
    if request.method == 'POST':
       m = request.form.get('missing_values')
       o = request.form.get('outliers')

       data = request.files.get('dataset')
       if not data:
            return "Error: No file uploaded!", 400

       df = pd.read_csv(data)
       if m:
           missing = df.isna().sum().to_dict()
           return f"The number of missing values in {data} is {missing}"
       if o:
           num_df = df.select_dtypes(include = 'number')
           num_cols = num_df.columns
           
           dict1 = {}
           for col in num_cols:
               q1 = df[col].quantile(0.25)
               q3 = df[col].quantile(0.75)
               iqr = q3-q1

               lower = q1 - (1.5*iqr)
               upper = q3 + (1.5*iqr)

               out = df[(df[col] < lower) | (df[col] > upper)]
               dict1[col] = out[col].to_list()
           return render_template('results.html', outlier_data = dict1)
       return "Error: Please select at least one analysis option (Missing Values or Outliers)!"
           
    else:
        return render_template('choice.html')


if __name__ == "__main__":
    app.run(debug = True)