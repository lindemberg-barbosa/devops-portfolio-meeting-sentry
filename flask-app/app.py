import sentry_sdk
from flask import Flask, request
from time import sleep

sentry_sdk.init(
    dsn="http://2e77897adfe7463396b4f6b4026f7974@localhost:9000/3",
    traces_sample_rate=1.0,
    release="flask-demo@v0.2",
    environment="production",
)

app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Hello World'


@app.route('/debug-sentry', methods=['GET', 'POST'])
def debug_sentry():
    if request.method == 'POST':
        sleep(10)
        sentry_sdk.capture_message('Something went wrong, sending error to sentry')
        return 'Sending issue to Sentry'
    else:
        try:
            division_by_zero = 1 / 0
        except Exception as e:
            sentry_sdk.capture_exception(e)
        return 'Sending handled issue to Sentry'
