from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://host:senha@servidor/REGISTRO_ALUNOS_FAMERP'

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)

