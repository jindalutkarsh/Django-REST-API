# Django-REST-API
##Google Calendar Integration using Django REST API
This project demonstrates the implementation of Google Calendar integration using Django REST API and OAuth2 authentication. It allows users to authenticate with their Google accounts, authorize the application to access their calendar, and retrieve a list of events from their calendar.

#Prerequisites
Before running this project, make sure you have the following:
Python 3.6 or above
Django 3.x
Django REST Framework
Setup
Clone the repository:
bash
Copy code
git clone <repository-url>
Install the required dependencies:
Copy code
pip install -r requirements.txt
Configure Google API credentials:

Go to the Google API Console.
Create a new project (if not already created).
Enable the Google Calendar API for the project.
Create OAuth 2.0 credentials (client ID and client secret).
Set the redirect URI to <your-base-url>/rest/v1/calendar/redirect/.
#Update the settings:

Open the settings.py file in your Django project.
Set the GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, and GOOGLE_REDIRECT_URI variables with your Google API credentials.
Usage
Start the Django development server:
Copy code
python manage.py runserver
#Access the following API endpoints:

/rest/v1/calendar/init/: Initiates the OAuth process by redirecting the user to the Google authorization page. The user will be prompted to enter their credentials.
/rest/v1/calendar/redirect/: Handles the redirect request sent by Google after successful authorization. It retrieves the access token and fetches the list of events from the user's calendar.
#Implementation Details
GoogleCalendarInitView
This view starts the OAuth process. It redirects the user to Google's authorization page, where they need to enter their Google account credentials.

The view constructs the authorization URL with the necessary parameters, including the client ID, redirect URI, response type, scope, and access type. The user is then redirected to this URL.

GoogleCalendarRedirectView
This view handles the redirect request sent by Google after the user has authorized the application. It performs two main tasks:

Exchange the authorization code for an access token:

The view retrieves the authorization code from the request parameters.
It constructs a request to Google's token endpoint, including the code, client ID, client secret, redirect URI, and grant type.
The view sends a POST request to the token endpoint to exchange the code for an access token.
If the response contains an access token, it proceeds to the next step.
Retrieve events from the user's calendar:

The view uses the obtained access token to authenticate subsequent requests.
It sends a GET request to the Google Calendar API endpoint to fetch the list of events from the user's calendar.
The response, containing the events data, is returned as an HTTP response.
#Conclusion
This project demonstrates how to integrate Google Calendar using Django REST API and OAuth2 authentication. It provides two API endpoints, one for initiating the OAuth process and another for handling the authorization redirect and retrieving events from the user's calendar.
