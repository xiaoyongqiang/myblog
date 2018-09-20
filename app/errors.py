from flask import render_template
from app.app import app, db


#要声明自定义错误处理程序，请使用@errorhandler装饰器
@app.errorhandler(404)
def not_found_error(error):
    #返回值第二个参数为错误编码，默认是200
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500