import webapp2
from uuid import uuid4

bot_url = "https://tokbox.slack.com/services/hooks/slackbot?token=tmDWAkbbKcxLJDaSINQgxOtw&channel=%23"

class MainPage(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('http://meet.tokbox.com/' + str(uuid4()))

        urlfetch.fetch(url=bot_url + self.request.get('channel_name'),
                       payload="Let's talk: https://meet.tokbox.com/" + str(uuid4()),
                       method=urlfetch.POST)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

