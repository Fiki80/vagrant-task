#!/usr/bin/env python3

from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest

app = Flask(__name__)

c = Counter('visit_counter','Page visit counter')
count = 0

@app.route("/")
def message():
    global count
    c.inc()
    count += 1
    return "This page has been visited " + str(count) + " times!"


@app.route("/metrics")
def metrics():
    return generate_latest()


if __name__ == '__main__':
    app.run()
