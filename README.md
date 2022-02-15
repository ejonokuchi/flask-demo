# flask-demo

A minimal [Flask](https://flask.palletsprojects.com/en/2.0.x/) app for rapid demos.

Intended for getting Python code live on the Internet in a couple minutes. Not made with any considerations for security, infrastructure, or durability.

Includes the following variants, by branch:
- `main`: a single-page web application, including Bootstrap and HTML templates.
- `api`: a simple API, for serving JSON responses.


## Installation

Use Python 3.

Set up and activate a virtual environment:
```
python3 -m venv venv
. venv/bin/activate
```

Install requirements:
```
pip install -r requirements.txt
```


## Run the server

Start the development server in debug mode:
```
python run.py
```

Start the "production" server:
```
gunicorn --bind 127.0.0.1:8080 --workers 4 --threads 8 src:app
```

## Publish local server via ngrok

The easy way to make your demo public.

If you don't have ngrok, download it by following [these instructions](https://ngrok.com/download). The free version is more than enough to get started.

Forward the local port:
```
ngrok http 8080
```

Or forward the local port with a required username and password (replace `username` and `password` with desired values):
```
ngrok http -auth="username:password" 8080
```


## Deploy via GCP App Engine

The persitent way to make your demo public.

If you aren't already set up on GCP, first follow [this guide](https://cloud.google.com/appengine/docs/standard/python3/quickstart) to set up a Project, enable the Cloud Build API, and install the Google Cloud CLI.

Be sure to name your service in L1 of `./app.yaml`. This will distinguish it from other App Engine services in your GCP project.

Finally, deploy the application:
```
gcloud app deploy
```


## See Also

For a more fully-featured starter application in Flask, see the [official tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/).
