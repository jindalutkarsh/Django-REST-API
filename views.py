import json
import requests
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

GOOGLE_CLIENT_ID = '<your-google-client-id>'
GOOGLE_CLIENT_SECRET = '<your-google-client-secret>'
GOOGLE_REDIRECT_URI = '<your-google-redirect-uri>'
GOOGLE_AUTH_ENDPOINT = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_ENDPOINT = 'https://oauth2.googleapis.com/token'
GOOGLE_API_ENDPOINT = 'https://www.googleapis.com/calendar/v3/events'

class GoogleCalendarInitView(View):
    def get(self, request):
        # Step 1 of OAuth: Redirect user to Google's authorization page
        params = {
            'client_id': GOOGLE_CLIENT_ID,
            'redirect_uri': request.build_absolute_uri(reverse('google-calendar-redirect')),
            'response_type': 'code',
            'scope': 'https://www.googleapis.com/auth/calendar.readonly',
            'access_type': 'offline',
        }
        auth_url = f'{GOOGLE_AUTH_ENDPOINT}?{urlencode(params)}'
        return HttpResponseRedirect(auth_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        code = request.GET.get('code')
        if code:
            # Step 2 of OAuth: Exchange code for access token
            token_params = {
                'code': code,
                'client_id': GOOGLE_CLIENT_ID,
                'client_secret': GOOGLE_CLIENT_SECRET,
                'redirect_uri': request.build_absolute_uri(reverse('google-calendar-redirect')),
                'grant_type': 'authorization_code',
            }
            token_response = requests.post(GOOGLE_TOKEN_ENDPOINT, data=token_params)
            token_data = json.loads(token_response.text)
            
            if 'access_token' in token_data:
                # Use the access token to fetch events from the user's calendar
                access_token = token_data['access_token']
                headers = {'Authorization': f'Bearer {access_token}'}
                events_response = requests.get(GOOGLE_API_ENDPOINT, headers=headers)
                events_data = json.loads(events_response.text)
                
                # Process events_data as per your requirements
                
                return HttpResponse(events_data)
        
        return HttpResponse('Authentication failed')

