#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: Extracts and counts the specified actions from actions.txt file and prints them to CSV file.
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

############################################# H E L P - M E N U  #############################################


# Presents help menu to the user to illustrate usage options
all_arguments = sys.argv
help_commands = ['help', '--help', '-h']
try:
    if all_arguments[1] in help_commands:
        print (100 * '='),'\n', (40 * ' '), "H E L P - M E N U", (40 * ' '),'\n', (100 * '-')
        print "usage(): python %s" % filename ,'\n', (100 * '-') ,'\n', "Sample inputs and required parameters:" ,'\n', (100 * '-')
        print  """\nInput the information (one-by-one) as following:
                 \n1. SessionIds database name for the chosen application: amo_sessionIDs \n## For all database names, refer to './sessionIds_database_names.txt'
                 \n2. SessionIds table name for the desired version: sessionids_2015_04_25 \n## For all database names, refer to './sessionIds_table_names.txt'
                 \n3. Directory name in which action files are stored (including trailing slashes): %s/ActionFiles/ \n## Example actions file: %s/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
                 \n4. Application's major version: amo_mv1 \n## For all application major version names, refer to './application_major_version_names.txt'
                 \n5. Output filename: mozilla-addons-mv1. \n## Example output file: mozilla-addons-mv1.csv
                 \n============ For additional details, please refer to README.md ============ """ % (homedir,homedir), '\n',(100 * '-')
        exit()
except IndexError:
    pass

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

def get_table_name_input():
    """
    Gets MySQL sessionId table name input from the user.

    For all table names, refer to './sessionIds_table_names.txt'
    Example table name: sessionids_2015_04_25
    """
     # Get input through 'raw_input'
    table_name = raw_input("\n2. SessionIds table name for the desired version: ")
    # Connect to MySQL database
    connect_mysql_table = MysqlPython('localhost', 'root', '', database_name)
    # Check if SQL table exists
    table_exists = connect_mysql_table.check_table_exists(table_name)
    return table_exists, table_name

check_table_exists,table_name = get_table_name_input()
# Re-ask for input in case input is incorrectly specified
while check_table_exists is False:
    print "Please Re-enter the correct table name."
    check_table_exists, table_name = get_table_name_input()

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

# Get major version of the application. Example: amo_mv1. For all application major version names, refer to './application_major_version_names.txt'
# Get input through 'raw_input'
applications_major_version_database = raw_input("\n4. Application's major version: ")
# Get output file name, such as mozilla-addons-mv1. Example output file: mozilla-addons-mv1.csv
# Get input through 'raw_input'
output_file_name = raw_input("\n5. Output filename: ")

print (100 * ' '), '\n', (41 * '*'), "Ongoing script execution", (41 * '*'), '\n'

def extract_action_file_contents(sessionId, action_file_dir):
    """
    Reads the contents of action.txt file, takes as input the sessionId and action files directory.

    :param sessionId: Browser SessionId of a test.
    :param action_file_dir: Directory where action files are stored.
    :return: All contents of action.txt file
    :raises: File read error if actions.txt file for given sessionId does not exist in given directory.

    Example:
        Sample action_file_dir: /Users/$USER/ActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993/actions.txt
    """
    # Read contents of actions.txt files
    try:
        file_content = open(action_file_dir + '/' + sessionId + '/' + 'actions.txt').read()
        return file_content
    except IOError:
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
    :return: Two lists unique_findElement_list and other_webdriver_actions_list

    Example:
        Sample output lists:
        unique_findElement_list: {('findElement', 'css selector'): 82, ('findElement', 'xpath'): 55, ('findChildElement', 'xpath'): 22, ('findElements', 'xpath'): 11, ('findElements', 'css selector'): 7, ('findElement', 'name'): 1}
        other_webdriver_actions: {'clickElement': 314, 'get': 252, 'sendKeysToElement': 128, 'implicitlyWait': 34}
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
    other_webdriver_actions = ['clickElement',
    'sendKeysToElement',
    'implicitlyWait',
    'get']

    findElement_list= []
    other_webdriver_actions_list = []

    # Extracting specified actions from the list of actions
    for item in data:
        items = item.split('{', 1)
        action = items[0].replace(' ', '')
        if action in findElementsDictionary and action not in other_webdriver_actions :
            splitter = findElementsDictionary[action] + '="'
            value_splitter = 'value="'
            value = items[1].split(value_splitter)[1].replace('"}', '', -1)
            element = items[1].split(splitter)[1].split('",')[0]
            element_value = (element, value)
            tuple = (action, element_value)
            findElement_list.append(tuple)
        elif action in other_webdriver_actions:
            other_webdriver_actions_list.append(action)

    # Exclude repeated findElement calls to measure unique element locators
    unique_findElement_list = [(x[0], x[1][0]) for x in set(findElement_list)]

    # return the two extracted lists
    return dict(Counter(unique_findElement_list)), dict(Counter(other_webdriver_actions_list))

def merge_dictionary(contents):
    """
    Merges element locator actions list to output a nested dictionary of 'findElement+findElements' to 'Element' dictionary and 'findChildElement+findChildElements'
    to 'ChildElement' dictionary. This was originally created to separate children element - the idea was that only findChildElement(s) methods
    are used for locating structure based elements. After detailed inspection of actions.txt files - it turned out that apart from these two methods
    even the findElement(s) methods are used for locating structure based elements.

    :param contents: element locator actions dictionary
    Example:
        contents: {'findElements': {'css selector': 7, 'xpath': 11, 'tag name': '0'}, 'findChildElements': {'css selector': '0', 'xpath': '0', 'tag name': '0'}, 'findElement': {'xpath': 55, 'partial link text': '0', 'class name': '0', 'link text': '0', 'name': 1, 'css selector': 82, 'tag name': '0', 'id': '0'}, 'findChildElement': {'css selector': '0', 'xpath': 22, 'tag name': '0'}}
    :return: dictionaries Element and childElement after merging
    Example:
        Merged dictionary:  {'ChildElement': {'css selector': 0, 'xpath': 22, 'tag name': 0},
            'Element': {'xpath': 66, 'partial link text': '0', 'class name': '0', 'link text': '0', 'name': 1, 'css selector': 89, 'tag name': 0, 'id': '0'}}

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
    :param elementdict: Element locator actions dictionary, which is returned from return_raw_actions() by get_dictionary()
    :param exception: WebDriver actions dictionary, which is returned from return_raw_actions() by get_dictionary()
    :return: Dictionary containing number of each element locator and webdriver action.

    Example:
        Sample output dictionary: {'xpath': 66, 'Childcssselector': 0, 'name': 1, 'get': 252, 'Childxpath': 22, 'Childtagname': 0, 'clickElement': 314,
                'id': '0', 'classname': '0', 'cssselector': 89, 'sendKeysToElement': 128,
                'linktext': '0', 'tagname': 0, 'partiallinktext': '0', 'implicitlyWait': 34}
    """
    dictionary = {}
    for key, value in elementdict.items():
        # process the data according to column name
        for element in value:
            title = element.replace(' ', '')
            if dictionary.get(title):
                dictionary[title] = dictionary[title] + value[element]
            else:
                dictionary[title] = value[element]

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

    findElement_count_dict,otherActions_count_dict=count_by_action_type(file_contents)
    for key, value in findElement_count_dict.items():
        dictionary[key[0]].update({key[1]: value})
    for key, value in otherActions_count_dict.items():
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
    action_files_dir = action_files_directory

    # Connect to MySQL database in which sessionIds are stored. SessionIds for each version are stored as a MySQL table. Return list of all sessionIds from this table.
    try:
        list_of_ref_sessionIds= connect_mysql.select_major_version_database(major_version_database, ref_sessionId_table_name)
    except :
        print "==== MySQL ERROR : Please check if the MySQL table name and major-version information is correct. ===="
        print "==== Database Table: ", ref_sessionId_table_name, " | ", "Major version: ", major_version_database, "===="

    # Return actions for all the tests
    if list_of_ref_sessionIds:
        all_contents = []
        contents = ''
        rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
        for i in rows_in_ref_sessionId_table:
            ref_action_file_contents = extract_action_file_contents(list_of_ref_sessionIds[i], action_files_dir)
            contents = contents + ',\n' + ref_action_file_contents
        dictionary = get_dictionary(contents)
        all_contents.append(dictionary)
        return all_contents


def write_in_csv(content_list,out_file_name,output_file_directory):
    """
    Writes (through appending) the count of element locator and WebDriver actions to an output CSV file.

    :param content_list: Contents i.e. list of actions obtained from get_all_processed_contents()
    :param out_file_name: Name of the output CSV file
    :return: Result of writing (success or failure)
    """
    # Headers for printing to CSV file
    fields = [ 'xpath', 'partiallinktext','classname', 'linktext', 'name', 'cssselector', 'tagname', 'id',
              'sendKeysToElement', 'implicitlyWait', 'get','clickElement']

    # Contents to be printed to CSV file
    if content_list:
        try:
            with open(output_file_directory+ '/'+ out_file_name + '.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for dictionary in content_list:
                    try:
                        writer.writerow(dictionary)
                    except IOError:
                        print "==================== Please check input to the CSV file ===================="
                success = True
                return success
        except IOError:
            print "==================== ERROR: Filewrite error ===================="

# Connect to MySQL database in which sessionIds are stored
connect_mysql = MysqlPython('localhost', 'root', '', database_name)

# Directory in which all output files are to be stored. If desired, 'output_file_directory' can be changed to preferred directory.
output_file_directory = homedir + '/' + 'PythonScriptsOutput'
check_output_dir_exists = os.path.isdir(output_file_directory)
try:
    if check_output_dir_exists is False:
        os.mkdir(output_file_directory)
except OSError:
    print "Error while creating output directory"

# Get all the data for counting and printing the number of element locators and webdriver actions
content_list = get_all_processed_contents(applications_major_version_database, table_name, action_files_directory)
# Print to CSV file
success = write_in_csv(content_list,output_file_name,output_file_directory)

# Re-run message to run the program if unsuccessful
if success is True:
    print (100 * '-'), '\n', "The action counts are successfully extracted to file:", output_file_directory + '/' + output_file_name + '.csv', '\n', (100 * '=')
else:
    print (100 * '-'), '\n', (20 * ' '), "Please re-run the program with correct inputs. ", '\n', (100 * '=')

