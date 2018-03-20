from flask import Flask, render_template, request, jsonify
from app import models as db
import re
from apscheduler.schedulers.background import BackgroundScheduler
from app.auth.JobboleSpider import spider_job

sched = BackgroundScheduler()
app = Flask(__name__)
db = db.MongoSQL()

@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template('jobboleSearch.html')


@app.route('/getshell/page.html', methods=['POST'])
def get_list():
    page = request.args.get('page')
    page = request.form['page']
    page = re.split('[,， 　]+', page)
    page = '|'.join(page)
    lis = db.find_where(page)
    # lis = db.find_all()
    page_list = []
    for l in lis:
        dic = {}
        dic['title'] = l['title']
        dic['href'] = l['href']
        page_list.append(dic)
    page_list
    lis = jsonify(page_list)
    return lis


if __name__ == '__main__':
    sched.add_job(func=spider_job, trigger='cron', hour=00, minute=00, end_date='2019-01-01')
    sched.start()
    app.run(debug=True)
