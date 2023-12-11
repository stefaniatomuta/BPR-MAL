import datetime

class FrameworkDetails(object):
    def __init__(self, releaseDate, eol, lts):
        self.releaseDate = releaseDate
        self.eol = eol
        self.lts = lts
    def end_of_life(self) -> bool:
        if isinstance(self.eol, bool):
            return self.eol
        eol_date = datetime.datetime.strptime(self.eol, "%Y-%m-%d")
        return eol_date < datetime.datetime.now()

class FrameworkInfo(object):
    def __init__(self, type, cycle, isEndOfLife):
        self.type = type
        self.cycle = cycle
        self.isEndOfLife = isEndOfLife
