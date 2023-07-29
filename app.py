## create a simple flask application
from flask import Flask, render_template, url_for,request, redirect
#This is push no1
## This is added in vs code
## create the flask app
app=Flask(__name__)
@app.route('/')
def home():
    return "<h1>Hello World</h1>"

@app.route('/welcome')
def welcome():
    return "Welcome to flask Tutorials"
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/success/<int:score>')
def success(score):
    return f"<h1> you have passed the score is {str(score)} </h1>"

@app.route('/fail/<int:score>')
def fail(score):
    return f"<h1> You are failed your score is {str(score)}</h1>"

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        result=""
        if average_marks >=50:
            result='success'
        else:
            result='fail'
        # return redirect(url_for(result,score=average_marks))
            
        return render_template('result.html',results=average_marks)
    

if __name__=='__main__':
    
    app.run()

