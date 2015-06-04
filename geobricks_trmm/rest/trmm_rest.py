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
    out = m.list_years()
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/<year>/')
@cross_origin(origins='*')
def list_months(year):
    out = m.list_months(year)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/<year>/<month>/')
@cross_origin(origins='*')
def list_days(year, month):
    out = m.list_days(year, month)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')


@trmm.route('/<year>/<month>/<day>/')
@cross_origin(origins='*')
def list_layers(year, month, day):
    out = m.list_layers(year, month, day)
    return Response(json.dumps(out), content_type='application/json; charset=utf-8')
