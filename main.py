
# Main Python code (`main.py`) for Flask application

# Import the necessary modules.
from flask import Flask, render_template

# Create a Flask application.
app = Flask(__name__)

# Define the routes for the application.
@app.route('/')
def index():
    """Main landing page for the application."""
    return render_template('index.html')

@app.route('/learning-path')
def learning_path():
    """Displays the learning path to master calculus."""
    return render_template('learning-path.html')

@app.route('/resources')
def resources():
    """Lists external resources related to calculus."""
    return render_template('resources.html')

@app.route('/progress-tracker')
def progress_tracker():
    """Allows users to track their progress through the learning path."""
    return render_template('progress-tracker.html')

@app.route('/exercises')
def exercises():
    """Provides interactive exercises related to calculus topics."""
    return render_template('exercises.html')

@app.route('/about')
def about():
    """Displays information about the application and its creators."""
    return render_template('about.html')

# Run the application.
if __name__ == '__main__':
    app.run(debug=True)
