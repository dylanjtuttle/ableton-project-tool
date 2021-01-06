# To Adjust Ableton Project Breakdown
# Project row structure: ['Name.als', 'Date Created(?)', 'Finished?', 'Track Title', 'Sent To']
# TODO: Add features like Breakdown (Num finished/unfinished, OF THOSE FINISHED num sent/not sent), List unfinished, Order by rapper (enter rapper's name, see list of songs \
#  you've sent to them), while loops within/'back button' options, switch to .json

import csv

projects = []

with open(r'H:\OneDrive\Battlestation\Art\Beats\Project Breakdown.csv', newline='') as csv_file_read:
    csv_reader = csv.reader(csv_file_read, delimiter=',')
    for row in csv_reader:
        projects.append(row)

name_index = projects[0].index('Project Name')
date_index = projects[0].index('Date Modified')
fin_index = projects[0].index('Finished?')
track_index = projects[0].index('Track Title')
sent_index = projects[0].index('Sent To')

dont_break = True

while dont_break:
    what_to_do = input(
        '\nHello and welcome to the Ableton Project Breakdown Updater! What would you like to do today? \n\tU: Update project \n\tP: Print all projects \n\tN: Quit \n- ')

    if what_to_do.lower() == 'n':
        dont_break = False
    else:
        if what_to_do.lower() == 'u':
            project_to_update = input('\nWhich of your Ableton Projects would you like to update?: ')

            found_project = []
            found_index = None
            for project_index in range(len(projects)):
                proj_attr = projects[project_index]
                if proj_attr[0] == project_to_update:
                    found_project = proj_attr
                    found_index = project_index

            if found_index is None:
                print(f'\nYou have no Ableton Projects entitled {project_to_update}, please try again.')
            else:
                found_project[fin_index] = input('Has this project been finished? (Yes or No): ')
                found_project[track_index] = input('What is the title of the track? (NA if the track does not have a title yet) ')
                found_project[sent_index] = input(
                    'What are the names of the artist(s) you have sent this track to? (comma separated, NA if you haven\'t sent this track to anyone) ')

                projects[found_index] = found_project

                with open(r'H:\OneDrive\Battlestation\Art\Beats\Project Breakdown.csv', 'w', newline='') as csv_file_write:
                    csv_writer = csv.writer(csv_file_write, delimiter=',')
                    for project_row in projects:
                        csv_writer.writerow(project_row)

                print('\nSuccess!')

        elif what_to_do.lower() == 'p':
            print('\n')
            for proj in projects:
                print(proj)
