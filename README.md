Short demo to get data from OURA cloud via python.
This example is utilizing server-side (explicit) flow. Implicit flow would be somewhat simpler, however it's providing access token in plain text.

* First go to https://cloud.ouraring.com/oauth/applications and create a new application
    * The application has to have http://localhost:65010/oura_redir at REDIRECT_URI field!
* Insert provided information to config_sample.py and rename it to config.py
* `python oura_server.py` (requires 'flask' install it using pip, conda, etc.)
* Open http://localhost:65010/ in a browser and click to get a token
* Copy-paste token from browser to config.py
* Play with your data (example lines at `oura_playground.py`) (requires at least 'json' formatting and html 'requests', install via pgkmanager)
