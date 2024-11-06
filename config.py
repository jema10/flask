#p50
#pip install pymysql
#pip install cryptography
import os
BASE_DIR=os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI='sqlite:///{}'.format(os.path.join(BASE_DIR,'security.db'))
#SQLALCHEMY_DATABASE_URI='mysql+pymysql://master:123456@localhost/master'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY="dev"
