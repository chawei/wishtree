import os
import json,httplib,urllib

from bottle import debug, route, run ,template

from bottle import static_file
debug(True)

@route('/images/<filename:re:.*\.png>')
def send_image(filename):
    print u'filename:%s' % filename
    return static_file(filename, root='images', mimetype='image/png')

@route('/<filename:re:favicon\.ico>')
@route('/<filename:re:[js/,css/,extra/].*>')
@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

@route("/")
def home():
    return template('home')

@route('/test')
def test():
    return  template('sample_index', name='1')

@route('/wish/<objectId>')
def wishLine(objectId):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"include":"photoList,user"})
    connection.connect()
    connection.request('GET', '/1/classes/EVENT/%s?%s' % (objectId,params), '', {
           "X-Parse-Application-Id": "Db11NiRR5q1AIzVeoHUh6zGtfmOp84z7I0N1GYNy",
           "X-Parse-REST-API-Key": "adpRHecNIktEef44NZYzLH3ZslAJPumt7ARSETwe"
         })
    jsonstring = connection.getresponse().read()
    result = json.loads(jsonstring)
    # f = open('a.json','w')
    # f.write(jsonstring);
    # f.close()

    return template('wish', result=result)


@route('/SJW8Fk8HkqBQ618jL0lRXmR9uN0uY39E/appstore')
def count():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"count":1,"limit":0})
    connection.connect()
    connection.request('GET', '/1/users?%s' % params, '', {
       "X-Parse-Application-Id": "O6QXaSCA8Jocb6zHIX7fIunZSw3bfXpChurcyL8A",
       "X-Parse-REST-API-Key": "lv2P4rF6JrbFsN1Q58IqQ0KeVVY5va0z29u1iFyW"
     })
    result = json.loads(connection.getresponse().read())
    return '%d users!' % result['count']

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

