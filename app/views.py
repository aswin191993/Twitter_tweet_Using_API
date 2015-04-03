import requests
from flask import render_template, flash, redirect,url_for,session,abort
from app import app
from .forms import SigninForm
import json
import oauth2 as oauth,json
import twitter

def reques(url):
	consumer = oauth.Consumer(key='GcPPtjWQoHZiLWTpMQa3z44Es',secret='JJo4VbMBKJ6J9FdSl6x10tpGWGh2mEBjc1NzHXxDWCNo3mhILz')
	token = oauth.Token(key='597987159-cX3oqo8rGFVC0i1WZZuN8hI0qKXjcAQBZlE66un7',secret='7idwwQzFB1TqRmKBcTSFwW79BGKMkykb6c2oT1s2GLWoN')
	client = oauth.Client(consumer, token)
	resp,content = client.request( url)
	return content

@app.route('/',  methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = SigninForm()
	resp=[]
	if form.validate_on_submit():
		username=form.idu.data
		u=reques('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+username+'&count=10')
		count=""
		stored=[]
		r=str(json.loads(u))
		for i in r:
			count+=i
			if i == ",":
				stored.append(count)
				count=""
		for k in stored:
			if "text" in k and "text_" not in k:
				resp.append(k[12:-23])
	return render_template('index.html',title='Home',form=form,resp=resp)
