import csv
import pickle
import json
from collections import OrderedDict

states_dict = {
        'AK': { 
            'name': 'Alaska',
            'region': 4,
            'division': 9,
            'number': '02',
            },
        'AL': { 
            'name': 'Alabama',
            'region': 3,
            'division': 6,
            'number': '01',
            },
        'AR': { 
            'name': 'Arkansas',
            'region': 3,
            'division': 7,
            'number': '05',
            },
        'AS': { 
            'name': 'American Samoa',
            'region': 9,
            'division': 9,
            },
        'AZ': { 
            'name': 'Arizona',
            'region': 4,
            'division': 8,
            'number': '04',
            },
        'CA': { 
            'name': 'California',
            'region': 4,
            'division': 9,
            'number': '06',
            },
        'CO': { 
            'name': 'Colorado',
            'region': 4,
            'division': 8,
            'number': '08',
            },
        'CT': { 
            'name' : 'Connecticut',
            'region' : 1,
            'division' : 1,
            'number' : '09',
            },
        'DC': { 
            'name' : 'District of Columbia',
            'region' : 3,
            'division' : 5,
            'number' : '11',
            },
        'DE': { 
            'name' : 'Delaware',
            'region' : 3,
            'division' : 5,
            'number' : '10',
            },
        'FL': { 
            'name' : 'Florida',
            'region' : 3,
            'division' : 5,
            'number' : '12',
            },
        'GA': { 
            'name' : 'Georgia',
            'region' : 3,
            'division' : 5,
            'number' : '13',
            },
        'GU': { 
            'name' : 'Guam',
            'region' : 9,
            'division' : 9,
            'number' : '14',
            },
        'HI': { 
                'name' : 'Hawaii',
                'region' : 4,
                'division' : 9,
                'number' : '15',
                },
        'IA': { 
                'name' : 'Iowa',
                'region' : 2,
                'division' : 4,
                'number' : '19',
                },
        'ID': { 
                'name' : 'Idaho',
                'region' : 4,
                'division' : 8,
                'number' : '16',
                },
        'IL': { 
                'name' : 'Illinois',
                'region' : 2,
                'division' : 3,
                'number' : '17',
                },
        'IN': { 
                'name' : 'Indiana',
                'region' : 2,
                'division' : 3,
                'number' : '18',
                },
        'KS': { 
                'name' : 'Kansas',
                'region' : 2,
                'division' : 4,
                'number' : '20',
                },
        'KY': { 
                'name' : 'Kentucky',
                'region' : 3,
                'division' : 6,
                'number' : '21',
                },
        'LA': { 
                'name' : 'Louisiana',
                'region' : 3,
                'division' :7 ,
                'number' : '22',
                },
        'MA': { 
                'name' : 'Massachusetts',
                'region' : 1,
                'division' : 1,
                'number' : '25',
                },
        'MD': { 
                'name' : 'Maryland',
                'region' : 3,
                'division' : 5,
                'number' : '24',
                },
        'ME': { 
                'name' : 'Maine',
                'region' : 1,
                'division' :1 ,
                'number' : '23',
                },
        'MI': { 
                'name' : 'Michigan',
                'region' : 2,
                'division' : 3,
                'number' : '26',
                },
        'MN': { 
                'name' : 'Minnesota',
                'region' : 2,
                'division' : 4,
                'number' : '27',
                },
        'MO': { 
                'name' : 'Missouri',
                'region' : 2,
                'division' :4 ,
                'number' : '29',
                },
        'MP': { 
                'name' : 'Northern Mariana Islands',
                'region' : 9,
                'division' :9 ,
                },
        'MS': { 
                'name' : 'Mississippi',
                'region' : 3,
                'division' : 6,
                'number' : '28',
                },
        'MT': { 
                'name' : 'Montana',
                'region' : 4,
                'division' :8 ,
                'number' : '30',
                },
#        'NA': { name: 'National',
#                region: ,
#                division: ,
#                },
        'NC': { 
                'name' : 'North Carolina',
                'region' :3 ,
                'division' :5 ,
                'number' : '37',
                },
        'ND': { 
                'name' : 'North Dakota',
                'region' : 2,
                'division' :4 ,
                'number' : '38',
                },
        'NE': { 
                'name' : 'Nebraska',
                'region' : 2,
                'division' :4 ,
                'number' : '31',
                },
        'NH': { 
                'name' : 'New Hampshire',
                'region' : 1,
                'division' :1 ,
                'number' : '33',
                },
        'NJ': { 
                'name' : 'New Jersey',
                'region' : 1,
                'division' : 2,
                'number' : '34',
                },
        'NM': { 
                'name' : 'New Mexico',
                'region' : 4,
                'division' :8 ,
                'number' : '35',
                },
        'NV': { 
                'name' : 'Nevada',
                'region' : 4,
                'division' :8 ,
                'number' : '32',
                },
        'NY': { 
                'name' : 'New York',
                'region' : 1,
                'division' :2 ,
                'number' : '36',
                },
        'OH': { 
                'name' : 'Ohio',
                'region' : 2,
                'division' :3 ,
                'number' : '39',
                },
        'OK': { 
                'name' : 'Oklahoma',
                'region' : 3,
                'division' :7 ,
                'number' : '40',
                },
        'OR': { 
                'name' : 'Oregon',
                'region' : 4,
                'division' :9,
                'number' : '41',
                },
        'PA': { 
                'name' : 'Pennsylvania',
                'region' : 1,
                'division' :2 ,
                'number' : '42',
                },
        'PR': { 
                'name' : 'Puerto Rico',
                'region' : 9,
                'division' :9 ,
                'number' : '72',
                },
        'RI': { 
                'name' : 'Rhode Island',
                'region' : 1,
                'division' :1 ,
                'number' : '44',
                },
        'SC': { 
                'name' : 'South Carolina',
                'region' : 3,
                'division' :5 ,
                'number' : '45',
                },
        'SD': { 
                'name' : 'South Dakota',
                'region' : 2,
                'division' :4 ,
                'number' : '46',
                },
        'TN': { 
                'name' : 'Tennessee',
                'region' : 3,
                'division' :6 ,
                'number' : '47',
                },
        'TX': { 
                'name' : 'Texas',
                'region' : 3,
                'division' :7 ,
                'number' : '48',
                },
        'UT': { 
                'name' : 'Utah',
                'region' : 4,
                'division' :8 ,
                'number' : '49',
                },
        'VA': { 
                'name' : 'Virginia',
                'region' : 3,
                'division' :5 ,
                'number' : '51',
                },
        'VI': { 
                'name' : 'Virgin Islands',
                'region' : 9,
                'division' :9 ,
                },
        'VT': { 
                'name' : 'Vermont',
                'region' : 1,
                'division' :1 ,
                'number' : '50',
                },
        'WA': { 
                'name' : 'Washington',
                'region' : 4,
                'division' :9 ,
                'number' : '53',
                },
        'WI': { 
                'name' : 'Wisconsin',
                'region' : 2,
                'division' :3 ,
                'number' : '55',
                },
        'WV': { 
                'name' : 'West Virginia',
                'region' : 3,
                'division' :5 ,
                'number' : '54',
                },
        'WY': { 
                'name' : 'Wyoming',
                'region' : 4,
                'division' :8 ,
                'number' : '56',
                },
}
def get_state_name(state):
    return states_dict[state]['name']

def get_region(state):
    return states_dict[state]['region']

def get_division(state):
    return states_dict[state]['division']

def get_state_number(state):
    return states_dict[state]['number']

bfo = {}

tsv_file = 'ufo_awesome.tsv' 

reader = csv.reader(open(tsv_file), delimiter='\t',)
for row in reader:
    location = row[2]
    location_split = location.split(', ')
    if (len(location_split) < 2):
        continue

    state = location_split[1]
    if not states_dict.get(state):
        continue

    sighted_on = row[0]
    year_sighted = sighted_on[:4]

    if not bfo.get(state):
        bfo[state] = {}
    if not bfo[state].get(year_sighted):
        bfo[state][year_sighted] = 0
    bfo[state][year_sighted] +=1


with open('ufo_by_state.csv', 'wb') as f:
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([ 'Sumlev', 'Region', 'Division', 'State', 'Name',
        'sighting1995', 'sighting1996', 'sighting1997', 'sighting1998',
        'sighting1999', 'sighting2000', 'sighting2001', 'sighting2002',
        'sighting2003', 'sighting2004', 'sighting2005', 'sighting2006',
        'sighting2007', 'sighting2008', 'sighting2009', 'sighting2010'])
    total = {}
    for year in range(1995, 2011):
        total[year] = [0, 0, 0, 0, 0]

    for state in bfo:
        if (get_region(state) > 4):
            continue
        sightings = [];
        for year in range(1995, 2011):
            if not bfo[state].get(str(year)):
                sightings.append(0)
                continue
            sightings.append(bfo[state][str(year)])
            total[year][0] += bfo[state][str(year)]
            total[year][get_region(state)] += bfo[state][str(year)]

        row = ['040', get_region(state), get_division(state),
            get_state_number(state), get_state_name(state)]
        row += sightings
        writer.writerow(row)

    total_us = []
    total_ne = []
    total_mw = []
    total_s = []
    total_w = []
    for year in range(1995, 2011):
        total_us.append(total[year][0])
        total_ne.append(total[year][1])
        total_mw.append(total[year][2])
        total_s.append(total[year][3])
        total_w.append(total[year][4])
    us = ['010', '0', '0', '00', 'United States'] 
    us += total_us
    writer.writerow(us)
    ne = ['020', '1', '0', '00', 'Northeast Region']
    ne += total_ne
    writer.writerow(ne)
    mw = ['020', '2', '0', '00', 'Midwest Region']
    mw += total_mw
    writer.writerow(mw)
    south = ['020', '3', '0', '00', 'South Region']
    south += total_s
    writer.writerow(south)
    west = ['020', '4', '0', '00', 'West Region']
    west += total_w
    writer.writerow(west)
