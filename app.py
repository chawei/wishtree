import os
import json,httplib,urllib

from bottle import debug, route, run ,template

from bottle import static_file

import dateutil.parser
import math

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


def timeDeltaString(t1,t2):
    delta = t2 - t1
    if delta.days < 0 :
        return t2.strftime('%b %d, %Y at %I:%M%p')
    elif delta.days == 1:
        return '%d day after...' % delta.days
    elif delta.days > 1:
        return '%d days after...' % delta.days
    elif delta.days ==0:
        mins = math.floor(delta.seconds / 60)
        hours = math.floor(mins / 60)

        if hours == 1:
            return '%d hour after...' % hours
        elif hours > 1:
            return '%d hours after...' % hours
        elif mins == 1:
            return '%d minute after...' % mins
        elif mins > 1:
            return '%d minutes after...' % mins
        else:
            return 'few seconds after...'

    return str(delta)


@route('/wish/<objectId>')
def wishLine(objectId):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"include":"photoList,user"})
    connection.connect()
    connection.request('GET', '/1/classes/EVENT/%s?%s' % (objectId,params), '', {
           "X-Parse-Application-Id": "O6QXaSCA8Jocb6zHIX7fIunZSw3bfXpChurcyL8A",
           "X-Parse-REST-API-Key": "lv2P4rF6JrbFsN1Q58IqQ0KeVVY5va0z29u1iFyW"
         })
    jsonstring = connection.getresponse().read()
    result = json.loads(jsonstring)
    shotDate1 = dateutil.parser.parse(result['shotDate']['iso'])
    for photo in result['photoList']:
        shotDate2 = dateutil.parser.parse(photo['shotDate']['iso'])
        photo['delta'] = timeDeltaString(shotDate1,shotDate2)
        shotDate1 = shotDate2

    if 'achieved' in result:
        result['delta'] = 'The end.'
    else:
        result['delta'] = 'To be continued...'
        
    

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

