import os
import json,httplib,urllib

from bottle import debug, route, run ,template, redirect

from bottle import static_file

import dateutil.parser
import math

#debug(True)

APP_ID  = 'O6QXaSCA8Jocb6zHIX7fIunZSw3bfXpChurcyL8A'
API_KEY = 'lv2P4rF6JrbFsN1Q58IqQ0KeVVY5va0z29u1iFyW'

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
    try:
        #connect to parse
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        params = urllib.urlencode({"include":"photoList,user"})
        connection.connect()
        connection.request('GET', '/1/classes/EVENT/%s?%s' % (objectId,params), '', {
               "X-Parse-Application-Id": APP_ID,
               "X-Parse-REST-API-Key": API_KEY
             })
        response = connection.getresponse();

        #if no data, redirect to homepage
        if response.status != 200:
            return redirect('/')

        jsonstring = response.read()
        result = json.loads(jsonstring)

        #change the line break symbol
        result['description'] = result['description'].replace(u'\n',u'<br />')

        #calculate date delta
        shotDate1 = dateutil.parser.parse(result['shotDate']['iso'])
        for photo in result['photoList']:
            photo['description'] = photo['description'].replace(u'\n',u'<br />')
            shotDate2 = dateutil.parser.parse(photo['shotDate']['iso'])
            photo['delta'] = timeDeltaString(shotDate1,shotDate2)
            shotDate1 = shotDate2

        #check which word used in the end of line.
        if 'achieved' in result:
            result['delta'] = 'The end.'
        else:
            result['delta'] = 'To be continued...'

        #render it
        return template('wish', result=result)
    except :
        return redirect('/')



@route('/SJW8Fk8HkqBQ618jL0lRXmR9uN0uY39E/appstore')
def count():
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    params = urllib.urlencode({"count":1,"limit":0})
    connection.connect()
    connection.request('GET', '/1/users?%s' % params, '', {
       "X-Parse-Application-Id": APP_ID,
       "X-Parse-REST-API-Key": API_KEY
     })
    result = json.loads(connection.getresponse().read())
    return '%d users!' % result['count']

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

