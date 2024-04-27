from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    myname="Souradip"
    myresult=33 + 36
    mylist=[34,67,12,89,44,56,90]
    return render_template('index.html',result=myresult,name=myname,list=mylist)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)