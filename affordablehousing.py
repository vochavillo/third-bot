import requests
import csv
from csv import DictReader
from urllib.parse import urlencode


def fetch_affordable_data():
    url = 'https://data.sfgov.org/api/views/9rdx-httc/rows.csv?accessType=DOWNLOAD'
    resp = requests.get(url)
    txt = resp.text
    myreader = csv.DictReader(txt.splitlines())
    records = list(myreader)
    return records

def fetch_inclusionary_data():
    url = 'https://data.sfgov.org/api/views/i9x4-xhtt/rows.csv?accessType=DOWNLOAD'
    resp = requests.get(url)
    txt = resp.text
    myreader = csv.DictReader(txt.splitlines())
    records = list(myreader)
    return records

def make_map_url(markers):
    base_url = 'https://maps.googleapis.com/maps/api/staticmap?'
    MAP_SIZE = '800x400'
    coordinate_pairs = []
    my_params = {'size': MAP_SIZE, 'markers': coordinate_pairs}
    coordinate_pairs = ["%s,%s" % (q, markers[q]) for q in markers.keys()]
    preq = requests.PreparedRequest()
    preq.prepare_url(base_url, {'size': MAP_SIZE, 'markers': coordinate_pairs})
    my_url = preq.url
    return my_url

def get_latitude(pair):
    lat = ''
    coordinate_int = pair[1:-1]
    comma_index = coordinate_int.index(',')
    lat_end = comma_index
    lat = coordinate_int[0:lat_end]
    return lat

def get_longitude(pair):
    lon = ''
    coordinate_int = pair[1:-1]
    comma_index = coordinate_int.index(',')
    lon_start = comma_index + 2
    lon = coordinate_int[lon_start:]
    return lon

def affordable_list():
    affordable_dict = {}
    record = fetch_affordable_data()
    for i in record:
        if len(i['Project Location']) > 0:
            pair = i['Project Location']
            latitude = get_latitude(pair)
            longitude = get_longitude(pair)
            affordable_dict[latitude] = longitude
        else:
            pass
    return affordable_dict


def parse_pair(pair_string):
    start_index = pair_string.index('(')
    lat_long = pair_string[start_index:]
    return lat_long

def inclusionary_list():
    inclusionary_list = {}
    record = fetch_inclusionary_data()
    for i in record:
        if len(i['Location']) > 0:
            if '(' in i['Location'] and ')' in i['Location']:
                pair = i['Location']
                lat_lon_pair = parse_pair(pair)
                latitude = get_latitude(lat_lon_pair)
                longitude = get_longitude(lat_lon_pair)
                inclusionary_list[latitude] = longitude
        else:
            pass
    return inclusionary_list

def both_affordable_inclusionary():
    match = []
    affordable = affordable_list()
    inclusionary = inclusionary_list()
    afflist = []
    inclist = []
    match_dict = {}
    for a in affordable.keys():
        afflist.append(a)
    for a in inclusionary.keys():
        inclist.append(a)
    for a in afflist:
        if a in inclist:
            match.append(a)
    for a in match:
        match_aff_long = affordable[a]
        match_inc_long = inclusionary[a]
        num1 = float(match_aff_long)
        num2 = float(match_inc_long)
        if num1 == num2:
            match_dict[float(a)] = num1
    return match_dict

def check_progress():
    count = 0
    progress_dict = {}
    record = fetch_inclusionary_data()
    for r in record:
        progress_label = r['Project Status']
        if progress_label not in progress_dict.keys():
            progress_dict.setdefault(progress_label, 1)
        else:
            progress_dict[progress_label] += 1
    return progress_dict

def earliest_inclusionary_project():
    record = fetch_inclusionary_data()
    sortedprojects = sorted(record,key=sort_foo)
    return sortedprojects[1]

def sort_foo(inclusionary_list):
    return datetime.strptime(inclusionary_list['Planning Approval Date'], '%m/%d/%Y')

def main():
    affordable_inclusionary_housing_dict = both_affordable_inclusionary()
    aff_inc_count = len(affordable_inclusionary_housing_dict.items())
    print('The inclusionary housing program in San Francisco began in 1992 and requires any new housing developments of 10 or more units to set aside a subset of all units as affordalbe housing units, or otherwise pay a fee.')
    if aff_inc_count > 0:
        map_url = make_map_url(match_dict)
        count = len(match_dict.keys())
        print('There are ' + count + ' housing projects that are both affordable and that include the inclusionary requirements. Here is a map showing where these affordable-accessible projects are located in San Francisco.')
    else:
        print('There are no recorded housing projects in San Francisco that meet the inclusionary housing requirements.')

    progress = check_progress()

    print('Here is an update of the progress and count of all the housing developents that include the inclusionary housing requirement:')
    for p in progress.keys():
        status = p
        count = str(progress[p])
        print(status + ' : ' + count)

    earliest_project = earliest_inclusionary_project()

    rest_of_story = """

    The earliest project dates back to {date}, when its planning was approved. It was completed on {date2} and is located on {address}.

    """

    story = rest_of_story.format(
    date = earliest_project['Planning Approval Date'],
    date2 = earliest_project['Completion Date'],
    address = earliest_project['Location']
    )

    print(story)




main()
