from flask import Flask, render_template, abort,request,redirect,url_for,flash
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import numpy as np
from model import abandoning_user
from auto_email import Email
app = Flask(__name__)

app.secret_key='5791628bb0b13ce0c676dfde280ba245'
passw='####'#Sender's email password 
#app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'
 
# @app.route('/')
# def home():
#     return render_template('main.html')
check=0



@app.route('/',methods=['GET','POST'])
def index():
    global check
    global prob
    global name
    global email
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    if request.method == 'POST':
        email = request.form['email']
        # print("##################",text)
        if(email=='admin@dell.com'):
        	return redirect(url_for('log'))
        name,prob=abandoning_user(email)
        # print("############",name," ",email,"$$$$$$$$$$$")
        check=1
    # print("############",name," ",email,"$$$@@@@@@@@@@@@@@$$$$$$$$")


    if check==1 and cv==1 and prob==0:
        global passw
        # print("############",name," ",email,"############")
        Email(name,email,passw,False)
        check=0
        return redirect(url_for('index1'))
    if cv==1:
        return redirect(url_for('login'))

    return render_template('index.html',cart_value=cv)

@app.route('/index1',methods=['GET','POST'])
def index1():

    b=np.loadtxt('cartvalue.txt')
    cv = b+1
    a=[cv]
    cv=int(cv)
    np.savetxt('cartvalue.txt',a)
    return redirect(url_for('index'))

@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/log')
def log():
	a=[0]
	prob=-1
	name=''
	email=''
	np.savetxt('cartvalue.txt',a)
	global check
	check=0
	fb=[]
	f = open("feedback.txt", "r")
	for x in f:
		fb.append(x)
	return render_template('log.html',feedback=fb)

@app.route('/shop')
def shop():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    return render_template('shop.html',cart_value=cv)

@app.route('/product_single')
def product_single():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    return render_template('product-single.html',cart_value=cv)

@app.route('/cart')
def cart():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
	# img='images/product-3.png'
    return render_template('cart.html',cart_value=cv)

@app.route('/checkout')
def checkout():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    return render_template('checkout.html',cart_value=cv)

@app.route('/checkout_message')
def checkout_message():
	b=np.loadtxt('cartvalue.txt')
	cv = b
	cv=int(cv)
	global name
	global email
	global passw
	print("############# In checkout_message #############")
	Email(name,email,passw,True)
	return render_template('checkout.html',cart_value=cv)

@app.route('/about')
def about():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    return render_template('about.html',cart_value=cv)

@app.route('/blog')
def blog():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    return render_template('blog.html',cart_value=cv)

@app.route('/contact')
def contact():
    b=np.loadtxt('cartvalue.txt')
    cv = b
    cv=int(cv)
    return render_template('contact.html',cart_value=cv)




if __name__ == '__main__':
    app.run(debug = True)