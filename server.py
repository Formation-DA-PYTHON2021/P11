import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


def booked_places(comps, clubs_list):
    places = []
    for comp in comps:
        for club in clubs_list:
            places.append({'competition': comp['name'], 'booked': [0, club['name']]})
    return places


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
places_booked = booked_places(competitions, clubs)


def number_booked_places(competition, club, places_booked, placesRequired):
    for i in places_booked:
        if i['competition'] == competition['name']:
            if i['booked'][1] == club['name'] and i['booked'][0] + placesRequired <= 12:
                i['booked'][0] += placesRequired
                break


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        flash("Sorry, that email wasn't found.")
    return render_template('index.html'), 403


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        if datetime.strptime(foundCompetition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
            flash("This competition is closed.")
            return render_template('welcome.html', club=club, competitions=competitions), 403
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions), 403


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if placesRequired > int(club['points']):
        flash("Your don't have enough points.")
        return render_template('welcome.html', club=club, competitions=competitions), 403

    if placesRequired > int(competition['numberOfPlaces']):
        flash("'Not enough places available.")
        return render_template('welcome.html', club=club, competitions=competitions), 403

    elif placesRequired > 12:
        flash("You can't book more than twelve place per competition")
        return render_template('welcome.html', club=club, competitions=competitions), 403

    else:
        for i in places_booked:
            if i['competition'] == competition['name']:
                if i['booked'][1] == club['name'] and i['booked'][0] + placesRequired <= 12:
                    number_booked_places(competition, club, places_booked, placesRequired)
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
                    club['points'] = int(club['points']) - placesRequired
                    flash('Great-booking complete!')
                    return render_template('welcome.html', club=club, competitions=competitions)
            else:
                flash("You can't book more than twelve place per competition")
                return render_template('welcome.html', club=club, competitions=competitions), 403


@app.route('/viewClubsPoints')
def view_clubs_points():
    club_list = sorted(clubs, key=lambda club: club['name'])
    return render_template('clubs_points.html', clubs=club_list)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
