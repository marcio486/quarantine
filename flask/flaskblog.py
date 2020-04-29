from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '5321996517bd5f3399d5ad36d915a8d7'

posts = [
     {
     'author':'Marcio',
     'title':'Post do Blog',
     'content':'Blog post 1',
     'date_post':'27 de maio, 2020'
     },
    {
     'author':'Malandro',
     'title':'malandragem',
     'content':'a arte da malandragem',
     'date_post':'27 de maio, 2020'
     }
]


@app.route("/")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title = 'about')

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)
    
if __name__ == '__main__':
    app.run(debug = True)