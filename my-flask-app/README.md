# My Flask App

This is a simple Flask application that demonstrates the basic structure and functionality of a Flask web application.

## Project Structure

```
my-flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.py` file to set your configuration variables, such as database connection details and secret keys.

## Running the Application

To run the application, use the following command:
```
flask run
```

Make sure to set the `FLASK_APP` environment variable to `app` before running the command.

## Usage

Once the application is running, you can access it at `http://127.0.0.1:5000/`. You can define your routes in `app/routes.py` and your data models in `app/models.py`.