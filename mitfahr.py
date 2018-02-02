from flask import Flask, Response, jsonify, render_template, request, g,redirect, url_for
from os.path import join, dirname
import dbstart

app = Flask(__name__)


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['Name']
    Id = request.form['USERID']
    print (name, Id)
    dbstart.createperson(name,Id)
    return render_template('index.html',Name=name, Id=Id)
    #return render_template('greeting.html', say=request.form['say'], to=request.form['to'])

@app.route('/add_place', methods=['POST'])
def add_place():
    name = request.form['Name']
    category = request.form['Category']
    print (name, category)
    dbstart.createplace(name,category)
    return render_template('index.html',Place=name, Category=category)


@app.route('/', methods=['GET', 'POST'])
def appview():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(host='194.95.202.123')
    app.run(host='localhost')
