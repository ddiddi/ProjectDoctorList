# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

doctor_names = ["Julius Herbbert", "Algernop Keiger", "Nick Riviero"]
# use decorators to link the function to a url
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home", doctors = doctor_names)  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
