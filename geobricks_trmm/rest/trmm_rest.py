import json
from flask import Blueprint
from flask import Response
from flask.ext.cors import cross_origin
from geobricks_trmm.core import trmm_core as m

trmm = Blueprint('trmm', __name__)


@trmm.route('/discovery/')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service available for all Geobricks libraries that describes the plug-in.
    @return: Dictionary containing information about the service.
    """
    out = {
        'name': 'TRMM',
        'description': 'Core functionalities and services for TRMM products.',
        'type': 'DATASOURCE'
    }
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/')
@cross_origin(origins='*')
def list_years():
    """
    List all the available years.
    @return: A list of objects code/label with all the available years.
    """
    out = m.list_years()
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/<year>/')
@cross_origin(origins='*')
def list_months(year):
    """
    List all the available months for a given year.
    @param year: Year of interest, e.g. 2014.
    @type year: str | int
    @return: A list of objects code/label with all the available months.
    """
    out = m.list_months(year)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/<year>/<month>/')
@cross_origin(origins='*')
def list_days(year, month):
    """
    List all the available days for a given year and month.
    @param year: Year of interest, e.g. 2014.
    @type year: str | int
    @param month: Month of interest, e.g. 5.
    @type month: str | int
    @return: A list of objects code/label with all the available days.
    """
    out = m.list_days(year, month)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/<year>/<month>/<day>/')
@cross_origin(origins='*')
def list_layers(year, month, day):
    """
    List all the available layers for a given year, month and day.
    @param year: Year of interest, e.g. 2014.
    @type year: str | int
    @param month: Month of interest, e.g. 5.
    @type month: str | int
    @param day: Day of interest, e.g. 3.
    @type day: str | int
    @return: A list of objects describing the layers.
    """
    out = m.list_layers(year, month, day)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')
