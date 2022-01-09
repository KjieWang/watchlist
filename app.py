from flask import Flask
from flask import escape,url_for
app = Flask(__name__)

@app.route('/hello')
@app.route('/')
@app.route('/home')

def hello():
	return '<h1>欢迎学习flask框架</h1>'

@app.route('/hello/<name>')
def helloq(name):
	return 'hello page'

@app.route('/user/<name>')
def user_page(name):
	return 'user: %s' %escape(name)

@app.route('/test')
def test_url_for():
	print(url_for('hello'))
	print(url_for('user_page',name='wkj'))
	pirnt(url_for('user_page',name='pangpang'))
	print(url_for('test_url_for',min=2))
	return 'Test Page'