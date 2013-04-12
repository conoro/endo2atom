Endo2Atom
-------------------
Generate an ATOM feed from your recent Endomondo activity for re-use elsewhere 

Description
-----------
This tool generates an ATOM feed from your public Endomondo activity. Yuo can then use that on sites like IFTTT or dlvr.it to post that activity to far more sites/systems than Endomondo themselves currently support. e.g. you can auto-post your activities to App.Net or Tumblr

More details over on http://conoroneill.net/

Usage
------------------------
* Go to your Endomondo Profile which will have a URL like http://www.endomondo.com/profile/8922951
* Grab that trailing ID and use it on the example of this code that I have running on heroku e.g.: http://blahblhblah.heroku.com/8922951
* That gives you ATOm output so just use that URL on IFTTT etc
* Let me know if you have any problems. I have only tested it on my own Endomondo account

    
Developer Notes
------------------------------------
You can run this on many different Python hosting sites as long as they support WSGI. Try Heroku, Google App Engine etc. It uses Bottle but only in the most minimal way.


Changelog
=========

2013/04/12
----------
First version. Tested on Treadmill walking, treadmill running and road running