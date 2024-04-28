from flask import Flask,render_template,redirect,url_for

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    myname="Souradip"
    myresult=33 + 36
    mylist=[34,67,12,89,44,56,90]
    return render_template('index.html',result=myresult,name=myname,list=mylist)

@app.route('/other')
def other():
    random_text="Hello Flask!"
    return render_template('other.html',random_text=random_text)

## Using redirect points for redirecting to other pages
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

##Applying custom filters 

##Example like to reverse a string
@app.template_filter('reverse_str')
def reverse_str(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s,times=2):
    return s*times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i,c in enumerate(s)])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)