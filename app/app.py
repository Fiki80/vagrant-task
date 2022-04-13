#!/usr/bin/env python3

import os, psutil

from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

c = Counter('visit_counter','Page visit counter')

def get_process_metrics():
    proc = psutil.Process(os.getpid())
    return proc.memory_info().rss


@app.route("/")
def message():
    c.inc()
    vv = get_process_metrics()
    return "Hello world! " + str(vv)


@app.route("/metrics")
def metrics():
    return generate_latest()
#return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run()
