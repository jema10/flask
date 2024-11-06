#p44
'''
from flask import Blueprint

bp = Blueprint('main',__name__,url_prefix='/')
@bp.route('/')
def index():
	return "main"
'''
#p67
from flask import Blueprint,render_template

bp = Blueprint('main',__name__,url_prefix='/')
@bp.route('/')
def index():
	return render_template('index.html')

@bp.route('/intro')
def intro():
	return render_template('intro.html')