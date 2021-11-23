from datetime import date, datetime, tzinfo

from astral import LocationInfo
from astral.sun import sunset, sunrise


class Sun:
    """
    Calculate sunset based on longitude and latitude
    """
    tz = 'Europe/Brussels'

    def sunset(self, lon: float, lat: float, date: date) -> datetime:
        location = LocationInfo('x', 'x', self.tz, lat, lon)
        s = sunset(location.observer, date=date, tzinfo=location.timezone)
        return s

    def sunrise(self, lon: float, lat: float, date: date) -> datetime:
        location = LocationInfo('x', 'x', self.tz, lat, lon)
        s = sunrise(location.observer, date=date, tzinfo=location.timezone)
        return s
