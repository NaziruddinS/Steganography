import os
from flask import Flask, render_template
from modes.Image.image import image
from modes.Audio.audio import audio
from modes.Text.text import text


UPLOAD_IMAGE_FOLDER = 'modes/Image/static'
IMAGE_CACHE_FOLDER = 'modes/Image/__pycache__'
UPLOAD_TEXT_FOLDER = 'modes/Text/static'
TEXT_CACHE_FOLDER = 'modes/Text/__pycache__'
UPLOAD_AUDIO_FOLDER = 'modes/Audio/static'
AUDIO_CACHE_FOLDER = 'modes/Audio/__pycache__'


# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'hello')
app.config['UPLOAD_IMAGE_FOLDER'] = UPLOAD_IMAGE_FOLDER
app.config['IMAGE_CACHE_FOLDER'] = IMAGE_CACHE_FOLDER
app.config['UPLOAD_TEXT_FOLDER'] = UPLOAD_TEXT_FOLDER
app.config['TEXT_CACHE_FOLDER'] = TEXT_CACHE_FOLDER
app.config['UPLOAD_AUDIO_FOLDER'] = UPLOAD_AUDIO_FOLDER
app.config['AUDIO_CACHE_FOLDER'] = AUDIO_CACHE_FOLDER
app.register_blueprint(image, url_prefix="/image")
app.register_blueprint(audio, url_prefix="/audio")
app.register_blueprint(text, url_prefix="/text")

@app.route("/")
def home():
    return render_template("home.html")

# Vercel entry point
def handler(environ, start_response):
    return app(environ, start_response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)