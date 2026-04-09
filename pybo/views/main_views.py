from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/') # bp는 BluePrint 클래스로 생성한 객체 (이름, 모듈명, url_prefix)

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return 'Pybo index'
