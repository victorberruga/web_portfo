from flask import Flask, render_template, url_for, request, redirect
import csv

"""The strong point of of flask is that it can evaluate expressions within html files
using {{}}, anything within these double curly brackets is interpreted as python and 
it needs to be evaluated. This comes from jinja, a templating language"""
app = Flask(__name__)

"""instead of brute coding all of the .html files we will code it dynamically:
@app.route('/index.html')
def my_home():
    return render_template('index.html')"""


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


"""In order to receive the information we have to add in the html form data by
writing name="email", etc in front of the inputs of the classes"""


@app.route('/submit_form', methods=['POST', 'GET'])  # POST=browser wants us to save, GET=browser wants info
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again.'
