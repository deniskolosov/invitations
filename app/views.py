# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, session, g, request
from app import app, db
from forms import InvitationForm, SubmitForm
from models import Person
from emails import email_form_record
from invitations import SendData
from threading import Thread


@app.route("/", methods = ["GET", "POST"])
def index():
    form = InvitationForm()
    if form.validate_on_submit():

        person = Person(booking_number=form.booking_number.data,
                        name=form.name.data,
                        last_name=form.last_name.data,
                        sex=form.sex.data,
                        passport_number=form.passport_number.data,
                        delivery_needed=form.delivery_needed.data,
                        address=form.address.data,
                        citizenship=form.citizenship.data,
                        birth_date=form.birth_date.data,
                        entry_date=form.entry_date.data,
                        exit_date=form.exit_date.data,
                        kids=form.kids.data,
                        transport=form.transport.data,
                        email=form.email.data,
                        cities=form.cities.data,
                        if_double=form.if_double.data)
        db.session.add(person)
        db.session.commit()
        flash('Thank you!')
        return redirect('/')

    return render_template('index.html',
                           title="Invitation form",
                           form=form)

@app.route("/invitations", methods = ["GET", "POST"])
def invitations_page():
    persons = Person.query.order_by(Person.id).all()
    form = SubmitForm()

    if request.method == "POST":
        email_form_record(persons[int(form.hidden_field.data)])
        return render_template('invitations.html',
                           persons=persons,
                           form=form)

    return render_template('invitations.html',
                           persons=persons,
                           form=form)

@app.route("/getpdf", methods = ["GET", "POST"])
def pdf_page():
    persons = Person.query.order_by(Person.id).all()
    form = SubmitForm()

    if request.method == "POST":
        s = SendData(persons[int(form.hidden_field.data)])

        t = Thread(target=s.fill_data())
        t.start()

        return redirect('http://travelrussia.su/ru/cabinet.php?page=history')

    return render_template('invitations.html',
                           persons=persons,
                           form=form)

