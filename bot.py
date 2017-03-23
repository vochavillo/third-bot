from affordablehousing import *

def ask_question():
    response = input("Would you like to know about affordable housing in San Francisco? (Y/N): ")
    return response

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

def bot():
    response = ask_question()
    if response == 'Y':
        main()
