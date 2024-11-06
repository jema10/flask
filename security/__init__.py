from flask import Flask
#db사용하기 위함
#pip install Flask_Migrate
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

#p42_step1
'''
def create_app():
	app=Flask(__name__)
	@app.route('/')
	def index():
		return 'hello'
	return app
'''
#p45_step2
'''
def create_app():
	app=Flask(__name__)
	from .views import main,auth,board,sensor
	app.register_blueprint(main.bp)
	app.register_blueprint(auth.bp)
	app.register_blueprint(board.bp)
	app.register_blueprint(sensor.bp)

	return app
'''
#p57_step3,p51
def create_app():
	app=Flask(__name__)
	app.config.from_object(config)
	
	#ORM
	db.init_app(app)
	migrate.init_app(app,db)
	from . import models
	
	from .views import main,auth,board,sensor
	app.register_blueprint(main.bp)
	app.register_blueprint(auth.bp)
	app.register_blueprint(board.bp)
	app.register_blueprint(sensor.bp)



	return app



