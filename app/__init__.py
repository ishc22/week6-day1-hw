from app import app

from flask import render_template
#end points _ urls 
@app.route("/")
def hello_world():
    return render_template('index.html')
#end points _ urls 

@app.route("/test")
def hello_test():
    return "Hello World this is a test!"

#end points _ urls 
@app.route("/test2")
def hello_test2():
    return "Hello World this is a test2!!!!"