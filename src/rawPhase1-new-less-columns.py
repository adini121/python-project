#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: Extracts and counts the specified actions from actions.txt files for each test and prints them to CSV file.
    # Takes as input all sessionIds list (from MySQL table) for (major) versions.
# Requirements:
    # Requires to be run inside Python virtualenvironment. All infos: http://docs.python-guide.org/en/latest/dev/virtualenvs/)
        # Installation: $ pip install virtualenv
        # Create a virtual environment in the project directory: $ virtualenv venv
        # Activate a virtual environment: $ source venv/bin/activate
    # All additional requirements are specified in ./python_scripts/requirements.txt.
    # To install the requirements, simply run '$ pip install -r requirements.txt'

import csv,os,sys
from collections import Counter
from mysql_connection import MysqlPython

homedir = os.environ['HOME'] # home directory of user
filename = os.path.basename(__file__) # name of current file

# Directory in which all output files are to be stored. If desired, 'output_file_directory' can be changed to preferred directory.
output_file_directory = homedir + '/' + 'PythonScriptsOutput' + '/'
check_output_dir_exists = os.path.isdir(output_file_directory)
try:
    if check_output_dir_exists is False:
        os.mkdir(output_file_directory)
except OSError:
    print "Error while creating output directory"

############################################# Present help menu on the CLI  #############################################

# Presents help menu to the user to illustrate usage options
all_arguments = sys.argv
help_commands = ['help', '--help', '-h']
try:
    if all_arguments[1] in help_commands:
        print (100 * '='),'\n', (40 * ' '), "H E L P - M E N U", (40 * ' '),'\n', (100 * '-')
        print "usage(): python %s" % filename ,'\n', (100 * '-') ,'\n', "Sample inputs and required parameters:" ,'\n', (100 * '-')
        print  """\nInput the information (one-by-one) as following:
                 \n1. SessionIds database name for the chosen application: amo_sessionIDs
Each application has a separate database in which SessionIds for each application version are stored as a MySQL table. \n## For all database names, refer to './sessionIds_database_names.md'
                 \n2. SessionIds table name for the desired (major) version: sessionids_2015_04_25 \n## For all database names, refer to './sessionIds_table_names.md'
                 \n3. Directory name in which action files are stored (including trailing slashes): %s/ActionFiles/
All actions.txt files from `{sessionId}.tar.xz` files can be extracted using following command \n$ for file in *tar.xz; do gtar -xvf $file -C %s/ActionFiles/ --wildcards */actions.txt; done \n## Example actions file: %s/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
                 \n4. Application's major version: amo_mv1 \n## Used for selecting/deselecting rows of a MySQL table for a particular version.
## For all application major version names, refer to './application_major_version_names_for_database_selection.md' and './mysql_connection.py'
                 \n5. Output filename: amo-mv1-test-metrics. \n## Example output file: amo-mv1-test-metrics.csv
[Note] All output files are stored in directory %s \nThis directory can be changed with parameter 'output_file_directory' from within the scripts.""" % (homedir,homedir,homedir,output_file_directory), '\n',(100 * '-')
        exit()
except IndexError:
    pass

############################################# Present main menu on the CLI  #############################################

# Presents main menu to the user to illustrate possible options
print (100 * '=')
print (40 * ' '), "M A I N - M E N U", (40 * ' ')
print (100 * '-')
print "For executing this script: python %s" % filename
print "\nFor help regarding input parameters, please execute: python %s --help" % filename
print "The --help option presents detailed information about the usage, including examples."
print (100 * '-')
print """# Description: Extracts and counts the specified actions (in terms of metrics) from actions.txt files for each test and prints them to CSV file.
# Requirements:
    # Requires to be run inside Python virtualenvironment. All infos: http://docs.python-guide.org/en/latest/dev/virtualenvs/
        # Installation: $ pip install virtualenv
        # Create a virtual environment in the project directory: $ virtualenv venv
        # Activate a virtual environment: $ source venv/bin/activate
    # All additional requirements are specified in ./python_scripts/requirements.txt.
        # To install the requirements, simply run '$ pip install -r requirements.txt'"""
print (100 * ' '), '\n', (44 * '*'), "User Inputs", (44 * '*')

############################################# Get Inputs from User #############################################
#
def get_database_input():
    """
    Gets MySQL sessionId database name input from the user.

    For all database names, refer to './sessionIds_database_names.md'
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

def get_table_name_input():
    """
    Gets MySQL sessionId table name input from the user.

    For all table names, refer to './sessionIds_table_names.md'
    Example table name: sessionids_2015_04_25
    """
     # Get input through 'raw_input'
    table_name = raw_input("\n2. SessionIds table name for the desired (major) version: ")
    # Connect to MySQL database
    connect_mysql_table = MysqlPython('localhost', 'root', '', database_name)
    # Check if SQL table exists
    table_exists = connect_mysql_table.check_table_exists(table_name)
    return table_exists, table_name

check_table_exists,sessionId_table_name = get_table_name_input()
# Re-ask for input in case input is incorrectly specified
while check_table_exists is False:
    print "Please Re-enter the correct table name."
    check_table_exists, sessionId_table_name = get_table_name_input()

def get_action_files_directory():
    """
    Gets actions.txt files directory name input from the user.

    Example actions file: /Users/$USER/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
    """
     # Get input through 'raw_input'
    action_files_directory = raw_input("\n3. Directory name in which action files are stored (including trailing slashes): ")
    # Check if directory is present
    dir_exists = os.path.isdir(action_files_directory)
    return dir_exists, action_files_directory

check_dir_exists,action_files_directory = get_action_files_directory()
# Re-ask for input in case input is incorrectly specified
while check_dir_exists is False:
    print "Following directory does not exist: ", action_files_directory
    print "Please re-enter the valid actions files directory."
    check_dir_exists,action_files_directory = get_action_files_directory()

# Get major version of the application. Example: amo_mv1. For all application major version names, refer to './application_major_version_names_for_database_selection.md'
# Get input through 'raw_input'
applications_major_version_database = raw_input("\n4. Application's major version: ")
# Get output file name, such as amo-mv1-test-metrics. Example output file: amo-mv1-test-metrics.csv
# Get input through 'raw_input'
output_file_name = raw_input("\n5. Output filename: ")

print (100 * ' '), '\n', (41 * '*'), "Ongoing script execution", (41 * '*'), '\n'

########################################## Start of the script's main logic ############################################

def extract_action_file_contents(sessionId, action_file_dir):
    """
    Reads the contents of action.txt file, takes as input the sessionId and action files directory.

    :param sessionId: Browser SessionId of a test.
    :param action_file_dir: Directory where action files are stored.
    :return: All contents of action.txt file

    Example:
        Sample action_file_dir: /Users/$USER/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
    """
    # Read contents of actions.txt files
    try:
        file_contents=open(action_file_dir + '/' + sessionId + '/' + 'actions.txt').read()
        return file_contents

    except:
        print "==== Error! Please check if following actions file exists : ", action_file_dir + '/' + sessionId + '/' + 'actions.txt', "===="

def return_raw_actions(file_contents):
    """
    Parses the action file contents and returns a list of actions.

    :param file_contents: All contents of action.txt file
    :return: List of all actions

    Example:
        Sample input file_contents = Session 8849abf6-2375-44cb-8b4a-767a32102824 {
                        actions : {
                        ...
                        [8849abf6-2375-44cb-8b4a-767a32102824, getCookies {sessionId=1205d76c-6281-4477-8df6-147fe99c325e}],
                        [8849abf6-2375-44cb-8b4a-767a32102824, setTimeout findElement {using="name", value="name"}],
                        ...
                        }

        Sample output of list of all actions: [... 'getCookies {sessionId=1205d76c-6281-4477-8df6-147fe99c325e}', 'findElement {using="name", value="name"}'...]
    """
    actions_list = []
    # Parse the action file contents
    actions = file_contents.split(' {', 1)[1].split('\n,')
    total_length = range(len(actions))
    for number in total_length:
        data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
        length = len(data)
        total_action = range(length)
        # Return the actions in the form of a list
        for i in total_action:
            action = data[i].split(',', 1)[1]
            actions_list.append(action)
    return actions_list


def count_by_action_type(file_contents):
    """
    Parses the 'list of actions' returned by the function return_raw_actions().

    :param file_contents: All contents of action.txt file
    :return: Two lists findElement_list and other_actions_list

    Example:
        Sample output (as dictionaries):
        findElement_list: {('findElement', 'name'): 1, ('findElements', 'xpath'): 2, ('findElement', 'xpath'): 16, ('findChildElement', 'xpath'): 4, ('findElement', 'css selector'): 4}
        other_actions_list: {'sendKeysToElement': 5, 'clickElement': 8, 'implicitlyWait': 1, 'get': 1}
    """

    # Get list of actions from the action file contents
    data = return_raw_actions(file_contents)

    # Define element locator actions to be extracted from the list of actions. Example: findElement {using="name", value="name"}
    findElementsDictionary = {
    'findChildElement':'using',
    'findChildElements':'using',
    'findElement':'using',
    'findElements':'using'}

    # Define WebDriver actions to be extracted from the list of actions. Example: clickElement {id="2"}
    other_actions=['clickElement',
    'sendKeysToElement',
    'implicitlyWait',
    'get']

    findElement_list= []
    other_actions_list = []

    # Extracting specified actions from the list of actions
    for item in data:
        items = item.split('{')
        action = items[0].replace(' ', '')
        if action in findElementsDictionary and action not in other_actions :
            splitter = findElementsDictionary[action] + '="'
            element = items[1].split(splitter)[1].split('",')[0]
            tuple = (action, element)
            findElement_list.append(tuple)
        elif action in other_actions:
            other_actions_list.append(action)
    # return the two extracted lists (as dictionaries)
    return dict(Counter(findElement_list)), dict(Counter(other_actions_list))


def merge_dictionary(contents):
    """
    Merges element locator actions list to output a nested dictionary of 'findElement+findElements' to 'Element' dictionary and 'findChildElement+findChildElements'
    to 'ChildElement' dictionary. This was originally created to separate children element - the idea was that only findChildElement(s) methods
    are used for locating structure based elements. After detailed inspection of actions.txt files - it turned out that apart from these two methods
    even the findElement(s) methods are used for locating structure based elements.

    :param contents: element locator actions dictionary
        Example:
            contents: {'findElements': {'css selector': '0', 'xpath': '0', 'tag name': '0'}, 'findChildElements': {'css selector': '0', 'xpath': '0', 'tag name': '0'},
            'findElement': {'xpath': 29, 'partial link text': '0', 'class name': '0', 'link text': '0', 'name': 1, 'css selector': 4, 'tag name': '0', 'id': '0'},
            'findChildElement': {'css selector': '0', 'xpath': 1, 'tag name': '0'}}

    :return: dictionaries Element and childElement after merging
        Example:
            Merged dictionary:  {'ChildElement': {'css selector': 0, 'xpath': 1, 'tag name': 0},
            'Element': {'xpath': 29, 'partial link text': '0', 'class name': '0', 'link text': '0', 'name': 1, 'css selector': 4, 'tag name': 0, 'id': '0'}}
    """

    # Dictionary containing merged dictionaries ('findElement+findElements' to 'Element' dictionary
    # and 'findChildElement+findChildElements' to 'ChildElement' dictionary)
    dictionary = {
    'Element': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
    'ChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
    }

    for item, elements in dictionary.items():
        # For findElement and findElements actions
        if item == "Element":
            for element in elements:
                try:
                    one = contents["findElement"][element]
                    two = contents["findElements"][element]
                    dictionary["Element"][element] = int(one) + int(two)
                except KeyError:
                    dictionary["Element"][element] = contents["findElement"][element]
        # For findChildElement and findChildElements actions
        if item == "ChildElement":
            for element in elements:
                try:
                    one = contents["findChildElement"][element]
                    two = contents["findChildElements"][element]
                    dictionary["ChildElement"][element] = int(one) + int(two)
                except KeyError:
                    dictionary["ChildElement"][element] = contents["findChildElement"][element]
    return dictionary

def process_data_for_csv(elementdict, exception):
    """
    Processes the output data to be printed to a CSV file by trimming the whitespaces and arranging the data according to the column
    names (headers) of the file. Outputs the entire data as a dictionary.

    :param elementdict: Element locator actions dictionary, which is returned from return_raw_actions() by get_dictionary()
    :param exception: WebDriver actions dictionary, which is returned from return_raw_actions() by get_dictionary()
    :return: Dictionary containing number of each element locator and WebDriver action.

    Example:
        Sample output dictionary for a test: {'xpath': 12, 'name': 2, 'get': 7, 'clickElement': 11, 'id': 0, 'classname': 0, 'cssselector': 9,
        'sendKeysToElement': 3, 'linktext': 0, 'tagname': 0, 'partiallinktext': 0, 'implicitlyWait': 1}
    """
    dictionary = {}
    for key, value in elementdict.items():
        # process the data according to column name of the csv file
        for element in value:
            title = element.replace(' ', '')
            if dictionary.get(title) is None:
                dictionary[title] = int(value[element])
            else:
                past_value = int(dictionary[title])
                dictionary[title] = past_value + int(value[element])

   # For WebDriver actions other than element locator actions
    dictionary.update(exception)
    return dictionary

def get_dictionary(file_contents):
    """
    Processes the two extracted list of actions returned by the function count_by_action_type(). Creates a dictionary from the
    processed lists which is later output to a CSV file.

    :param file_contents: All contents of action.txt file
    :return: Dictionary of the extracted actions including element location and webdriver actions
    """

    # Define element locator actions to be extracted in the form of dictionary from the extracted list of actions.
    dictionary = {
        'findChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
        'findChildElements': {"css selector":"0", "xpath":"0", "tag name":"0"},
        'findElement': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
        'findElements': {"css selector":"0", "xpath":"0", "tag name": "0"}
    }

    # Define webdriver actions to be extracted in the form of dictionary from the extracted list of actions.
    exception = {'get' : '0',
      'implicitlyWait' : '0',
      'clickElement': '0',
      'sendKeysToElement': '0'}

    # Update both dictionaries according to the data obtained from actions.txt files
    findElement_count_dict,other_actions_count_dict=count_by_action_type(file_contents)
    for key, value in findElement_count_dict.items():
        dictionary[key[0]].update({key[1]: value})
    for key, value in other_actions_count_dict.items():
        exception[key] = value

    # Merging findElements and findElement actions
    dictionary = merge_dictionary(dictionary)
    # Preparing the data for printing to a CSV file
    dictionary = process_data_for_csv(dictionary, exception)
    return dictionary

def get_all_processed_contents(major_version_database, ref_sessionId_table_name, action_files_directory):
    """
    Gets all the data for counting and printing the number of element locators and webdriver actions (e.g. clickElement) and returns a list
    of these contents.

    :param major_version_database: Major version name for selecting the sessionIds of an application, e.g. jenkins_core_mv1
    :param ref_sessionId_table_name: MySQL table name for reference major version of an application, e.g. for Jenkins version 1.609 -> sessionids_1_609
    :param action_files_directory: Directory in which actions.txt files are stored.
    :return: List of all actions to be printed to CSV file
    """

    # Connect to MySQL database in which sessionIds are stored. SessionIds for each version are stored as a MySQL table. Return list of all sessionIds from this table.
    try:
        list_of_ref_sessionIds= connect_mysql.select_major_version_database(major_version_database, ref_sessionId_table_name)
    except:
        print "==== MySQL ERROR : Please check if the MySQL table name and major-version information is correct. ===="
        print "==== Database Table: ", ref_sessionId_table_name, " | ", "Major version: ", major_version_database, "===="

    # Return actions for each test
    if list_of_ref_sessionIds:
        all_contents = []
        rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
        for i in rows_in_ref_sessionId_table:
            ref_action_file_contents = extract_action_file_contents(list_of_ref_sessionIds[i], action_files_directory)
            dictionary= get_dictionary(ref_action_file_contents)
            all_contents.append(dictionary)
        return all_contents

def write_in_csv(content_list,out_file_name,output_file_directory):
    """
    Writes the count of element locator and WebDriver actions for each test of the test-suite to an output CSV file.

    :param content_list: Contents i.e. list of actions obtained from get_all_processed_contents()
    :param out_file_name: Name of the output CSV file
    :param output_file_directory: Directory where the output files are to be stored
    :return: Result of writing (success or failure)
    """
    # Headers for printing to CSV file
    fields = ['xpath','partiallinktext','classname','linktext','name','cssselector','tagname','id',
              'sendKeysToElement','implicitlyWait','get','clickElement']

    # Contents to be printed to CSV file
    if content_list:
        try:
            with open(output_file_directory + '/' + out_file_name + '.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for dictionary in content_list:
                    try:
                        writer.writerow(dictionary)
                        success = True
                    except:
                        print "==== Error while printing the output to file ===="
                return success
        except:
            print "==== IOError: File-write error ===="

######################## Database connection, function calls and printing the result to console ###########################

# Connect to MySQL database in which sessionIds are stored
connect_mysql = MysqlPython('localhost', 'root', '', database_name)


######################################################################################################
# connect_mysql = MysqlPython('localhost', 'root', '', 'jenkins_plugins_sessionIDs')
# action_files_directory = "/Users/adityanisal/Dropbox/ActionFiles/"
# applications_major_version_database = 'jenkins_plugins_mv3'
# sessionId_table_name='sessionids_1_609'
# output_file_name='JenkinsPluginsMV3'
######################################################################################################

# Get all the data for counting and printing the number of element locators and webdriver actions
content_list = get_all_processed_contents(applications_major_version_database, sessionId_table_name, action_files_directory)
# Print output to CSV file
success = write_in_csv(content_list, output_file_name, output_file_directory)

# Re-run message to run the program if unsuccessful
if success is True:
    print (100 * '-'), '\n', "The action counts are successfully extracted to file:", output_file_directory + output_file_name + '.csv', '\n', (100 * '=')
else:
    print (100 * '-'), '\n', (20 * ' '), "Please re-run the program with correct inputs. ", '\n', (100 * '=')