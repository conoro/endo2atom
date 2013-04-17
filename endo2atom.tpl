<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
    <title>{{title}}</title>
    <link rel="alternate" type="text/html" href="{{site_url}}" />
    <link rel="self" type="application/atom+xml" href="{{feed_url}}" />
    <id>{{feed_url}}</id>
    <updated>{{date_updated}}</updated>

    %for entry in entries:
    <entry>
        <title>{{entry['title']}}</title>
        <link rel="alternate" type="text/html" href="{{entry['url']}}" />
        <id>{{entry['url']}}</id>
        <published>{{entry['date_published']}}</published>
        <updated>{{entry['date_updated']}}</updated>
        <author>
            <name>{{author}}</name>
            <uri>{{site_url}}</uri>
        </author>
        <content type="html" xml:base="{{site_url}}" xml:lang="en">
            <![CDATA[{{entry['body']}}]]>
        </content>
    </entry>
    %end

</feed>
