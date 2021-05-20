from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(
    SECRET_KEY = 'FUCKYOU',
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:Sophia17@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 'postgresql+psycopg2://login:pass@localhost/flask_app'
)

db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello_flask():
    return 'Hello Flask'


@app.route('/new/')
def query_string(greetings = 'Fuckface'):
    query_value = request.args.get('greetings',greetings)
    return '<h1> the greeting is :{0} </h1>'.format(query_value)

@app.route('/User')
@app.route('/User/<name>')
def no_query_string(name='mina'):
    return '<h1> hey: {} </h1>'.format(name)


@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1, num2 ):
    return '<h1> the sum is : {}'.format(num1 + num2) + '</h1>'

@app.route('/product/<float:num1>/<float:num2>')
def product(num1, num2):
    return '<h1> the product is: {}'.format(num1 * num2) + '</h1>'



@app.route('/temp')
def using_templates():
    return  render_template('hello.html')


@app.route('/watch')
def top_movies():
    movie_list = ['lemby', 'zeby', 'masr', 'mask']

    return render_template('movies.html',
    movies= movie_list,name='Harry')


@app.route('/tables')
def movies_plus():
    movies_dict = {'autopsy of jane doe': 02.41,
    'neon deamon': 1.5,
    'kong': 3.7,
    'spiderman': 1.48}

    return render_template('table_data.html',
    movies=movies_dict,
    name= 'Sally')


@app.route('/filters')
def filter_data():
    movies_dict = {'autopsy of jane doe': 02.41,
        'neon deamon': 1.5,
        'kong': 3.7,
        'spiderman': 1.48}

    return  render_template('filter_data.html',
    movies = movies_dict,
    name = None,
    film = 'a christmas carol'
    )


@app.route('/macros')
def jinja_macros():
    movies_dict = {'autopsy of jane doe': 02.41,
        'neon deamon': 1.5,
        'kong': 3.7,
        'spiderman': 1.48}

    return  render_template('using_macros.html', movies = movies_dict)


class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'publisher is {}'.format(self.name)




class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # ESTABLISH A RELATIONSHIP BETWEEN PUBLICATION AND BOOK TABLES
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):

        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)







if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    
    


