from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojos, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos=dojos.Dojo.get_all())

@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

