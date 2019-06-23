# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

doctor_names = ["Julius Herbbert", "Algernop Keiger", "Nick Riviero"]
data_list = [["Julius Herbbert","jh@gmail.com",[["Patient1", "8am", "Regular Visit"], ["Patient2", "10am", "Fever"], ["Patient3", "3:30pm", "Visit"]]],
            ["Algernop Keiger","ak@yahoo.com",[["Patient4", "7am", "Sick"], ["Patient5", "1:30pm", "Annual"]]],
            ["Nick Riviero","nr@nr.com",[["Patient6", "6am", "Basic Check Up"], ["Patient7", "1:30pm", "Fever Returning"]]]]

# use decorators to link the function to a url
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home", doctors = doctor_names, data_list=data_list)  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
