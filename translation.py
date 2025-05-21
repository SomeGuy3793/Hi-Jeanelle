from flask import Flask, request, jsonify
import speech_recognition as sr
from translate import Translator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
r = sr.Recognizer()

@app.route('/translate', methods=['POST'])
def translate_speech():
    target_language = request.form.get('language', 'zh')  # Default to Chinese
    translator = Translator(provider='mymemory', to_lang=target_language)

    try:
        # Simulate speech recognition (replace with actual audio handling if needed)
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            recognized_text = r.recognize_sphinx(audio)

        # Translate the recognized text
        translation = translator.translate(recognized_text)
        return jsonify({"recognized_text": recognized_text, "translation": translation})
    except sr.UnknownValueError:
        return jsonify({"error": "Sphinx could not understand audio"}), 400
    except sr.RequestError as e:
        return jsonify({"error": f"Sphinx error: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)