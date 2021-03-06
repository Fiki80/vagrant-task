#!/usr/bin/env python3

from flask import Flask
from prometheus_client import Counter, Gauge, generate_latest
import time, math
from threading import Thread

app = Flask(__name__)

c = Counter('visit_counter','Page visit counter')
count = 0

def gen_load():
     while True:
        startTime = time.time()
        while time.time() - startTime < 0.5:
            math.factorial(100)
        time.sleep(0.5)

thr1 = Thread(target=gen_load)

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
    thr1.start()
    app.run()
