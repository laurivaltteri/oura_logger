Short demo to get data from OURA cloud via python.
This example is utilizing server-side (explicit) flow. Implicit flow would be somewhat simpler, however it's providing access token in plain text.

* First go to https://cloud.ouraring.com/oauth/applications and create a new application
* Insert provided information to config_sample.py and rename it to config.py
* `python oura_server.py`
* Open http://localhost:65010/ in a browser and click to get a token
* Insert token to config.py
* Play with your data (examples at `oura.py`)
