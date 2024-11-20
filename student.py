from datetime import date, time#

class Student:
    """A stdent class as a base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False


    def full_name(self):
        return f"{self._first_name} {self._last_name}"
