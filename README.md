# Python Minifier API

## Overview:

This repository contains a Flask-based web API for minifying Python code using the [python_minifier](https://pypi.org/project/python-minifier/) library. The API allows users to submit Python code snippets and receive the minified version in response. Additionally, it supports CORS to enable cross-origin requests from specified origins.

## Setup:

To set up the Python Minifier Web API, follow these steps:

1. Clone this repository to your local machine
    ```
    https://github.com/glad432/python-minifier-flask.git
    ```
2. Navigate into the cloned repository directory
    ```
    cd python-minifier-flask
    ```
3. Install the required dependencies listed in `requirements.txt` using pip:
    ```
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```
    python app.py
    ```
5. The application should now be running locally.

### Endpoints:

- `POST /`: Accepts a Python code snippet via a form submission and returns the minified version of the code.
- `POST /minify`: Alternative endpoint for minification, accepting Python code snippet via form submission.
- `GET /`: Renders an HTML page.

### CORS Configuration:

Cross-Origin Resource Sharing (CORS) is configured to allow requests from the following origins:

For example:
- https://glad432.github.io

## Dependencies:

- Flask: A lightweight WSGI web application framework for Python.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.
- Python_minifier: Minifies Python source code, reducing it to its smallest form.

## Contributing:

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
