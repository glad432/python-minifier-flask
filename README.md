# Python Minifier API

## Overview:

This repository contains a Flask-based web API for minifying Python code using the [python_minifier](https://pypi.org/project/python-minifier/) library. The API allows users to submit Python code snippets and receive the minified version in response. Additionally, it supports CORS to enable cross-origin requests from specified origins.

## Setup:

To set up the Python Minifier Web API, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt` using pip:
    ```
    pip install -r requirements.txt
    ```
3. Run the Flask application:
    ```
    python app.py
    ```
4. The application should now be running locally.

## Usage:

### Endpoints:

- `POST /`: Accepts a Python code snippet via a form submission and returns the minified version of the code.
- `POST /minify`: Alternative endpoint for minification, accepting Python code snippet via form submission.
- `GET /`: Renders an HTML page.

### Input Limit:

The maximum allowed input size for code snippets is limited to 310 KB. If the submitted code exceeds this limit, an error will be returned.

### CORS Configuration:

Cross-Origin Resource Sharing (CORS) is configured to allow requests from the following origins:

For example:
- https://glad432.github.io
- http://localhost:3000
- https://python-minifier.vercel.app

## Dependencies:

- Flask: A lightweight WSGI web application framework for Python.
- Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS), making cross-origin AJAX possible.

## Contributing:

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
