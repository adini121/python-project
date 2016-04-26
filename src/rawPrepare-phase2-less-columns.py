#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Description: Extracts contents of actions.txt file (for phase-two) for two minor versions. Compares the extracted actions for a set of
    #  repaired metrics (actions). Takes as input all sessionIds list (from MySQL table) for two minor versions. Prints the results (by appending) them to CSV file.
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
# Presents help menu to the user to illustrate usage options
all_arguments = sys.argv
help_commands = ['help', '--help', '-h']
try:
    if all_arguments[1] in help_commands:
        print (100 * '='), '\n', (40 * ' '), "H E L P - M E N U", (40 * ' '), '\n', (100 * '-')
        print "usage(): python %s" % filename, '\n', (
        100 * '-'), '\n', "Sample inputs and required parameters:", '\n', (100 * '-')
        print  "\nInput the information (one-by-one) as following:"
        print "1. SessionIds database name (phase two) for the chosen application: phase_two_jenkins_sids"
        print "Each application has a separate database in which SessionIds for each application version are stored as a MySQL table.", '\n',\
            "## For all database names, refer to './sessionIds_database_names.md'"
        print "\n2. SessionIds table name for the desired version1: sessionids_1_609"
        print "## For all table names, refer to './sessionIds_table_names_phase_two.md'"
        print "\n3. SessionIds table name for the desired version2: sessionids_1_611"
        print "## For all table names, refer to './sessionIds_table_names_phase_two.md'"
        print "\n4. Directory name in which action files are stored (including trailing slashes): %s/PhaseTwoActionFiles/"  % (homedir)
        print "## Example actions file: %s/PhaseTwoActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993.actions.txt"  % (homedir)
        print "\n5. SessionId Table selection parameter for version1:"
        print "# This parameter provides the facility to select or de-select specific rows of sessionId tables for the sake of comparison."
        print "## Example, version1_sql_table_selector = 'id != 9'"
        print "### Resultant query will be -> SELECT session_id FROM sessionids_1_609 where id !=9"
        print "\n6. SessionId Table selection parameter for version2:"
        print "## Example, version1_sql_table_selector = 'id != 11 and id != 18'"
        print "### Resultant query will be -> SELECT session_id FROM sessionids_1_611 where id != 11 and id != 18"
        print """\n7. Output filename: amo-phase2-metrics. \n## Example output file: amo-phase2-metrics.csv
[Note] All output files are stored in directory %s \nThis directory can be changed with parameter 'output_file_directory' from within the scripts."""  % (output_file_directory), '\n', (100 * '-')
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
print """# Description: Extracts contents of actions.txt file (for phase-two) for two minor versions.
Compares the extracted actions for a set of repaired metrics (actions).
Takes as input all sessionIds list (from MySQL table) for two versions.
Prints the results (by appending) them to CSV file.
# Requirements:
    # Requires to be run inside Python virtualenvironment. All infos: http://docs.python-guide.org/en/latest/dev/virtualenvs/
        # Installation: $ pip install virtualenv
        # Create a virtual environment in the project directory: $ virtualenv venv
        # Activate a virtual environment: $ source venv/bin/activate
    # All additional requirements are specified in ./python_scripts/requirements.txt.
        # To install the requirements, simply run '$ pip install -r requirements.txt'"""
print (100 * ' '), '\n', (44 * '*'), "User Inputs", (44 * '*')

############################################# Get Inputs from User #############################################

def get_database_input():
    """
    Gets MySQL sessionId database name input from the user.

    For all database names, refer to './sessionIds_database_names.md'
    Example database name: amo_sessionIDs
    """
    # Get input through 'raw_input'
    database_name = raw_input("\n1. SessionIds database name (phase two) for the chosen application: ")
    # Connect to MySQL database
    connect_mysql = MysqlPython('localhost', 'root', '', database_name)
    connected = connect_mysql.check_open()
    return connected, database_name

is_connected, database_name = get_database_input()
# Re-ask for input in case input is incorrectly specified
while is_connected is False:
    print "Please Re-enter the correct database name."
    is_connected, database_name = get_database_input()

def get_version1_table_name_input():
    """
    Gets MySQL sessionId table name input for version1 from the user.

    For all table names, refer to './sessionIds_table_names_phase_two.md'
    Example table name: sessionids_2015_04_25
    """
    # Get input through 'raw_input'
    version1_table_name = raw_input("\n2. SessionIds table name for the desired version1: ")
    # Connect to MySQL database
    connect_mysql_table = MysqlPython('localhost', 'root', '', database_name)
    # Check if SQL table exists
    table_exists = connect_mysql_table.check_table_exists(version1_table_name)
    return table_exists, version1_table_name

check_table_exists, version1_table_name = get_version1_table_name_input()
# Re-ask for input in case input is incorrectly specified
while check_table_exists is False:
    print "Please Re-enter the correct table name."
    check_table_exists, version1_table_name = get_version1_table_name_input()

def get_version2_table_name_input():
    """
    Gets MySQL sessionId table name input for version2 from the user.

    For all table names, refer to './sessionIds_table_names_phase_two.md'
    Example table name: sessionids_2015_04_25
    """
    # Get input through 'raw_input'
    version2_table_name = raw_input("\n3. SessionIds table name for the desired version2: ")
    # Connect to MySQL database
    connect_mysql_table = MysqlPython('localhost', 'root', '', database_name)
    # Check if SQL table exists
    table_exists_for_version2 = connect_mysql_table.check_table_exists(version2_table_name)
    return table_exists_for_version2, version2_table_name

check_table_exists_for_version2, version2_table_name = get_version2_table_name_input()
# Re-ask for input in case input is incorrectly specified
while check_table_exists_for_version2 is False:
    print "Please Re-enter the correct table name."
    check_table_exists_for_version2, version2_table_name = get_version2_table_name_input()


def get_phase_two_action_files_directory():
    """
    Gets actions.txt files directory name input from the user.

    Example actions file: /Users/$USER/PhaseTwoActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993.actions.txt
    """
    # Get input through 'raw_input'
    phase_two_action_files_directory = raw_input(
        "\n4. Directory name in which action files are stored (including trailing slashes): ")
    # Check if directory is present
    dir_exists = os.path.isdir(phase_two_action_files_directory)
    return dir_exists, phase_two_action_files_directory

check_dir_exists, phase_two_action_files_directory = get_phase_two_action_files_directory()
# Re-ask for input in case input is incorrectly specified
while check_dir_exists is False:
    print "Following directory does not exist: ", phase_two_action_files_directory
    print "Please re-enter the valid actions files directory."
    check_dir_exists, phase_two_action_files_directory = get_phase_two_action_files_directory()

# Parameter that dictates which sessionIds are to be deselected for comparison. For example, version1_sql_table_selector = 'id != 9' deselects the row where primary key 'id' is 9.
# If no table rows are to be deselected, this parameter can be kept empty.
version1_sql_table_selector = raw_input("\n5. SessionId Table selection parameter for version1: ") or ""
version2_sql_table_selector = raw_input("\n6. SessionId Table selection parameter for version2: ") or ""

# Get output file name, such as amo-mv1-test-metrics. Example output file: amo-mv1-test-metrics.csv
# Get input through 'raw_input'
output_file_name = raw_input("\n7. Output filename: ")

########################################## Start of the script's main logic ############################################

def extract_action_file_contents(sessionId, phase_two_action_files_dir):
    """
    Reads the contents of action.txt (for phase-two) file, takes as input the sessionId and action files directory (for phase-two).

    :param sessionId: Browser SessionId of a test.
    :param action_file_dir: Directory where action files are stored for phase-two.
    :return: All contents of action.txt file

    Example:
        Sample action_file_dir: /Users/$USER/PhaseTwoActionFiles/707231c1-b9b3-4d25-8343-ed230be6c993.actions.txt
    """
    # Read contents of actions.txt files
    try:
        file_contents=open(phase_two_action_files_dir + '/' + sessionId + '.' + 'actions.txt').read()
        return file_contents

    except:
        print "==== Error! Please check if following actions file exists : ", phase_two_action_files_dir + '/' + sessionId + '.' + 'actions.txt', "===="

def get_actions_from_file_contents(file_contents):
    """
    Parses the action file contents for element locator and implicit wait actions. Returns element locator in the form of dictionary and
    implicit wait actions in the form of list.

    :param file_contents: All contents of action.txt file for phase-two.
    :return: element locator and implicit wait actions
    """
    # Create a dictionary for actions findElement, findElements, findChildElement, findChildElements
    # Example key-value pair: 'findElements': [('css selector', '.categories li')]
    dictionary = {
       'findElement': [],
       'findElements': [],
       'findChildElement': [],
       'findChildElements': []
    }

    # Create a list for implicitylyWait actions. All times are in ms, as recorded by actions.txt files. Example: [10000.0, 10000.0]
    implicitly_wait = []

    # Parse the file contents for above actions
    items = file_contents.split(']\n')
    for item in items:
        element = item.split(', ', 1)[1].split(' {', 1)
        element_name = element[0]
        element_content = element[1]
        # For element locator actions
        if element_name in dictionary:
            using = element_content.split('using="', 1)[1].split('",', 1)[0]
            value = element_content.split('value="', 1)[1].replace('"}', '')
            tuple = (using, value)
            my_list = dictionary[element_name]
            my_list.append(tuple)

        # For implicit wait actions
        if element_name == "implicitlyWait":
            time = element_content.split('ms=', 1)[1].replace("}", "")
            if float(time) != 0.0:
                implicitly_wait.append(float(time))

    return dictionary, implicitly_wait


def select_unique_element_occurrence_(data):
    """
    Selects unique element locator occurrences by excluding repeated element locator calls to measure unique changes in element locators.
    This logic is helpful since all tests use page-object pattern, and element locator changes are done to the page-objects.
    If all 10 tests of a test-suite use a locator from the page-object, there are 10 occurrences of this locator in 10 action files. If this locator
    is repaired, the idea is to output the change correctly -> not that 10 locators were repaired, but one.
    # Example: if findElement {using="css selector", value="label.privacy} is used by 10 out of 10 tests, and is later changed to
    findElement {using="css selector", value=".privacy-check-label > span"}, this change is to be output as 1 repaired css selector and not 10.

    :param data: Parsed contents of actions.txt files
    :return: List of unique element locator occurrences
    """
    unique_element_list = []
    [unique_element_list.append(item) for item in data if item not in unique_element_list]
    return unique_element_list

def compare_actions_across_two_versions(data1, data2):
    """
    Compares element locator actions to detect the repaired changes in between two versions of the test-suite.

    :param data1: Parsed contents of actions.txt files for version1
    :param data2: Parsed contents of actions.txt files for version2
    :return: Comparison results in the formed of repaired (changed, added and deleted) element locators.
    """
    changed_list = []
    deleted_list = []
    added_list = []

    # For findElement, findElements, for findChildElement, findChildElements actions
    # Remove duplicate entries and get list of actions in the form of a tuple [(action, value)] Example: [('css selector', '.hovercats li')]
    for element in data1:
        actions_list1 = list(select_unique_element_occurrence_(data1[element]))
        actions_list2 = list(select_unique_element_occurrence_(data2[element]))

        # Return first element of tuple - which is the action, e.g. 'css selector'
        actions_list1_number = [x[0] for x in actions_list1]
        actions_list2_number = [x[0] for x in actions_list2]
        number_of_particular_action = range(len(actions_list1))
        # Get the changed tuple. Example: version1 = [('tag name', 'option'), ('css selector', 'li > h3 > a')] and version2 = [('tag name', 'option')],('css selector', 'li')]
        # Output the 'css selector' was changed
        for i in number_of_particular_action:
            if actions_list1[i] not in actions_list2:
                tuple = (element, actions_list1[i][0])
                changed_list.append(tuple)

        # Get the number of occurrences of a particular element locator {'css selector': 3}
        actions_list1_count = Counter(actions_list1_number)
        actions_list2_count = Counter(actions_list2_number)
        # Get the number of added or deleted element locators by type
        for obj in actions_list1_count:
            # Store the number of occurrences
            one = actions_list1_count[obj]
            two = actions_list2_count[obj]
            # Compute the added or deleted diff-set
            if one != two:
                if one > two:
                    tuple = (element, (one-two, obj))
                    deleted_list.append(tuple)
                if two > one:
                    tuple = (element, (two-one, obj))
                    added_list.append(tuple)

    return changed_list, deleted_list, added_list


def print_accordance(diff_type, data):

    """
    Outputs the comparison results (diff-set) of element locators between two versions. If no repaired changes are present, then output "0" element locators
    changed for a particular element locator action.

    :param diff_type: Comparison type of the element locators between two versions: changed, added and deleted element locators
    :param data: Comparison results (diff-set) of element locators between two versions
    :return: Dictionary containing the the comparison results (as numbers)
    """
    # Dictionary for element actions with default diff-sets set to "0". This will be overwritten in case the diff-set number is other than "0".
    dictionary = {
        'findChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
        'findChildElements': {"css selector":"0", "xpath":"0", "tag name":"0"},
        'findElement': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
        'findElements': {"css selector":"0", "xpath":"0", "tag name": "0"}
    }

    # The deleted and added diff-sets are in the form of list of tuples
    # Example: [('findElement', (1, 'css selector')]
    if diff_type in ["deleted", "added"]:
        for key in data:
            dictionary[key[0]].update({key[1][1]: key[1][0]})
        return dictionary

    # The changed diff-sets are in the form of dictionary
    # Example: {('findElement', 'css selector'): 2}
    if diff_type in ["changed"]:
        for key, value in data.items():
            dictionary[key[0]].update({key[1]: value})
        return dictionary


def compare_implicitly_wait(implicitly_wait1, implicitly_wait2):
    """
    Compares if number of implicit waits was added or deleted
    :param implicitly_wait1: Number of implicit wait actions for version1
    :param implicitly_wait2: Number of implicit wait actions for version2
    :return: Diff-set of implicit wait actions
    """

    number_of_implicit_waits1 = len(implicitly_wait1)
    number_of_implicit_waits2 = len(implicitly_wait2)
    return number_of_implicit_waits1 - number_of_implicit_waits2

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


def compare_all(data1, data2):
    """
    Outputs the comparison results (diff-set) of repaired element locators and implicit waits in the form of dictionary.
    :param data1: Parsed contents of actions.txt files for version1
    :param data2: Parsed contents of actions.txt files for version2
    :return: comparison results (diff-set) of element locators and implicit waits in the form of dictionary
    """
    # Get the parsed element locator and implicit wait actions for version1 and version2
    parsed_element_locator_actions1, implicitly_wait1 = get_actions_from_file_contents(data1)
    parsed_element_locator_actions2, implicitly_wait2 = get_actions_from_file_contents(data2)
    # Get the comparison results in the formed of changed, added and deleted element locators
    changed_list, deleted_list, added_list = compare_actions_across_two_versions(parsed_element_locator_actions1, parsed_element_locator_actions2)
    total_changed = Counter(changed_list)
    changed = merge_dictionary(print_accordance("changed", total_changed))
    deleted = merge_dictionary(print_accordance("deleted", deleted_list))
    added   = merge_dictionary(print_accordance("added", added_list))

    # Get the number of implicit waits added or deleted
    implicit_wait_diff = compare_implicitly_wait(implicitly_wait1, implicitly_wait2)

    # Store the element locators and implicit waits diff-sets as a dictionary
    dictionary = {"changed": changed,
                  "deleted": deleted,
                  "added": added,
                  "implicitWaitdiff": implicit_wait_diff}
    return dictionary


def process_data_for_csv(all_dictionary):
    """
    Processes the output data to be printed to a CSV file by trimming the whitespaces and arranging the data according to the column
    names (headers) of the file. Outputs the entire data as a dictionary.

    :param all_dictionary:
    :return:
    """
    dictionary = {}
    for item, elementdict in all_dictionary.items():
        # For element locator actions
        if item in ["changed", "deleted", "added"]:
            for key, value in elementdict.items():
                # process the data according to column name of the csv file
                for element in value:
                    # Headers of csv file
                    title = element.replace(' ', '')
                    # Output the total number of repaired (changed, added, deleted) element actions
                    if dictionary.get(title) is None:
                        dictionary[title] = value[element]
                    else:
                        past_value = int(dictionary[title])
                        dictionary[title] = past_value + int(value[element])
        # For implicit wait actions
        if item in ["implicitWaitdiff"]:
            dictionary[item] = elementdict

    return dictionary


def get_all_processed_contents(version1_sessionId_table_name, version2_sessionId_table_name, phase_two_action_files_dir, version1_sql_table_selector='',version2_sql_table_selector=''):
    """
    :param version1_sessionId_table_name: MySQL table name for version1 of an application, e.g. for Jenkins version 1.609 -> sessionids_1_609
    :param version2_sessionId_table_name: MySQL table name for version1 of an application, e.g. for Jenkins version 1.611 -> sessionids_1_611
    :param phase_two_action_files_dir: Directory where action files are stored for phase-two.
    :param version1_sql_table_selector: For version1 - Parameter that dictates which sessionIds are to be deselected for comparison. For example, querymodifier= 'id != 9' deselects
    :param version2_sql_table_selector: For version2 - Same parameter as above
    :return: Output results ready to be printed to csv file
    """
    try:
        list_of_version1_sessionIds= connect_mysql.select_table_for_phase_two(version1_sessionId_table_name, version1_sql_table_selector)
    except:
        print "==== MySQL ERROR : Please check if following table exists :", version1_sessionId_table_name, "===="

    try:
        list_of_version2_sessionIds= connect_mysql.select_table_for_phase_two(version2_sessionId_table_name, version2_sql_table_selector)
    except:
        print "==== MySQL ERROR : Please check if following table exists :", version2_sessionId_table_name, "===="

    try:
        all_contents = []
        all_version1_action_file_data = ''
        all_version2_action_file_data = ''
        rows_in_version1_sessionId_table = range(len(list_of_version1_sessionIds))
        rows_in_version2_sessionId_table = range(len(list_of_version2_sessionIds))

        # Return actions for the test-suite of version1
        for i in rows_in_version1_sessionId_table:
            version1_action_files_data = extract_action_file_contents(list_of_version1_sessionIds[i], phase_two_action_files_dir)
            all_version1_action_file_data = all_version1_action_file_data + '\n' + version1_action_files_data
        # Return actions for the test-suite of version2
        for i in rows_in_version2_sessionId_table:
            version2_action_file_data = extract_action_file_contents(list_of_version2_sessionIds[i], phase_two_action_files_dir)
            all_version2_action_file_data = all_version2_action_file_data + '\n' + version2_action_file_data

        # Get the comparison results (diff-set) of repaired element locators and implicit waits
        all_dictionary = compare_all(all_version1_action_file_data, all_version2_action_file_data)
        # Process the output data to be printed to a CSV file
        processed_data_csv = process_data_for_csv(all_dictionary)
        all_contents.append(processed_data_csv)
        return all_contents

    except:
        print "==== MySQL ERROR : Please check if the MySQL table name and database information is correct. ===="
        print "==== Database Tables: ", version1_sessionId_table_name, "and", version2_sessionId_table_name, "===="

def write_in_csv(content_list, out_file_name, output_file_directory):
    """
    Writes (through appending) the number of repaired element locator and implicitWait actions of the entire test-suite to an output CSV file.

    :param content_list: Contents i.e. list of actions obtained from get_all_processed_contents()
    :param out_file_name: Name of the output CSV file
    :param output_file_directory: Directory where the output files are to be stored
    :return: Result of writing (success or failure)
    """
    # Headers for printing to CSV file
    fields = ["xpath", "partiallinktext", "classname", "linktext", "name", "cssselector", "tagname", "id", "implicitWaitdiff"]

    # Contents to be printed to CSV file
    if content_list:
        try:
            with open(output_file_directory + '/' + out_file_name + '.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields)
                writer.writeheader()
                for dictionary in content_list:
                    try:
                        writer.writerow(dictionary)
                        success = True
                    except IOError:
                        print "==== Error while printing the output to file ===="
                return success
        except IOError:
            print "==== IOError: File-write error ===="

######################## Database connection, function calls and printing the result to console ###########################

# Connect to MySQL database in which sessionIds are stored
connect_mysql = MysqlPython('localhost', 'root', '', database_name)

######################################################################################################
# connect_mysql = MysqlPython('localhost', 'root', '', 'backup_phase_two_fireplace_sids')
# phase_two_action_files_directory = '/Users/adityanisal/Dropbox/PhaseTwoActionFiles/'
# version1_table_name= 'sessionids_mv1_p2_2015_01_06'
# version2_table_name= 'sessionids_mv1_p2_2015_01_20'
# output_file_name='phase2-fireplace'
# version1_sql_table_selector= 'id != 100'
# version2_sql_table_selector= 'id != 100'
#######################################################################################################

# Get all the data for counting and printing the output
content_list = get_all_processed_contents(version1_table_name, version2_table_name, phase_two_action_files_directory, version1_sql_table_selector, version2_sql_table_selector)
# Print output to CSV file
success = write_in_csv(content_list, output_file_name, output_file_directory)

# Re-run message to run the program if unsuccessful
if success is True:
    print (100 * '-'), '\n', "The action counts are successfully extracted to file:", output_file_directory + output_file_name + '.csv', '\n', (100 * '=')
else:
    print (100 * '-'), '\n', (20 * ' '), "Please re-run the program with correct inputs. ", '\n', (100 * '=')















