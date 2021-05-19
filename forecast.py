#!/usr/bin/env python3
import os
import geocoder
from pyowm.owm import OWM


def get_my_latlng():
    """Return a tuple consisting of my latitude and longitude"""
    g = geocoder.ip('me')

    return g.latlng


def get_week_weather_status():
    """Return a list of the weather status for the next seven days"""
    owm = OWM(os.getenv('owm_key'))
    mgr = owm.weather_manager()

    week_forecast = mgr.one_call(*get_my_latlng()).forecast_daily
    week_weather_status = [d.status for d in week_forecast]

    return week_weather_status

