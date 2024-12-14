from flask import Flask, render_template, request, redirect, url_for
import os
import pandas as pd
from ocr_engine import extract_text

app = Flask(__name__)
UPLOAD_FOLDER = 'receipts'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Save the uploaded file
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Perform OCR
            text = extract_text(filepath)

            # Save extracted data to CSV
            output_file = os.path.join(OUTPUT_FOLDER, 'extracted_data.csv')
            data = {'Filename': [file.filename], 'Extracted Text': [text]}
            df = pd.DataFrame(data)
            df.to_csv(output_file, mode='a', index=False, header=not os.path.exists(output_file))

            return render_template('index.html', text=text)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
