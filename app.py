from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import python_minifier

app = Flask(__name__)
CORS(app)
CORS(
    app,
    resources={
        r"/*": {
            "origins": [
                "https://glad432.github.io",
                "http://localhost:3000",
                "https://python-minifier.vercel.app",
            ]
        }
    },
)

MAX_INPUT_SIZE_KB = 310


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        input_code = request.form.get("inputCode", "")

    if len(input_code.encode("utf-8")) > MAX_INPUT_SIZE_KB * 1024:
        return (
            jsonify({"error": f"exceeds the maximum limit of {MAX_INPUT_SIZE_KB} KB"}),
            400,
        )

        options = extract_options(request.form)
        try:
            minified_code = minify_code(input_code, options)
            return jsonify({"minified_code": minified_code})
        except Exception as e:
            return jsonify({"error": "Minification failed, check the py code"}), 500

    elif request.method == "GET":
        return render_template("out.html")


def extract_options(form_data):
    options = {}
    for key, value in form_data.items():
        if key != "inputCode":
            options[key] = value == "true"
    return options


@app.route("/minify", methods=["POST"])
def minify_post():
    input_code = request.form.get("inputCode", "")

    if len(input_code.encode("utf-8")) > MAX_INPUT_SIZE_KB * 1024:
        return (
            jsonify(
                {"error": f"size exceeds the maximum limit of {MAX_INPUT_SIZE_KB} KB"}
            ),
            400,
        )

    options = extract_options(request.form)
    try:
        minified_code = minify_code(input_code, options)
        return jsonify({"minified_code": minified_code})
    except Exception as e:
        return jsonify({"error": "Minification failed, check the py code"}), 500


def minify_code(input_code, options):
    try:
        minified_code = python_minifier.minify(input_code, **options)
        return minified_code
    except Exception as e:
        raise Exception("Minification failed, check the py code")


if __name__ == "__main__":
    app.run(debug=False)
