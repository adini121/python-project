#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: Takes as input sessionIds of reference (major) version and corresponding minor versions.
#              For each pair of reference and comparable sessionId, parses as well as compares corresponding action files states.
#              Outputs state-level differences GUI-level differences
# Requirements:
# ImageMagick's command line 'convert utility: http://www.imagemagick.org/script/convert.php
# Installation: http://www.imagemagick.org/script/binary-releases.php
# Ubuntu: sudo apt-get install imagemagick
# OS X: brew install imagemagick
# Requires to be run inside Python virtualenvironment. All infos: http://docs.python-guide.org/en/latest/dev/virtualenvs/)
# Installation: $ pip install virtualenv
# Create a virtual environment in the project directory: $ virtualenv venv
# Activate a virtual environment: $ source venv/bin/activate
# All additional requirements are specified in ./python_scripts/requirements.txt.
# To install the requirements, simply run '$ pip install -r requirements.txt'

import re, os, platform
import subprocess, sys
from humanfriendly.tables import format_pretty_table
from mysql_connection import MysqlPython

homedir = os.environ['HOME']  # home directory of user
filename = os.path.basename(__file__)  # name of current file
osplatform = platform.system()  # current OS platform

############################################# H E L P - M E N U  #############################################

# Presents help menu to the user to illustrate usage options
all_arguments = sys.argv
help_commands = ['help', '--help', '-h']
try:
    if all_arguments[1] in help_commands:
        print (100 * '='), '\n', (40 * ' '), "H E L P - M E N U", (40 * ' '), '\n', (100 * '-')
        print "usage(): python %s" % filename, '\n', (
        100 * '-'), '\n', "Sample inputs and required parameters:", '\n', (100 * '-')
        print  "\nInput the information (one-by-one) as following:"
        print "1. SessionIds database name for the chosen application: jenkins_plugins_sessionIDs"
        print "## For all database names, refer to './sessionIds_database_names.txt'"
        print "\n2. SessionIds table name for the desired reference (major) version: sessionids_1_609"
        print "## For all table names, refer to './sessionIds_table_names.txt'"
        print "\n3. SessionIds table names for the desired comparable (minor) version: sessionids_1_611"
        print "## For all table names, refer to './sessionIds_table_names.txt'"
        print "\n4. Directory name in which action files are stored (including trailing slashes): %s/ActionFiles/"  % (homedir)
        print "## Example actions file: %s/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt"  % (homedir)
        print "\n5. Directory name in which screenshot files are stored (including trailing slashes): %s/ScreenShots/"""  % (homedir)
        print "## Examples:"
        print "-- Screenshots directory: %s/ScreenShots/sessionId(s)/" % (homedir)
        print "-- Screenshot directory structure for a sessionId '02731bd6-60df-44d2-98d3-a80d992197c5': %s/ScreenShots/02731bd6-60df-44d2-98d3-a80d992197c5/*.png" % (homedir)
        print """-- Directory and file structure:
         ├── 02731bd6-60df-44d2-98d3-a80d992197c5 <------ sessionId
             └── screenshots
                 ├── 127a286f-9930-4276-8e8c-350ecd89b5a6.png
                 ├── .
                 ├── .
                 └── f22b4a1a-fdd5-45f5-8126-4f66789d6e7f.png"""
        print """\n6. Application's major version: jenkins_plugins_mv3 \n## For all application major version names, refer to './application_major_version_names.txt'
                 \n7. Application name (as prefix for output files): JenkinsPlugins. \n## Example output file: JenkinsPlugins_1_609_1_611_Results.txt
                 \n============ For additional details, please refer to README.md ============ """, '\n', (100 * '-')
        print (100 * '-')
        exit()
except IndexError:
    pass

############################################# M A I N - M E N U  #############################################

# Presents main menu to the user to illustrate possible options
print (100 * '=')
print (40 * ' '), "M A I N - M E N U", (40 * ' ')
print (100 * '-')
print "For executing this script: python %s" % filename
print "\nFor help regarding input parameters, please execute: python %s --help" % filename
print "The --help option presents detailed information about the usage, including examples."
print (100 * ' '), '\n', (44 * '*'), "User Inputs", (44 * '*')

#############################################  Get Inputs from User #############################################
def get_database_input():
    """
    Gets MySQL sessionId database name input from the user.

    For all database names, refer to './sessionIds_database_names.txt'
    Example database name: amo_sessionIDs
    """
    # Get input through 'raw_input'
    database_name = raw_input("\n1. SessionIds database name for the chosen application: ")
    # Connect to MySQL database
    connect_mysql = MysqlPython('localhost', 'root', '', database_name)
    connected = connect_mysql.check_open()
    return connected, database_name


is_connected, database_name = get_database_input()
# Re-ask for input in case input is incorrectly specified
while is_connected is False:
    print "Please Re-enter the correct database name."
    is_connected, database_name = get_database_input()


def get_ref_table_name_input():
    """
    Gets MySQL sessionId table name input for reference major version from the user.

    For all table names, refer to './sessionIds_table_names.txt'
    Example table name: sessionids_2015_04_25
    """
    # Get input through 'raw_input'
    ref_table_name = raw_input("\n2. SessionIds table name for the desired reference version: ")
    # Connect to MySQL database
    connect_mysql_table = MysqlPython('localhost', 'root', '', database_name)
    # Check if SQL table exists
    table_exists = connect_mysql_table.check_table_exists(ref_table_name)
    return table_exists, ref_table_name


check_table_exists, ref_table_name = get_ref_table_name_input()
# Re-ask for input in case input is incorrectly specified
while check_table_exists is False:
    print "Please Re-enter the correct reference table name."
    check_table_exists, ref_table_name = get_ref_table_name_input()


def get_comparable_versions_table_list_input():
    """
    Gets MySQL sessionId table name input from the user.

    For all table names, refer to './sessionIds_table_names.txt'
    Example table name: sessionids_2015_04_25
    """
    # Get input through 'raw_input' as list of MySQL table names
    tables_list = raw_input(
        "\n3. SessionIds table names for the desired comparable (minor) version"
        "\n[Note: please specify inputs with spaces in between. Example: 'input1 input2 .. inputN']: ")
    cmp_table_list = tables_list.split()
    # Connect to MySQL database
    connect_mysql_table = MysqlPython('localhost', 'root', '', database_name)

    for cmp_table_name in cmp_table_list:
        # Check if SQL table exists
        comp_table_exists = connect_mysql_table.check_table_exists(cmp_table_name)
        if not comp_table_exists:
            print "Table %s Does not exist. Please Re Enter the Table Name"
            return get_comparable_versions_table_list_input()
    return cmp_table_list

comp_table_list = get_comparable_versions_table_list_input()


def get_action_files_directory():
    """
    Gets actions.txt files directory name input from the user.

    Example actions file: /Users/$USER/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
    """
    # Get input through 'raw_input'
    action_files_directory = raw_input(
        "\n4. Directory name in which action files are stored (including trailing slashes): ")
    # Check if directory is present
    dir_exists = os.path.isdir(action_files_directory)
    return dir_exists, action_files_directory


check_dir_exists, action_files_directory = get_action_files_directory()
# Re-ask for input in case input is incorrectly specified
while check_dir_exists is False:
    print "Following directory does not exist: ", action_files_directory
    print "Please re-enter the valid actions files directory."
    check_dir_exists, action_files_directory = get_action_files_directory()


def get_screenshots_files_directory():
    """
    Gets 'sessionId/screenshots/*.png' screenshots files directory name input from the user.

    Example screenshots directory: /Users/$USER/ScreenShots/sessionId/*.png files
    Example screenshots file for sessionId 02731bd6-60df-44d2-98d3-a80d992197c5:
                /Users/$USER/ScreenShots/02731bd6-60df-44d2-98d3-a80d992197c5
                                         └── screenshots
                                             └── 127a286f-9930-4276-8e8c-350ecd89b5a6.png
    """
    # Get input through 'raw_input'
    screenshot_files_directory = raw_input(
        "\n5. Directory name in which screenshots files are stored (including trailing slashes): ")
    # Check if directory is present
    screenshot_dir_exists = os.path.isdir(screenshot_files_directory)
    return screenshot_dir_exists, screenshot_files_directory


screenshot_dir_exists, screenshot_files_directory = get_screenshots_files_directory()
# Re-ask for input in case input is incorrectly specified
while screenshot_dir_exists is False:
    print "Following directory does not exist: ", screenshot_files_directory
    print "Please re-enter the valid actions files directory."
    screenshot_dir_exists, screenshot_files_directory = get_screenshots_files_directory()

# Get major version of the application. Example: amo_mv1. For all application major version names, refer to './application_major_version_names.txt'
applications_major_version_database = raw_input("\n6. Please enter the application's major version: ")
# Fabricate output file name using application name as prefix, such as JenkinsPlugins.
application_name = raw_input("\n7. Please enter the application name: ")

print (100 * ' '), '\n', (41 * '*'), "Ongoing script execution", (41 * '*'), '\n'


def extract_action_file_contents(sessionId, action_file_dir):
    """
    Reads the contents of action.txt file, takes as input the sessionId and action files directory.

    :param sessionId: Browser SessionId of a test.
    :param action_file_dir: Directory where actions.txt files are stored.
    :return: All contents of action.txt file
    :raises: File read error if actions.txt file for given sessionId does not exist in given directory.

    Example:
        Sample action_file_dir (on OS X): /Users/$USER/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
    """
    # Read contents of actions.txt files
    try:
        file_content = open(action_file_dir + '/' + sessionId + '/' + 'actions.txt').read()
        return file_content
    except IOError:
        print "==== Error! Please check if following actions file exists : ", action_file_dir + '/' + sessionId + '/' + 'actions.txt', "===="


def return_actions_dict(file_contents):
    """
    Returns the actions in the form of a dictionary, takes as input the contents of action file

    :param file_contents: All contents of action.txt file
    :return: All actions (States) in the form of a dictionary
    """
    main_dict = {}
    # Parse the action file contents
    total_actions = file_contents.split(' {', 1)[1].split('\n,')
    total_number_of_actions = range(len(total_actions))
    for action_number in total_number_of_actions:
        data = total_actions[action_number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '',1).split('],\n', -1)
        dictionary = {}
        data_length = len(data)
        total_number_of_sub_actions = range(data_length)
        # Return the actions in the form of a dictionary
        for i in total_number_of_sub_actions:
            dictionary[i] = data[i].split(',', 1)[1].split('{', 1)[0].replace(' ', '')
        main_dict[action_number] = dictionary
    return main_dict


def get_the_action_id(file_contents):
    """
    Returns the 'id' of an action (State) from the actions.txt file. This enables to map current-state and next-states.
    :param file_contents: All contents of action.txt file
    :return: 'id' of an action (State)

    Example:
        id : cd79feb9-ca8c-449b-adb2-27517d0b2b75 <----- Grab and Return this id.
        nextStateId : Some(61307eda-9821-43c0-a5a6-e05956629bf7)
    """
    # Parse for the 'id' of an action
    reg_current_id = re.findall('\}\\n\sid\s\:\s(.*?)\s\\n\snextStateId', file_contents, re.DOTALL | re.MULTILINE)
    return reg_current_id


def do_comparison(screenshots_directory, output_files_directory, app_name, ref_sessionId_table_name,
                  comp_sessionId_table_name, test_number, ref_sessionId, comp_sessionId, actions_in_reference_sessionId,
                  actions_in_comp_sessionId, id_of_action_in_ref_sessionId_action_file,
                  id_of_action_in_comp_sessionId_action_file):
    """
    Compares two action files to compare state-based and visual differences.

    :param screenshots_directory: Directory in which the screenshots for each sessionId are stored. Format: /screenshots_directory/sessionId/screenshot(s).png
                                    Example: /screenshots_directory/02731bd6-60df-44d2-98d3-a80d992197c5
                                            ├── 02731bd6-60df-44d2-98d3-a80d992197c5
                                                └── screenshots
                                                    ├── 127a286f-9930-4276-8e8c-350ecd89b5a6.png
                                                    ├── .
                                                    ├── .
                                                    └── f22b4a1a-fdd5-45f5-8126-4f66789d6e7f.png
    :param output_files_directory: Directory in which output '.txt' and '.png' files are to be stored (output to)
    :param app_name: Name of the application, e.g. Jenkins, Mozilla_Addons etc.
    :param ref_sessionId_table_name: MySQL table name in which sessionId for a major reference version are stored, Example table (for Jenkins 1.609): sessionids_1_609
    :param comp_sessionId_table_name: MySQL table name in which sessionId for a minor comparable version are stored, Example table (for Jenkins 1.611): sessionids_1_611
    :param test_number: Test number obtained from the column 'id' of a table
    :param ref_sessionId: Browser sessionId of a test for reference major version
    :param comp_sessionId: Browser sessionId of a test for minor comparable version
    :param actions_in_reference_sessionId: All actions from actions.txt file for reference major version
    :param actions_in_comp_sessionId: All actions from actions.txt file for minor comparable version
    :param id_of_action_in_ref_sessionId_action_file: 'id' of an action from actions.txt file for reference major version, e.g. (id : cd79feb9-ca8c-449b-adb2-27517d0b2b75)
    :param id_of_action_in_comp_sessionId_action_file: 'id' of an action from actions.txt file for minor comparable version
    :return:

    The State-based comparison results are passed on to 'generate_output()' function to be printed as '.txt' files.
    For the State-level comparison, f all the states are matched exactly, the 'Test Result' reflects entry '0', else '1'.
    The number of reference and comparison actions are also printed to the '.txt' files, along with corresponding sessionIds and action Ids (useful for further comparison)

    Example state-level comparison:
        -------------------------------------------------------------------------------------------------------------------------------------------
        | Test # | Test Result | #ref_actions | #comp_actions | ref sessionId      | comp sessionId     | ref action Id      | comp action Id     |
        -------------------------------------------------------------------------------------------------------------------------------------------
        |      0 |           1 |           40 |            40 | b5ddfd32-d8fc-4671 | ca0b0714-56cc-4c2a | 937c781d-397f-4ea4 | 6ee76322-0529-4973 |
        |      . |           . |           .  |            .  |         .          |         .          |        .           |         .          |
        |      . |           . |           .  |            .  |         .          |         .          |        .           |         .          |
        |      n |           . |           .  |            .  |         .          |         .          |        .           |         .          |
        -------------------------------------------------------------------------------------------------------------------------------------------

    The visual (GUI-level) differences are output in the form of '.png' images. Screenshots of reference major version GUI state and a comparable minor version
    GUI state are juxtaposed. For this purpose, the command line tool 'convert' by imagemagick is used.
    The '.png' file names are formed by concatenating the (Name of the application) + (Reference Major version name) + (Minor version name) + (Test Number) + (.png)

    Example GUI-level output filename:
        JenkinsPlugins_1_609_1_611_Test_16.png
        where, Name of the application = JenkinsPlugins, Reference Major version name = 1_609 (Jenkins 1.609) and Minor version name = 1_611 (Jenkins 1.611), Test Number = 16

    """
    # Perform checks for number of states for reference and comparable sessionId (test)
    if len(actions_in_reference_sessionId) > len(actions_in_comp_sessionId):
        number_of_actions_in_reference_sessionId = range(len(actions_in_reference_sessionId))
        reference_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        comp_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
    elif len(actions_in_reference_sessionId) == len(actions_in_comp_sessionId):
        number_of_actions_in_reference_sessionId = range(len(actions_in_reference_sessionId))
        reference_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        comp_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
    else:
        print "==== Caution! Reference sessionId has less number of states! Please check if correct tests are being compared! ===="
    # Get number of states for reference and comparable sessionId (test)
    num_of_ref_actions = '%d' % (len(actions_in_reference_sessionId))
    num_of_comp_actions = '%d' % (len(actions_in_comp_sessionId))

    list = []
    print "Generating GUI level image comparison results for test number ", test_number, ". . ."
    for key in number_of_actions_in_reference_sessionId:

        # Compare GUI-level state differences. Makes use of Imagemagick's convert (http://www.imagemagick.org/script/convert.php)

        # Check which OS platform is being used for determining the full path of Imagemagick convert.
        #
        # if osplatform == 'Darwin': # Mac OS X
        #     imagemagick_convert_path = "/usr/local/bin/convert"
        # elif osplatform == 'Linux': # Linux distributions
        #     imagemagick_convert_path = "/usr/bin/convert"
        #
        # num = '%d' % (test_number)
        # imgDir = screenshots_directory
        # outDir = output_files_directory + '/'
        # outFileName = app_name  + '_'+ ref_sessionId_table_name[11:] + '_' + comp_sessionId_table_name[11:] + '_Test_' + num  + '.png'
        # outFile = outDir + outFileName
        # ref_screenshot = imgDir + ref_sessionId + '/screenshots/'+ id_of_action_in_ref_sessionId_action_file[-1] + '.png'
        # comp_screenshot = imgDir + comp_sessionId + '/screenshots/'+ id_of_action_in_comp_sessionId_action_file[-1] + '.png'
        # try:
        #     p = subprocess.Popen([imagemagick_convert_path, "+append", ref_screenshot ,comp_screenshot, outFile],stdout=subprocess.PIPE)
        #     return_code = p.wait()
        #     if return_code > 0:
        #         raise Exception('==== Imagemagick convert error ! ====')
        # except OSError:
        #     print "==== There was an error in printing out the file %s ! ===="


        # Compare state-level actions for reference major version and comparable minor version
        ref_action = []
        comp_action = []
        try:
            assert reference_sessionId_action[0][key] == comp_sessionId_action[0][key]
            list.append(0)
        except AssertionError:
            ref_action = reference_sessionId_action[0][key]
            comp_action = comp_sessionId_action[0][key]
            list.append(1)
            break
        except KeyError:
            list.append(1)
            break

    # Output '0' if all actions (states) match exactly. Otherwise output '1'.
    if 1 in list:
        result = '1'
    else:
        result = '0'

    actions_difference = ''
    if ref_action and comp_action:
        actions_difference = '\n' + (
        30 * '=') + 'As Test Result is "1" for test number %s, please see below the comparison of states.' % (
        test_number) + (30 * '=') + '\nState-level (action) differences for test number ' + '%d' % (
        test_number) + ': \n'  # , ref_action, comp_action
        actions_difference = actions_difference + 'Reference major version:\n'
        actions_difference = actions_difference + '%s' % str(ref_action) + '\n' + (100 * '-') + '\n'
        actions_difference = actions_difference + 'Comparable minor version:\n'
        actions_difference = actions_difference + '%s' % str(comp_action)

    state_level_comparison_results = [test_number, result, num_of_ref_actions, num_of_comp_actions, ref_sessionId,
                                      comp_sessionId]
    return state_level_comparison_results, actions_difference


def get_all_data_of_session(sessionId, directory):
    """
    :param sessionId: Browser SessionId of a test.
    :param directory: Directory where actions.txt files are stored.
    :return: Actions from actions.txt files in the form of a dictionary, 'id' of an action (State)
    """
    # Read the contents of action.txt
    file_contents = extract_action_file_contents(sessionId, directory)
    actions = return_actions_dict(file_contents) # Get the actions in the form of a dictionary
    action_id = get_the_action_id(file_contents) # Get the 'id' of an action (State)
    return actions, action_id


def generate_output(screenshots_directory, output_files_directory, major_version_database, ref_sessionId_table_name,
                    comp_sessionId_table_name, action_files_dir, app_name):
    """
    Generates state-based and visual comparison differences.

    Outputs State-level differences to '.txt' files and GUI-level visual differences
    The '.txt' file names are formed by concatenating the (Name of the application) + (Reference Major version name) + (Minor version name) + (Results.txt)
    Example output '.txt' file name:
        JenkinsPlugins_1_609_1_611_Results.txt
        where, Name of the application = JenkinsPlugins, Reference Major version name = 1_609 (Jenkins 1.609) and Minor version name = 1_611 (Jenkins 1.611)

    :param screenshots_directory: Directory in which the screenshots for each sessionId are stored. [Detailed description in :param:screenshots_directory: in docstring for do_comparison()]
    :param output_files_directory: Directory in which output '.txt' and '.png' files are to be stored (output to)
    :param major_version_database: Major version name for selecting the sessionIds of an application, e.g. jenkins_core_mv1
    :param ref_sessionId_table_name: MySQL table name for reference major version of an application, e.g. for Jenkins version 1.609 -> sessionids_1_609
    :param comp_sessionId_table_name: MySQL table name for comparable minor version of an application, e.g. for Jenkins version 1.611 -> sessionids_1_611
    :param action_files_dir: Directory in which actions.txt files are stored.
    :param app_name: Name of the application, e.g. JenkinsPlugins, Moodle etc.
    """
    # Connect to MySQL database in which sessionIds are stored. SessionIds for each minor version are stored as a MySQL table. Return list of all sessionIds from this table.
    try:
        list_of_ref_sessionIds = connect_mysql.select_major_version_database(major_version_database,
                                                                             ref_sessionId_table_name)
    except:
        print "==== MySQL ERROR : Please check if following table exists :", ref_sessionId_table_name, "===="

    try:
        list_of_comp_sessionIds = connect_mysql.select_major_version_database(major_version_database,
                                                                              comp_sessionId_table_name)
    except:
        print "==== MySQL ERROR : Please check if following table exists :", comp_sessionId_table_name, "===="

    # Headers for printing state-level comparison output to '.txt' files.
    column_names = ['Test Number', 'Test Result', 'Num_actions_ref', 'Num_actions_comp', 'Reference_version_sessionId',
                    'Comparable_version_sessionId']
    final_list = []
    action_differences_dictionary = []
    # Compare each sessionId actions for reference and comparable versions
    try:
        if len(list_of_ref_sessionIds) == len(list_of_comp_sessionIds):
            rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
            for i in rows_in_ref_sessionId_table:
                ref_action_file_data = get_all_data_of_session(list_of_ref_sessionIds[i], action_files_dir)
                comp_action_file_data = get_all_data_of_session(list_of_comp_sessionIds[i], action_files_dir)
                state_level_comparison_results, action_differences_string = do_comparison(screenshots_directory,
                                                                                          output_files_directory,
                                                                                          app_name,
                                                                                          ref_sessionId_table_name,
                                                                                          comp_sessionId_table_name,
                                                                                          i,
                                                                                          list_of_ref_sessionIds[i],
                                                                                          list_of_comp_sessionIds[i],
                                                                                          actions_in_reference_sessionId=
                                                                                          ref_action_file_data[0],
                                                                                          actions_in_comp_sessionId=
                                                                                          comp_action_file_data[0],
                                                                                          id_of_action_in_ref_sessionId_action_file=
                                                                                          ref_action_file_data[1],
                                                                                          id_of_action_in_comp_sessionId_action_file=
                                                                                          comp_action_file_data[1])
                final_list.append(state_level_comparison_results)
                if action_differences_string != '':
                    action_differences_dictionary.append(action_differences_string)

            # Prints results in a tabular form to '.txt' file. Table format is according to 'humanfriendly tabels' (https://humanfriendly.readthedocs.org/en/latest/#module-humanfriendly.tables)
            with open(output_files_directory + '/' + app_name + '_' + ref_sessionId_table_name[11:] + '_' + comp_sessionId_table_name[11:] + '_Results.txt',
                      'w+') as resultfile:
                print >> resultfile, (format_pretty_table(final_list, column_names))
                for action_differences_string in action_differences_dictionary:
                    print >> resultfile, action_differences_string
                print "Generating state-level comparison results for all tests . . ."
                success = True
                return success
        else:
            print "==== CAUTION! reference sessionId table: ", ref_sessionId_table_name, "and comparable sessionId table:", comp_sessionId_table_name, "have different number of rows ===="
            print "==== Please verify whether both versions are intended to be compared against each other. ===="
    except:
        print "==== MySQL ERROR : Please check if all the MySQL database related information is correct. ===="
        print "==== For additional details please refer to ./mysql_connection.py ===="


# Directory in which all output files are to be stored. If desired, 'output_file_directory' can be changed to preferred directory.
output_file_directory = homedir + '/' + 'PythonScriptsOutput'
check_output_dir_exists = os.path.isdir(output_file_directory)
try:
    if check_output_dir_exists is False:
        os.mkdir(output_file_directory)
except OSError:
    print "Error while creating output directory"

# Connect to MySQL database in which sessionIds are stored
connect_mysql = MysqlPython('localhost', 'root', '', database_name)

##############################################################################
jenkins_plugins_MV3_reference_version_sessionId_table = 'sessionids_1_609'
jenkins_plugins_MV3_compare_version_sessionId_table_list = ['sessionids_1_611']
# connect_mysql = MysqlPython('localhost', 'root', '', 'jenkins_plugins_sessionIDs')
# action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"
# screenshots_directory = '/Users/adityanisal/ImageFiles/'
# for table in jenkins_plugins_MV3_compare_version_sessionId_table_list:
#     success=generate_output(screenshots_directory, output_file_directory, 'jenkins_plugins_mv3', jenkins_plugins_MV3_reference_version_sessionId_table, table, action_files_dir, 'JenkinsTest')
###############################################################################

# Generate state-based and visual comparison differences and output status log to console.
for table in comp_table_list:
    success = generate_output(screenshot_files_directory, output_file_directory, applications_major_version_database,
                              ref_table_name, table, action_files_directory, application_name)

# Re-run message to run the program if unsuccessful
if success is True:
    print (
    100 * '-'), '\n', "Success! The state-level comparison results are successfully output to directory:", output_file_directory, '\n', (
    100 * '=')
else:
    print (100 * '-'), '\n', (10 * ' '), "Please re-run the program with correct inputs. ", '\n', (100 * '=')
