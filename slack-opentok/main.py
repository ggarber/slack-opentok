import webapp2
from uuid import uuid4
from google.appengine.api import urlfetch

bot_url = "https://tokbox.slack.com/services/hooks/slackbot?token=tmDWAkbbKcxLJDaSINQgxOtw&channel=%23"

class MainPage(webapp2.RequestHandler):
    def post(self):
        room = str(uuid4())
        text = self.request.get('text')
        if text:
            room = text

        urlfetch.fetch(url=bot_url + self.request.get('channel_name'),
                       payload="Let's talk: https://meet.tokbox.com/" + room,
                       method=urlfetch.POST)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

