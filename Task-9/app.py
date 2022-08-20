#1
from flask import Flask, render_template, request 
import re

name=""
reg=""

#2
app=Flask(__name__)

#3
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET','POST'])
def search():
    global name,reg
    if request.method=='POST':
        name=request.form["in_1"]
        reg=request.form["in_2"]

        pattern = re.compile(reg)
        
        total = len(pattern.findall(name))
        matched = pattern.findall(name)
        

       
        return render_template('search.html',a=total, b=matched, c=reg, d=name)
    return render_template('index.html')
    

#4
if __name__=='__main__':
    app.run(debug=True)

