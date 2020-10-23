from bottle import route, run, template, request, error,  default_app
import datetime

import pymysql.cursors
import config

app = default_app()
conn = pymysql.connect(host=config.DB_HOST,
                             user=config.DB_USER,
                             password=config.DB_PASS,
                             db=config.DB_DATABASE,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


@route('/list')
def visitors_list():
    c = conn.cursor()
    c.execute("SELECT id, groups, fio, datetime FROM visitors ORDER BY id, groups")
    result = c.fetchall()
    c.close()

    output = template('make_table', rows=result)
    return output


@route('/', method='GET')
def index():
    return template('index.tpl')


@route('/new', method='POST')
def addnew():
    group = request.POST.group.strip()
    fio = request.POST.fio.strip()

    if not group or not fio:
        return '<a href="/new">ты что-то забыл указать, вернись</a>'

    c = conn.cursor()
    c.execute("INSERT INTO visitors (groups, fio) VALUES (%s,%s)", (group, fio))
    new_id = c.lastrowid
    conn.commit()
    c.close()

    return '<p>Я запомню тебя, %s, за номером %s</p>' % (fio, new_id)


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


if __name__ == '__main__':
    run(host='0.0.0.0', port=config.USE_PORT, reloader=True)
