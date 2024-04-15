from flask import Flask,render_template,url_for,redirect

# Create a Flask app instance
app = Flask(__name__)

# Define a route and corresponding view function
@app.route('/')
def index():
    return render_template("home.html")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
