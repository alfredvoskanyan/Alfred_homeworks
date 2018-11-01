from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfghjkl'

data_temp = [
    {
        'author' : 'Manjaro home page',
        'title' : 'Manjaro Linux',
        'content' : 'About Manjaro Linux',
        'date_posted' : 'April 1st, 2017',
        'home_page' : 'https://manjaro.org/',
        'link' : '/manjaro',
        'logo' : '/static/manjaro.png',
        'image' : '/static/manjaro-small.png'

    },

    {
        'author' : 'Mint home page',
        'title' : 'Linux Mint',
        'content' : 'About Linux Mint',
        'date_posted' : 'April 2nd, 2017',
        'home_page' : 'http://linuxmint.com/',
        'link' : '/mint',
        'logo' : '/static/mint.png',
        'image' : '/static/mint-small.png'

    },
    {
        'author' : 'Ubuntu home page',
        'title' : 'Ubuntu',
        'content' : 'About Ubuntu',
        'date_posted' : 'April 3rd, 2017',
        'home_page' : 'https://www.ubuntu.com/',
        'link' : '/ubuntu',
        'logo' : '/static/ubuntu.png',
        'image' : '/static/ubuntu-small.png'

    },

]

gallery_pictures = [
   '/static/manjaro-small.png',
    '/static/mint-small.png',
    '/static/ubuntu-small.png'
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = data_temp, my_title = "Home")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/manjaro')
def manjaro():
    return render_template('manjaro.html', posts = data_temp[0])

@app.route('/mint')
def mint():
    return render_template('mint.html', posts = data_temp[1])

@app.route('/ubuntu')
def ubuntu():
    return render_template('ubuntu.html', posts = data_temp[2])

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', pictures = gallery_pictures)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form1 = LoginForm()
    my_username = 'betman'
    my_password = 'betman123'
    if form1.username.data == my_username and form1.password.data == my_password:
        flash(f'Login Success {form1.username.data}!!!', 'success')
        return render_template('login.html', form = form1)
    else:
        flash(f'Login Failed {form1.username.data}!!!', 'danger')
        return render_template('login.html', form = form1)
    return render_template('login.html', form = form1)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form1 = RegistrationForm()
    if form1.validate_on_submit():
        flash(f'Welcome dear {form1.username.data}!!!', 'success')
        return redirect(url_for('home'))
    else:
        flash(f'You are welcome dear {form1.username.data}!!!', 'danger')
        return render_template('register.html', form = form1)
    return render_template('register.html', form = form1)


if __name__ == '__main__':
    app.run(debug = True)





