import sqlite3
from bottle import route, run, debug, template, request, static_file, error
import datetime
import pytz
tzekb = pytz.timezone('Asia/Yekaterinburg')


# only needed when you run Bottle on mod_wsgi
from bottle import default_app

app = application = default_app()


@route('/visitors')
def visitors_list():

    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute("SELECT id, groups, fio, datetime FROM visitors ORDER BY id, groups")
    result = c.fetchall()
    c.close()

    output = template('make_table', rows=result)
    return output


@route('/', method='GET')
def index():
    return template('new_task.tpl')


@route('/new', method='POST')
def addnew():
    group = request.POST.group.strip()
    fio = request.POST.fio.strip()
    added = str(datetime.datetime.now(tzekb))

    if not group or not fio:
        return '<a href="/new">ты что-то забыл указать, вернись</a>'

    print(group, fio, added)
    fp = open('log.txt','a')
    fp.write('%s\t%s\t%s\r\n' % (added, group, fio))
    fp.close()

    try:
        conn = sqlite3.connect('visitors.db')
        c = conn.cursor()
        client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')

        c.execute("INSERT INTO visitors (groups, fio, datetime, ip) VALUES (?,?,?,?)", ( group, fio, added, client_ip ))
        new_id = c.lastrowid

        conn.commit()
        c.close()
    except:
        returnt("Unexpected error:", sys.exc_info()[0])
    return '<p>Я запомню тебя, %s, за номером %s</p>' % (fio, new_id)



@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


if __name__ == '__main__':
    run(host='0.0.0.0', port=20119, reloader=True, debug=True)

# remember to remove reloader=True and debug(True) when you move your
# application from development to a productive environment
