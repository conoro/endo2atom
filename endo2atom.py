#!/usr/bin/env python
# encoding: utf-8
"""
endo2atom.py

Licensed under MIT License.
Copyright (c) 2013, Conor O'Neill <cwjoneill@gmail.com> - See http://conoroneill.net

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import os
import urllib2
from bs4 import BeautifulSoup
import time
from dateutil.parser import *
from dateutil.tz import *
from datetime import *
import gevent.monkey; gevent.monkey.patch_all()
from bottle import route, run, template


@route('/:user_id')
def index(user_id='8922951'):

    feed = []
 
    #Grab the activity widget HTML and parse
    endourl = 'http://www.endomondo.com/embed/user/workouts?id='+str(user_id)
    try:
        soup = BeautifulSoup(urllib2.urlopen(endourl).read())

        souptable = soup.find("table")

        souprows = souptable.findAll('tr')
        for row in souprows[1:]:
            item = {}

            col = row.findAll('td')
            activity_date = col[0].string.strip()
            activity_link = "http://www.endomondo.com/" + row.findAll('a')[0]['href'].lstrip('../../')
            activity_sport = col[1].string.strip()
            activity_distance = col[2].string.strip()
            activity_duration = col[3].string.strip()

            item["title"] = activity_sport
            item["url"] = activity_link
            item["body"] = "My latest activity was " + activity_sport + " and I did " + activity_distance + " in " + activity_duration
            item["date_published"] = parse(activity_date)
            item["date_updated"] = parse(activity_date)
            item["atom_id"] = "http://www.endo2rss.com/" + user_id + "/"

            # Add item to feed
            feed.append(item)

        #Bottle
        return template('endo2atom', 
            author = "Endomondo",
            title="Your Endomondo Activity Feed",
            site_url = "http:/www.endomondo.com/",
            feed_url = "http://www.endomondo.com/embed/user/workouts?id="+str(user_id),
            date_updated = datetime.now(),
            entries = feed
            )
    except:
        pass

run(server='gevent', port=os.environ.get('PORT', 5000))