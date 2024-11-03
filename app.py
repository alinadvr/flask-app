from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

trips = [
    {
        'country': 'Turkey',
        'operator': 'Alyans',
        'price': 43475, 'days': 6,
    },
    {
        'country': 'Spain',
        'operator': 'Siesta',
        'price': 203964,
        'days': 10,
    },
    {
        'country': 'Egypt',
        'operator': 'Siesta',
        'price': 48119,
        'days': 6,
    },
    {
        'country': 'Turkey',
        'operator': 'Itravel',
        'price': 54830,
        'days': 6,
    },
    {
        'country': 'Egypt',
        'operator': 'Alyans',
        'price': 53630,
        'days': 6,
    },
    {
        'country': 'Spain',
        'operator': 'Siesta',
        'price': 146047,
        'days': 8,
    },
    {
        'country': 'Turkey',
        'operator': 'Itravel',
        'price': 34854,
        'days': 4,
    },
    {
        'country': 'Egypt',
        'operator': 'Pilon',
        'price': 54282,
        'days': 6,
    },
    {
        'country': 'Spain',
        'operator': 'Itravel',
        'price': 135683,
        'days': 6,
    },
    {
        'country': 'Egypt',
        'operator': 'Pilon',
        'price': 56159,
        'days': 6,
    }
]


@app.route('/')
def home_page():
    return render_template('home.html', trips=trips)


@app.errorhandler(404)
def not_found_page(e):
    return render_template('not_found.html'), 404


@app.route('/trips/operator', methods=['GET'])
def get_trips_by_operator():
    name = request.args.get('name')

    if not name or name == "":
        return render_template('no_data.html')

    trips_by_operator = [trip for trip in trips if name.lower() in trip['operator'].lower()]

    if trips_by_operator:
        return render_template('trips.html', trips=trips_by_operator, name=name)
    else:
        return render_template('no_data.html')


@app.route('/trips/days', methods=['GET'])
def get_trips_by_days():
    days = request.args.get('days')

    if not days or days == "":
        return render_template('no_data.html')

    try:
        days = int(days)

        trips_by_days = [trip for trip in trips if (days <= trip['days'])]

        if trips_by_days:
            return render_template('trips.html', trips=trips_by_days)
        else:
            return render_template('no_data.html')
    except ValueError:
        return render_template('no_data.html')


@app.route('/trips/expensive/turkey', methods=['GET'])
def get_most_expensive_trip_turkey():
    turkey_trips = [trip for trip in trips if trip['country'] == 'Turkey']

    if turkey_trips:
        trip = max(turkey_trips, key=lambda x: x['price'])
        return render_template('trips.html', trips=[trip])
    else:
        return render_template('no_data.html')


if __name__ == '__main__':
    app.run()
