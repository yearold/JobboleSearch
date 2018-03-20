#!/usr/bin/python3
# -*- coding:utf-8 -*-
from flask import Flask, request
from flask_apscheduler import APScheduler

app = Flask(__name__)
aps = APScheduler()


class Config(object):
    JOBS = []


def task1(self, a, b):
    print(str(a) + ' ' + str(b))


# 暂停
@app.route('/pause')
def pausetask(self, id):
    aps.pause_job(id)
    return 'SUCCESS!'


# 恢复
@app.route('/resume')
def resumetask(self, id):
    aps.resume_job(id)
    return 'SUCCESS!'


# 获取
@app.route('/gettask')
def get_task(self, id):
    jobs = aps.get_jobs()
    print(jobs)
    return 'SUCCESS!111'


# 移除
@app.route('removetask')
def remove_task(self, id):
    aps.remove_job(id)
    return '000'


@app.route('/addjob', methods=['GET', 'POST'])
def add_task(self):
    aps.add_job(func=task1, id='1', args=(1, 2), trigger='interval', seconds=5, replace_existing=True)
    return 'sucess'


if __name__ == '__main__':
    app.config.from_object('Config')
    aps.init_app(app=app)
    aps.start()
    app.run(debug=True)
