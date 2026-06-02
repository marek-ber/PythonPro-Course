from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.get('/about')
def about():
    return "To jest strona o nas"

@app.get('/user/<username>')
def show_profile(username):
    return f"Witaj {username}"

@app.get('/post/<int:post_id>')
def show_post(post_id):
    return f"Wyświetlasz post od id {post_id}"

@app.get('/index')
def index():
    users_from_db = ['Marek', 'Paweł', 'Tomek']
    return render_template('index.html',
                            title='index', 
                            users=users_from_db, author='Marek Berny')


@app.get('/profile/<username>')
def show_my_profile(username):
    return render_template('user.html',
                           title='Profil',
                           my_user_name=username)

if __name__ == '__main__':
    app.run(debug=True)