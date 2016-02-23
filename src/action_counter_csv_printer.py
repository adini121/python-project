import csv

from collections import Counter

from mysql_connection import MysqlPython

def extract_action_file_contents(sessionId, action_file_dir):
    """ This function extracts the contents of action file , takes as input the sessionId and action files directory"""
    try:
        file_content=open(action_file_dir + sessionId + '/' + 'actions.txt').read()
        # print file_content
        return file_content

    except:
        print "======================================================== Following sessionID file does not exist : ", sessionId + '/' + 'actions.txt', "======================================================="

def return_raw_actions(file_contents):
    actions_list = []
    actions = file_contents.split(' {', 1)[1].split('\n,')
    total_length = range(len(actions))
    for number in total_length:
        data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
        dictionary = {}
        length = len(data)
        total_action = range(length)
        for i in total_action:
            action = data[i].split(',', 1)[1]
            actions_list.append(action)
    return actions_list


def count_by_action_type(file_contents):
    data = return_raw_actions(file_contents)
    # print data

    findElementsDictionary = {
    'findChildElement':'using',
    'findChildElements':'using',
    'findElement':'using',
    'findElements':'using'}

    other_actions=['clickElement',
    'sendKeysToElement',
    'implicitlyWait',
    'get']

    findElement_list= []
    other_actions_list = []
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

    return dict(Counter(findElement_list)), dict(Counter(other_actions_list))


def get_dictionary(file_contents):
    dictionary = {
        'findChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
        'findChildElements': {"css selector":"0", "xpath":"0", "tag name":"0"},
        'findElement': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
        'findElements': {"css selector":"0", "xpath":"0", "tag name": "0"}
    }

    exception = {'get' : '0',
      'implicitlyWait' : '0',
      'clickElement': '0',
      'sendKeysToElement': '0'}

    findElement_count_dict,otherActions_count_dict=count_by_action_type(file_contents)
    for key, value in findElement_count_dict.items():
        dictionary[key[0]].update({key[1]: value})
    for key, value in otherActions_count_dict.items():
        exception[key] = value
    # for merging elements and element
    dictionary = merge_dictionary(dictionary)
    # for getting processed data for the csv
    dictionary = process_data_for_csv(dictionary, exception)
    return dictionary

"""I will be back in 5 mins and knock you here. >> Ok
"""
def merge_dictionary(contents):
    dictionary = {
    'Element': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
    'ChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
    }

    for item, elements in dictionary.items():
        if item == "Element":
            for element in elements:
                try:
                    one = contents["findElement"][element]
                    two = contents["findElements"][element]
                    dictionary["Element"][element] = int(one) + int(two)
                except KeyError:
                    dictionary["Element"][element] = contents["findElement"][element]
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
    dictionary = {}
    for key, value in elementdict.items():
        # proces the data according to column name
        for element in value:
            if key != "ChildElement":
                title = element.replace(' ', '')
                dictionary[title] = value[element]
            if key == "ChildElement":
                title = element.replace(' ', '')
                dictionary["Child" + title] = value[element]

    # For exception one
    dictionary.update(exception)

    return dictionary

def write_in_csv(content_list,out_file_name):
    fields = ['Childcssselector', 'Childxpath', 'Childtagname', 'xpath', 'partiallinktext',
              'classname', 'linktext', 'name', 'cssselector', 'tagname', 'id',
              'sendKeysToElement', 'implicitlyWait', 'get','clickElement']
    # dictionary= get_dictionary(file_contents)
    try:
        with open('/Users/adityanisal/Dropbox/ExtractedResultFiles/CSV/'+out_file_name+'.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for dictionary in content_list:
                writer.writerow(dictionary)
            print "--success--"
    except IOError:
        "==================== ERROR: Filewrite error ===================="


def get_all_processd_contents(major_version_database, ref_sessionId_table_name):
    action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"
    try:
        list_of_ref_sessionIds= connect_mysql.select_major_version_database(major_version_database, ref_sessionId_table_name)
    except IOError:
        print "ERROR : Reference table does not exist :", ref_sessionId_table_name

    try:
        all_contents = []
        rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
        for i in rows_in_ref_sessionId_table:
            ref_action_file_contents = extract_action_file_contents(list_of_ref_sessionIds[i], action_files_dir)
            dictionary= get_dictionary(ref_action_file_contents)
            all_contents.append(dictionary)
        return all_contents

    except:
        print "#################################################### TABLE ERROR: Please check if given reference table exists: ", ref_sessionId_table_name



""" SesionId database names for each app """
# === Jenkins core ====
jenkins_core_database = 'jenkins_core_sessionIDs'
# ==== Jenkins plugins ====
jenkins_plugins_database = 'jenkins_plugins_sessionIDs'
# ====  Moodle ====
moodle_database = 'moodle_sessionIDs'
# === Moodle Reordered ===
moodle_reordered_database = 'reordered_moodle_sessionIDs'
# ====  Fireplace (Mozilla Marketplace) ====
fireplace_database = 'fireplace_sessionIDs'
# ====  AMO (Addons Mozilla) ====
amo_database = 'amo_sessionIDs'
# ====  Bedrock (Mozilla.org) ====
bedrock_database = 'bedrock_sessionIDs'

"""  Major and minor version sql table names for each application for connecting to database """
############################################## Jenkins ##############################################
# Jenkins core MV1
jenkins_core_MV1_reference_version_sessionId_table= 'sessionids_1_580'

# Jenkins core MV2
jenkins_core_MV2_reference_version_sessionId_table = 'sessionids_1_596_new'

# Jenkins core MV3
jenkins_core_MV3_reference_version_sessionId_table = 'sessionids_1_609'

# Jenkins core MV4
jenkins_core_MV4_reference_version_sessionId_table = 'sessionids_1_625'


############################################## Moodle ##############################################
# Moodle MV1
moodle_reference_version_sessionId_table= 'sessionids_230_beta_fin'

# Moodle Reordered
moodle_reordered_reference_version_sessionId_table='sessionids_230_beta_reordered'
############################################## Fireplace (Mozilla Marketplace) ##############################################
# Fireplace MV1
fireplace_mv1_reference_version_sessionId_table='sessionids_mv1_2014_12_16'

# Fireplace MV2
fireplace_mv2_reference_version_sessionId_table='sessionids_MV2_2015_02_10'

# Fireplace MV3
fireplace_mv3_reference_version_sessionId_table='sessionids_MV3_2015_07_07'

# Fireplace MV4
fireplace_mv4_reference_version_sessionId_table='sessionids_MV4_2015_11_02'

############################################## AMO ##############################################
# AMO MV1
amo_mv1_reference_version_sessionId_table='sessionids_2015_01_01'

#AMO MV2
amo_mv2_reference_version_sessionId_table='sessionids_2015_04_25'

#AMO MV3
amo_mv3_reference_version_sessionId_table='sessionids_2015_07_31'

############################################## Bedrock (Mozilla.org) ##############################################
#Bedrock MV1
bedrock_mv1_reference_version_sessionId_table='sessionids_mv1_2015_01_13'



""" !!! Input parameters: Select DATABASE name !!! """
# connect_mysql = MysqlPython('localhost', 'root', '', amo_database)
# action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"
#
# main('amo_mv1', fireplace_mv4_reference_version_sessionId_table)
connect_mysql = MysqlPython('localhost', 'root', '', fireplace_database)
action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"
# content_list =
# main('fireplace_mv1', fireplace_mv4_reference_version_sessionId_table)

content_list = get_all_processd_contents('fireplace_mv3', fireplace_mv3_reference_version_sessionId_table)
write_in_csv(content_list,"fireplace-mv3")