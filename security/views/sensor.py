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

bp = Blueprint('sensor',__name__,url_prefix='/sensor')
@bp.route('/')
def index():
	return render_template('/sensor/index.html')
