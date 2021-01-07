# To Adjust Ableton Project Breakdown
# Project structure: {'Name': name, 'Date Created': sec since epoch, 'Finished?' Yes/No, 'Track Title': title, 'Sent To': [artists]}
# TODO: Features - Add search by finished, sort by date created, search by artist sent to, add mention of new added projects and prompt to update status
# TODO: Improvements - fix alphanumeric sorting after adding new projects to list, improve date created

import json
import os

CONFIG_FILENAME = 'ableton_config.json'

PROJECT_BREAKDOWN_FILENAME = 'ableton_project_breakdown.json'

# File path in which this python script (and therefore config file) runs, [:-21] removes file name from path
BASE_FILE_PATH = __file__[:-21]

CONFIG_FILE_PATH = BASE_FILE_PATH + '/' + CONFIG_FILENAME


def load_projects():
    items = _return_list_of_contents(project_directory)
    list_of_projects = []
    for item in items:
        list_of_projects.append(item)
    return list_of_projects


def _return_list_of_contents(directory):
    contents = []
    for item in os.listdir(directory):
        item_path = directory + '/' + item
        if os.path.isfile(item_path) and item != 'Desktop.ini' and item.endswith('.als'):
            contents.append({'name': item[:-4], 'creation_date': os.path.getctime(item_path)})
        elif os.path.isdir(item_path) and item != 'Ableton Project Info' and item != 'Backup' and item != 'Samples':
            for inner_item in _return_list_of_contents(item_path):
                contents.append(inner_item)
    return contents


def _save_json_file(file, file_path):
    """Saves a json file to disk in the default user data directory with a given file path."""
    with open(file_path, 'w') as outfile:
        outfile.write(json.dumps(file))


def _load_json_file(file_path):
    """Reads a generic json file with a given file path. Returns None if the given file path is invalid."""
    if file_path is not None and os.path.isfile(file_path):
        with open(file_path, 'r') as infile:
            return json.loads(infile.read())


config_file = _load_json_file(CONFIG_FILE_PATH)

breakdown_file_path = config_file[0]['project_breakdown_file_path']

# This is the directory where the actual Ableton projects are stored
project_directory = config_file[1]['ableton_project_directory']

project_list = _load_json_file(breakdown_file_path + '/' + PROJECT_BREAKDOWN_FILENAME)

projects = load_projects()

if project_list is None:
    # We need to create a new one
    json_to_save = []
    for project in projects:
        json_to_save.append({'Name': project['name'], 'Date Created': project['creation_date'], 'Finished': 'No', 'Track Title': 'NA', 'Sent To': []})
    _save_json_file(json_to_save, breakdown_file_path + '/' + PROJECT_BREAKDOWN_FILENAME)
    project_list = json_to_save
elif len(project_list) != len(projects):
    # New Ableton projects have been created since our last running of this script, so we need to add them
    for project in projects:
        if project not in project_list:
            project_list.append(project)

break_cond = False

while not break_cond:
    what_to_do = input(
        '\nHello and welcome to the Ableton Project Breakdown Updater! What would you like to do today? \n\tU: Update project \n\tP: Print all projects \n\tQ: Quit \n- ')

    if what_to_do.lower() == 'q':
        break_cond = True
    else:
        if what_to_do.lower() == 'u':
            update_break = False
            while not update_break:
                project_to_update = input('\nWhich of your Ableton Projects would you like to update? (case sensitive, not including .als suffix, "B" to go back): ')
                if project_to_update.lower() == 'b':
                    update_break = True
                else:
                    found_project = None
                    found_index = None
                    for project_index in range(len(project_list)):
                        potential_match = project_list[project_index]
                        if potential_match['Name'] == project_to_update:
                            found_project = potential_match
                            found_index = project_index

                    if found_index is None:
                        print(f'\nYou have no Ableton Projects entitled {project_to_update}, please try again.')
                    else:
                        found_project['Finished'] = input('Has this project been finished? (Yes or No): ')
                        found_project['Track Title'] = input('What is the title of the track? (NA if the track does not have a title yet) ')
                        sent_prompt = 'What are the names of the artist(s) you have sent this track to? (one at a time, NA to exit or if you haven\'t sent this track to anyone) '
                        sent_break = False
                        while not sent_break:
                            sent = input(sent_prompt)
                            if sent.lower() == 'na':
                                sent_break = True
                            else:
                                found_project['Sent To'].append(sent)

                        project_list[found_index] = found_project

                        _save_json_file(project_list, breakdown_file_path + '/' + PROJECT_BREAKDOWN_FILENAME)

                        print('\nSuccess!')

        elif what_to_do.lower() == 'p':
            print('\n')
            for project in project_list:
                print(project['Name'])
