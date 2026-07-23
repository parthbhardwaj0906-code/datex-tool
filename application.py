import os
from io import StringIO
from flask import Flask, render_template, request, jsonify, Response
import pandas as pd
from cleaner import clean

# Set explicit template directory path for Vercel
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
application = Flask(__name__, template_folder=template_dir)
app = application

@app.route("/")
def welcome():
    return render_template('home.html')

@app.route("/choose", methods=['POST', 'GET'])
def choose():
    if request.method == 'POST':
        m = request.form.get('missing_values')
        o = request.form.get('outliers')

        data = request.files.get('dataset')
        if not data or data.filename == '':
            return "Error: No file uploaded!", 400

        try:
            df = pd.read_csv(data)
        except Exception as e:
            return f"Error reading CSV file: {str(e)}", 400

        missing_dict = None
        outlier_dict = None

        if m:
            missing_dict = df.isna().sum().to_dict()

        if o:
            num_df = df.select_dtypes(include='number')
            outlier_dict = {}
            for col in num_df.columns:
                q1 = df[col].quantile(0.25)
                q3 = df[col].quantile(0.75)
                iqr = q3 - q1

                lower = q1 - (1.5 * iqr)
                upper = q3 + (1.5 * iqr)

                out = df[(df[col] < lower) | (df[col] > upper)]
                outlier_dict[col] = out[col].tolist()

        if not m and not o:
            return "Error: Please select at least one analysis option!", 400
        
        return render_template('results.html', missing_data=missing_dict, outlier_data=outlier_dict, filename=data.filename)

    return render_template('choice.html')

@app.route("/about")
def about_us():
    return render_template('about.html')

@app.route("/download", methods=['GET', 'POST'])
def download_file():
    if request.method == 'POST':
        file = request.files.get('file')

        if not file:
            return "No file selected", 400
        cleaned_data = clean(file)
        buffer = StringIO()
        cleaned_data.to_csv(buffer, index=False)
        buffer.seek(0)

        return Response(
            buffer.getvalue(),
            mimetype="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=datex_cleaned.csv",
                "Content-Type": "text/csv; charset=utf-8"
            }
        )
    
    # Correctly un-indented out of the POST block:
    return render_template('download.html')

@app.route('/thank')
def thank_user():
    return render_template('thank_you.html')

if __name__ == "__main__":
    app.run(debug=True)
