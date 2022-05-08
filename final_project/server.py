import flask
from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.english_to_french(textToTranslate)
    if french_text == None:
        return "Text is empty"
    else:
        return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.french_to_english(textToTranslate)
    if english_text == None:
        return "Text is empty"
    else:
        return english_text

@app.route("/")
def renderIndexPage():
    # Render template
    return flask.render_template("index.html", template_folder='templates')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
