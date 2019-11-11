#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Blueprint, render_template, current_app

flaskRoutes = Blueprint('auth', __name__)

@flaskRoutes.route('/')
def index():
    #print(gui.auth.register())
    #return current_app.template_folder + ' | <a href="/auth/login">Login</a> | <a href="/register">Register</a>'
    return render_template("index.html", data="")


@flaskRoutes.route('/auth/login', methods=['GET'])
def login():
    return '<h1>Login</h1><form action="/auth/login" method="post">E-mail: <input type="text" name="email" /><br />Password: <input type="password" name="password" /><input type="submit" /></form>'

@flaskRoutes.route('/auth/login', methods=['POST'])
def loginCheck():
    return '<h1>Login done?</h1>'

@flaskRoutes.route('/auth/register')
def register():
    return '<h1>Login</h1><form action="/auth/register" method="post">E-mail: <input type="text" name="email" /><br />Password: <input type="password" name="password" /><input type="submit" /></form>'