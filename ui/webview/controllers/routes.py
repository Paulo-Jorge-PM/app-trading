#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#from ui.webview import db
from flask import Blueprint, render_template, current_app, jsonify, json, Response, request, redirect, url_for
from core import market

flaskRoutes = Blueprint('routes', __name__)

#===General data for templates without router
@flaskRoutes.context_processor
def template():
	if current_app.auth.user:
		username = current_app.auth.user.username
		balance = current_app.auth.user.balance
	else:
		username = ""
		balance = ""
	loginStatus = current_app.auth.loginStatus
	return dict(username=username, loginStatus=loginStatus, balance=balance)

#===Disable cache for all pages
@flaskRoutes.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response


#===Ajax API
@flaskRoutes.route('/assets')
def assets():
	#User None because we allow to see markets witouth login
	markets = market.Market(None)
	data = markets.getAssets()
	if data != False:
		return Response(json.dumps(data), mimetype='application/json')

@flaskRoutes.route('/prices')
def prices():
	instruments = request.args.get('instruments')
	#data = oanda.get_prices(instruments)
	markets = market.Market(None)
	data = markets.getPrices(instruments)
	#return Response(json.dumps(data), mimetype='application/json')
	if data != False:
		return Response(json.dumps(data), mimetype='application/json')

@flaskRoutes.route('/close')
def close():
	idAsset = request.args.get('idasset')
	markets = market.Market(current_app.auth.user.idUser)
	close = markets.closeAsset(idAsset)
	return close


#===Pages routes
@flaskRoutes.route('/')
def index():
	#if auth done data = xx nome user
    return render_template("index.html", data="")

@flaskRoutes.route('/portfolio')
def portfolio():
	portfolio = current_app.auth.user.portfolio()
	return render_template("portfolio.html", portfolio=portfolio)

@flaskRoutes.route('/markets')
def markets():
    return render_template("markets.html", data="")

@flaskRoutes.route('/wallet')
def wallet():
    return render_template("wallet.html", data="")

@flaskRoutes.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		#To do: validation and sanitazion. Now it is only in front-end view very light
		if request.form:
			username = request.form["username"]
			email = request.form["email"]
			password = request.form["password"]
			reg = current_app.auth.register(username,email,password)
			if reg == True:
				message="success"
			else:
				message="error"
		else:
			message="error"
		return render_template("register.html", status=message)
	else:
		return render_template("register.html", status="ask")

@flaskRoutes.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		if request.form:
			username = request.form["username"]
			password = request.form["password"]
			login = current_app.auth.login(username,password)
			if login == True:
				message="success"
			else:
				message="error"
	else:
		message="ask"
	return render_template("login.html", status=message)


@flaskRoutes.route('/logout')
def logout():
	current_app.auth.logout()
	return redirect( url_for('.index') )

@flaskRoutes.route('/profile')
def profile():
	username = current_app.auth.user.username
	email = current_app.auth.user.email
	return render_template("profile.html", username=username, email=email)

@flaskRoutes.route('/buysell', methods=['GET', 'POST'])
def buysell():
	message=""
	if request.method == 'POST':
		#if loged in
		if current_app.auth.user:
			if request.form:
				orderType = request.form["typeOrder"]
				instrument = request.form["instrument"]
				displayName = request.form["displayName"]
				marketType = request.form["marketType"]
				units = request.form["units"]
				takeProfit = request.form["takeProfit"]
				stopLoss = request.form["stopLoss"]

				markets = market.Market(current_app.auth.user.idUser)
				order = markets.order(orderType, instrument, units, takeProfit, stopLoss, displayName, marketType)

				if order == True:
					message = "Congratulations: order made with success! You can find it in your Portfolio section."
				else:
					message="Error! Something went wrong, your order could not be made."
				return render_template("message.html", message=message)
		else:
			message = "Not autorized: not loged in! Please login first."
			return render_template("message.html", message=message)
