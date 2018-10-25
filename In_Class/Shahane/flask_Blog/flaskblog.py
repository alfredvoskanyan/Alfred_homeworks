from flask import Flask, render_template
app = Flask(__name__)

data_temp = [
    {
        'author' : 'auther1',
        'title' : 'title1',
        'content' : 'content1',
        'date_posted' : 'Aprilo 1 2017'
    },
    {
        'author' : 'auther2',
        'title' : 'title2',
        'content' : 'content2',
        'date_posted' : 'Aprilo 2 2017'
    }

]


@app.route("/")
def Home():
    return render_template('home.html', posts = data_temp)

@app.route("/about")
def About():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)