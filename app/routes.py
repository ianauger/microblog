from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ian'}
    posts = [
            {
                'author': {'username': 'Alex'},
                'body': 'Another day in the metroplex...'
            },
            {
                'author': {'username': 'Kendra'},
                'body': 'Three inches of ash fell last night.'
            }
        ]
    return render_template('index.html', title='Home', user=user, posts=posts)
