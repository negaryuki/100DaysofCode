from flask import Flask, request, render_template, send_file
from pathlib import Path
import openai
import os
import fitz

app = Flask(__name__)

# ---------Setup OpenAI Client-----------------
openai.api_key = 'KEY'


# ---------Set folder to store Uploads---------
UPLOAD_FOLDER = 'Uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# ---------Convert PDF to Text-----------------
def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''

    for page in doc:
        text += page.get_text()

    return text


# -----------------Application----------------
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        # Check if PDF was uploaded
        if 'file' not in request.files:
            return 'No file part found'

        file = request.files['file']
        if file.filename == '':
            return 'No file selected'

        # Save Uploaded PDF
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'],
                                file.filename)  # constructs directory e.g., Uploads/document.pdf
        file.save(pdf_path)  # saves uploaded file to the constructed directory

        # Convert PDF to Text
        text = pdf_to_text(pdf_path)

        # Convert Text To Speech using OpenAI API
        response = openai.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )

        # Save Audiobook File
        audiobook_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audiobook.mp3')

        with open(audiobook_path, 'wb') as file:
            file.write(response['data'])

        return render_template('index.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
