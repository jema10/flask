#p44
'''
from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/')
@bp.route('/')
def index():
	return "main"
pip install email_validator
pip install flask_wtf
'''
#p67
from flask import Blueprint,render_template,request

from security.models import User
from security import db

from security.forms import UserCreateForm


bp = Blueprint('auth',__name__,url_prefix='/auth')
@bp.route('/')
def index():
	return render_template('/auth/index.html')

@bp.route('/login',methods=('GET','POST'))
def login():
	return render_template('/auth/login.html')

#pip install flask_wtf
@bp.route('/signup',methods=('GET','POST'))
def signup():
	form=UserCreateForm()
	if request.method == 'POST':
		#u = User(username='admin2',password='123456',email='3@t.com')
		u = User(username=form.username.data,password=form.password1.data,email=form.email.data)
		db.session.add(u)
		db.session.commit()


	return render_template('/auth/signup.html',form=form)