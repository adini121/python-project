from collections import Counter
from mysql_connection import MysqlPython
import csv

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
            action = data[i].split(',', 1)[1].replace(' ', '')
            actions_list.append(action)
    return actions_list
    # print actions_list

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
    # 'executeScript',
    # 'getPageSource',
    # 'setTimeout',
    # 'getElementText',
    'get']

    findElement_list= []
    other_actions_list = []
    for item in data:
        items = item.split('{')
        action = items[0]
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
        'findChildElement': {"cssselector": "0", "xpath": "0", "tagname": "0"},
        'findChildElements': {"cssselector":"0", "xpath":"0", "tagname":"0"},
        'findElement': {"cssselector":"0", "xpath":"0", "tagname":"0", "name":"0", "classname":"0", "id":"0", "linktext":"0",
                        "partiallinktext":"0"},
        'findElements': {"cssselector":"0", "xpath":"0", "tagname": "0"}
    }

    exception = {'get' : '0',
     'implicitlyWait' : '0',
      'clickElement': '0',
      'sendKeysToElement': '0',
      # 'executeScript': '0',
      # 'getPageSource': '0',
      # 'setTimeout': '0',
      # 'getElementText': '0',
      # 'getTitle': '0'
                 }

    findElement_count_dict,otherActions_count_dict=count_by_action_type(file_contents)
    for key, value in findElement_count_dict.items():
        dictionary[key[0]].update({key[1]: value})
    for key, value in otherActions_count_dict.items():
        exception[key] = value
    return dictionary, exception

def main(major_version_database, ref_sessionId_table_name):
    action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"
    try:
        list_of_ref_sessionIds= connect_mysql.select_major_version_database(major_version_database, ref_sessionId_table_name)
    except IOError:
        print "ERROR : Reference table does not exist :", ref_sessionId_table_name

    try:
        rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
        # with open('/Users/adityanisal/arbit/test2csv.csv', 'w') as csvfile:
        #     try:
        #         writer = csv.writer(csvfile)
        #         writer.writerow('sendKeys', 'clicks', 'waits','gets')
        #         # writer.writerow( ( )
        #         print "SUCCESS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        #     except IOError:
        #         print "File not found"
        for i in rows_in_ref_sessionId_table:
            ref_action_file_contents = extract_action_file_contents(list_of_ref_sessionIds[i], action_files_dir)
            print  "========================================================================================="
            # ref_actions_list = return_raw_actions(ref_action_file_contents)
            findElement_count_dict,otherActions_count_dict=get_dictionary(ref_action_file_contents)
            # print findElement_count_dict
            print "\n"
            # print otherActions_count_dict
            print "Test Number: ",i, "(SessionID:",list_of_ref_sessionIds[i],")"
            print "___________________________________________"
            for key in findElement_count_dict:
                for value in findElement_count_dict[key]:
                    # if added[key][value]!="0":
                    print "Number of" ,key ,"using" ,value, ":" ,findElement_count_dict[key][value]
            print "####################################################"
            for key, value in otherActions_count_dict.items():
                print key, ">>", value
            print "\n"
            for key, value in otherActions_count_dict.items():
                print key, ">>", value


                    # fieldnames = ['tnum', key+"_"+value]
                    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    # writer.writeheader()
                    # writer.writerow('tnum:')

    except:
        print "#################################################### TABLE ERROR: Please check if given reference table exists: ", ref_sessionId_table_name

############################################## Fireplace (Mozilla Marketplace) ##############################################
# Fireplace MV1
fireplace_mv1_reference_version_sessionId_table='sessionids_mv1_2014_12_16'

# Fireplace MV2
fireplace_mv2_reference_version_sessionId_table='sessionids_MV2_2015_02_10'

# Fireplace MV3
fireplace_mv3_reference_version_sessionId_table='sessionids_MV3_2015_07_07'

# Fireplace MV4
fireplace_mv4_reference_version_sessionId_table='sessionids_MV4_2015_11_02'
moodle_reordered_database = 'reordered_moodle_sessionIDs'
# ====  Fireplace (Mozilla Marketplace) ====
fireplace_database = 'fireplace_sessionIDs'


""" !!! Input parameters: Select DATABASE name !!! """
connect_mysql = MysqlPython('localhost', 'root', '', fireplace_database)
action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"

main('fireplace_mv1', fireplace_mv4_reference_version_sessionId_table)
