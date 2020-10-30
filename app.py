from bottle import route, run, template, request, error,  default_app
import bottle_pymysql
import datetime

import pymysql.cursors
import config

app = default_app()
plugin = bottle_pymysql.Plugin(dbhost=config.DB_HOST,
                             dbuser=config.DB_USER, 
                             dbpass=config.DB_PASS, 
                             dbname=config.DB_DATABASE,
                             charset='utf8mb4')
app.install(plugin)

@route('/list')
def visitors_list(pymydb):    
    pymydb.execute("SELECT id, groups, fio, datetime FROM visitors ORDER BY id, groups")
    result = pymydb.fetchall()

    output = template('make_table', rows=result)
    return output


@route('/', method='GET')
def index():
    return template('index.tpl')


@route('/new', method='POST')
def addnew(pymydb):
    group = request.POST.group.strip()
    fio = request.POST.fio.strip()

    if not group or not fio:
        return '<a href="/">ты что-то забыл указать, вернись</a>'

    pymydb.execute("INSERT INTO visitors (groups, fio) VALUES (%s,%s)", (group, fio))
    new_id = pymydb.lastrowid

    return '<p>Я запомню тебя, %s, за номером %s</p>' % (fio, new_id)


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


if __name__ == '__main__':
    run(host='0.0.0.0', port=config.USE_PORT, reloader=True)
