from apiclient.discovery import build
from google.appengine.ext import webapp
from oauth2client.contrib.appengine import OAuth2Decorator
from config import CLIENT_ID, CLIENT_SECRET

ipdb.set_trace()
decorator = OAuth2Decorator(
  client_id='your_client_id',
  client_secret='your_client_secret',
  scope='https://www.googleapis.com/auth/calendar')

service = build('calendar', 'v3')

class MainHandler(webapp.RequestHandler):

  @decorator.oauth_required
  def get(self):
    # Get the authorized Http object created by the decorator.
    http = decorator.http()
    # Call the service using the authorized Http object.
    request = service.events().list(calendarId='primary')
    response = request.execute(http=http)
