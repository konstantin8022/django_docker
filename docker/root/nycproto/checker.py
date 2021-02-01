from haversine import Haversine

class Checker():

    def __init__(self):
        # self.longitude = lon
        # self.latitude = lat

        self.hclat = 37.785834
        self.hclong = -122.406417
        self._status = None
        self._output = None

    def check(self, lat, lon):
        new_status = Haversine((self.hclat, self.hclong), (lat,lon)).place_is_empty()
        if self.status != new_status:
            self.status = new_status

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        self.output(self.status)