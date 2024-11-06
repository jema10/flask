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

bp = Blueprint('board',__name__,url_prefix='/board')
@bp.route('/')
def index():
	return render_template('/board/index.html')
