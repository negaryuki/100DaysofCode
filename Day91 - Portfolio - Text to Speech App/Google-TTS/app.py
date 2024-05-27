from flask import Flask, request, render_template, send_file
from pathlib import Path
from gtts import gTTS
import os
import fitz

app = Flask(__name__)

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


def text_to_speech(text, audio_path):
    tts = gTTS(text=text, lang='en')
    tts.save(audio_path)


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
        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(pdf_path)  # saves uploaded file to the constructed directory

        # Convert PDF to Text
        text = pdf_to_text(pdf_path)

        # Save Audiobook File
        audiobook_path = os.path.join(app.config['UPLOAD_FOLDER'], 'audiobook.mp3')

        # Convert Text To Speech using Google
        text_to_speech(text, audiobook_path)

        return send_file(audiobook_path, as_attachment=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
