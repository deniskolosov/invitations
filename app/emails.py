# -*- coding: utf-8 -*-
from flask.ext.mail import Message
from app import app, mail
from flask import render_template
from config import ADMINS
from threading import Thread


def send_async_email(msg):
    mail.send(msg)

def send_email(subject,sender,recipients,text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    t = Thread(target=send_async_email,args=[msg])
    t.start()

def email_form_record(person):
    send_email('New form',ADMINS[0],
               ADMINS,render_template('form_email.txt',p=person),
               render_template('form_email.html',p=person))
    print 'Sent an email!'