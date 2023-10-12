import json

j = '[{"cycle": "4.8.1", "releaseDate": "2022-08-09", "eol": false, "lts": false}, {"cycle": "4.8", "releaseDate": "2019-04-18","eol": "2027-01-12","lts": false}]'
class FrameworkDetails(object):
    def __init__(self, cycle, releaseDate, eol, lts):
        self.cycle = cycle
        self.releaseDate = releaseDate
        self.eol = eol
        self.lts = lts

data = json.loads(j)
framework_details = [FrameworkDetails(fd['cycle'], fd['releaseDate'], fd['eol'], fd['lts']) for fd in data]

print(framework_details[1].cycle)
print(framework_details[1].releaseDate)
print(framework_details[1].eol)
print(framework_details[1].lts)