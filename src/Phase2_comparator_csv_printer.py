import re
import csv

from collections import Counter
from phase2_mysql_connection import Phase2MysqlPython



def extract_p2_action_file_contents(sessionId):
    """ This function extracts the contents of action file , takes as input the sessionId and action files directory"""
    p2_action_file_dir='/Users/adityanisal/Dropbox/PhaseTwoActionFiles/'
    try:
        file_content=open(p2_action_file_dir + sessionId + '.' + 'actions.txt').read()
        return file_content

    except:
        print "======================================================== Following sessionID file does not exist : ", sessionId + '/' + 'actions.txt', "======================================================="

def get_element_dict(data):

    dictionary = {
       'findElement': [],
       'findElements': [],
       'findChildElement': [],
       'findChildElements': []
    }
    get = []
    implicitly_wait = []

    exception = {
      'clickElement': [],
      'sendKeysToElement': [],
      #'setTimeout': [],
    }

    items = data.split(']\n')
    for item in items:
        element = item.split(', ', 1)[1].split(' {', 1)
        element_name = element[0]
        element_content = element[1]
        if element_name in dictionary:
            using = element_content.split('using="', 1)[1].split('",', 1)[0]
            value = element_content.split('value="', 1)[1].replace('"}', '')
            tuple = (using, value)
            my_list = dictionary[element_name]
            my_list.append(tuple)
        if element_name == "get": #Get only the path of [get {url="someurl/path"}]
            get_url=re.findall('get\s\{url\=\"http?:\\/\\/[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+\.[a-zA-Z0-9]+:[a-zA-Z0-9]+(.*?)\}',
                               item.split(', ', 1)[1], re.DOTALL | re.MULTILINE)
            get.append(get_url)
        if element_name in exception:
            exception[element_name].append(1)
        if element_name == "implicitlyWait":
            time = element_content.split('ms=', 1)[1].replace("}", "")
            if float(time) != 0.0:
                implicitly_wait.append(float(time))

    return dictionary, get, exception, implicitly_wait


def set_(data):
    """Remove duplicate element entries"""
    unique = []
    [unique.append(item) for item in data if item not in unique]
    return unique

def print_and_process(data1, data2):
    reorder_list = []
    changed_list = []
    deleted_list = []
    added_list = []
    for element in data1:
        list1 = list(set_(data1[element]))
        list2 = list(set_(data2[element]))
        list1_number = [x[0] for x in list1]
        list2_number = [x[0] for x in list2]
        arange = range(len(list1))
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

        for i in arange:
            try:
                if list1[i] != list2[i]:
                    if list1[i] in list2:
                        tuple = (element, list1[i][0])
                        reorder_list.append(tuple)
                        # print list1[i], i, "ordering has been changed to", list2.index(list1[i]), "in second one"

                    else:
                        tuple = (element, list1[i][0])
                        changed_list.append(tuple)
                        print "Element ",list1[i], " ---Changed to -->", list2[i]
            except IndexError:
                if list1[i] in list2:
                    tuple = (element, list1[i][0])
                    reorder_list.append(tuple)
                    # print list1[i], i, "ordering has been changed to", list2.index(list1[i]), "in second one"
                else:
                    print ""
                    print list1[i], "not present in second data"
        # print list1
        # print "@@@@@@@@@@@"
        # print list2
        list1_count = Counter(list1_number)
        list2_count = Counter(list2_number)
        for obj in list1_count:
            one = list1_count[obj]
            two = list2_count[obj]
            if one != two:
                if one > two:
                    tuple = (element, (one-two, obj))
                    deleted_list.append(tuple)
                if two > one:
                    tuple = (element, (two-one, obj))
                    added_list.append(tuple)

    return reorder_list, changed_list, deleted_list, added_list


def get_deleted_or_added(data):
    """Can be deleted, not used anymore"""
    dictionary = {}
    for obj in data:
        if not obj[1] in dictionary:
            dictionary[obj[1]] = [obj[0]]
        else:
            dictionary[obj[1]].append(obj[0])
    return dictionary

def print_accordance(type, data):
    dictionary = {
        'findChildElement': {"css selector": "0", "xpath": "0", "tag name": "0"},
        'findChildElements': {"css selector":"0", "xpath":"0", "tag name":"0"},
        'findElement': {"css selector":"0", "xpath":"0", "tag name":"0", "name":"0", "class name":"0", "id":"0", "link text":"0",
                        "partial link text":"0"},
        'findElements': {"css selector":"0", "xpath":"0", "tag name": "0"}
    }
    if type in ["deleted", "added"]:
        for key in data:
            dictionary[key[0]].update({key[1][1]: key[1][0]})
        return dictionary
    if type in ["reorder", "changed"]:
        for key, value in data.items():
            dictionary[key[0]].update({key[1]: value})
        return dictionary


def compare_get(get_data1, get_data2):
    """Compare URL paths of two get{url} occurances"""
    changed_1 = []
    changed_2 = []

    for url in set_(get_data1):
        if not url in get_data2:
            changed_1.append(1)
    for url in set_(get_data2):
        if not url in get_data1:
            changed_2.append(1)
    total_get_diff=len(changed_1)+len(changed_2)
    print "changed get", total_get_diff
    return total_get_diff

def compare_exception(exception1, exception2):
    dictionary={}
    for key in exception1:
        one = len(exception1[key])
        two = len(exception2[key])
        counting_element_type=key
        dictionary[key]= one-two
    for key,vals in dictionary.items():
            print key,"---",vals
    return dictionary


def compare_implicitly_wait(implicitly_wait1, implicitly_wait2):

    one = len(implicitly_wait1)
    two = len(implicitly_wait2)
    return one-two

def do_all(data1,data2):


    processed_data1, get1, exception1, implicitly_wait1 = get_element_dict(data1)
    processed_data2, get2, exception2, implicitly_wait2 = get_element_dict(data2)
    print_and_process(data1=processed_data1, data2=processed_data2)
    reorder_list, changed_list, deleted_list, added_list = print_and_process(processed_data1, processed_data2)
    total_reorder = Counter(reorder_list)
    total_changed = Counter(changed_list)
    reorder = print_accordance("reorder", total_reorder)
    changed = print_accordance("changed", total_changed)
    deleted = print_accordance("deleted", deleted_list)
    added   = print_accordance("added", added_list)
    compare_get(get1, get2)
    compare_exception(exception1, exception2)
    implicit_wait_diff=compare_implicitly_wait(implicitly_wait1, implicitly_wait2)
    print "implicitWait diff: ",implicit_wait_diff
    print "\n"

    print "======================================= CHANGED =============================================================="
    child_dict={}
    Element_dict={}
    for key in changed:
        key_title_list=[]
        key_title_list.append(key.title())
        for value in changed[key]:
            print "changed" ,key ,"using" ,value, ":" ,changed[key][value]
            if key.startswith("findChild"):
                child_dict[value]=changed[key][value]

    print "changed dict:", changed

    print "Changed_children_dict:",child_dict
    print "Element_dict:", Element_dict

    print "======================================= ADDED =============================================================="
    for key in added:
        for value in added[key]:
            if added[key][value]!="0":
                print "added" ,key ,"using" ,value, ":" ,added[key][value]

    print "======================================= DELETED =============================================================="
    for key in deleted:
        for value in deleted[key]:
            if deleted[key][value]!="0":
                print "deleted" ,key ,"using" ,value, ":" ,deleted[key][value]


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

def get_all_processed_contents(major_version_database, ref_sessionId_table_name, comp_sessionId_table_name):
    try:
        list_of_ref_sessionIds= connect_mysql.select_phase2_major_version_database(major_version_database, ref_sessionId_table_name)
    except IOError:
        print "ERROR : Reference table does not exist :", ref_sessionId_table_name
        print list_of_ref_sessionIds

    try:
        list_of_comp_sessionIds= connect_mysql.select_phase2_major_version_database(major_version_database,comp_sessionId_table_name)
    except IOError:
        print "ERROR : Comparable table does not exist :", comp_sessionId_table_name
    csv_filename=major_version_database[:-4]+'/' +major_version_database[:-4] + '_' + ref_sessionId_table_name[11:] + '_III_' + comp_sessionId_table_name[11:]
    try:
        if len(list_of_ref_sessionIds) == len(list_of_comp_sessionIds):
            all_contents = []
            rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
            for i in rows_in_ref_sessionId_table:
                ref_action_file_data = extract_p2_action_file_contents(list_of_ref_sessionIds[i])
                comp_action_file_data = extract_p2_action_file_contents(list_of_comp_sessionIds[i])
                print "******************************************** Test #: ",i, "******************************************** \n"
                print "SessionID ", list_of_ref_sessionIds[i], " VS ", list_of_comp_sessionIds[i], "\n"
                all_dictionary = compare_all(ref_action_file_data, comp_action_file_data)
                processed_data_csv = process_data_for_csv(all_dictionary)
                all_contents.append(processed_data_csv)
                print "\n"
                do_all(ref_action_file_data,comp_action_file_data)
                print "\n"
            return all_contents,csv_filename

    except:
        print "#################################################### TABLE ERROR: Please check if given reference table", ref_sessionId_table_name,  "and comparable table exist", comp_sessionId_table_name, "########################################################"


def compare_all(data1, data2):
    processed_data1, get1, exception1, implicitly_wait1 = get_element_dict(data1)
    processed_data2, get2, exception2, implicitly_wait2 = get_element_dict(data2)
    reorder_list, changed_list, deleted_list, added_list = print_and_process(processed_data1, processed_data2)
    total_reorder = Counter(reorder_list)
    total_changed = Counter(changed_list)
    reorder = merge_dictionary(print_accordance("reorder", total_reorder))
    changed = merge_dictionary(print_accordance("changed", total_changed))
    deleted = merge_dictionary(print_accordance("deleted", deleted_list))
    added   = merge_dictionary(print_accordance("added", added_list))
    get_diff = compare_get(get1, get2)
    exception_diff = compare_exception(exception1, exception2)
    implicit_wait_diff = compare_implicitly_wait(implicitly_wait1, implicitly_wait2)
    dictionary = {#"reorder": reorder,
                  "changed": changed,
                  "deleted": deleted,
                  "added": added,
                  # "getDiff": get_diff,
                  # "exception": exception_diff,
                  "implicitWaitdiff": implicit_wait_diff
    }
    return dictionary


def process_data_for_csv(all_dictionary):
    dictionary = {}
    for item, elementdict in all_dictionary.items():
        if item in ["reorder", "changed", "deleted", "added"]:
            for key, value in elementdict.items():
                # proces the data according to column name
                for element in value:
                    if key != "ChildElement":
                        title = element.replace(' ', '')
                        dictionary[item + "Element" + title] = value[element]
                    if key == "ChildElement":
                        title = element.replace(' ', '')
                        dictionary[item + "ChildElement" + title] = value[element]
        if item == "exception":
            for key, value in elementdict.items():
                dictionary.update({key+"Diff": value})
        if item in ["getDiff", "implicitWaitdiff"]:
            dictionary[item] = elementdict

    return dictionary


def write_in_csv(content_list, fields,csv_filename):
    print csv_filename
    try:
        with open('/Users/adityanisal/Dropbox/Phase2-CSV-outputs/'+csv_filename+'.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for dictionary in content_list:
                writer.writerow(dictionary)
    except IOError:
        print "------------ERROR in printing CSV------------"
fields = [
    "changedElementxpath",
    "changedElementpartiallinktext",
    "changedElementclassname",
    "changedElementlinktext",
    "changedElementname",
    "changedElementcssselector",
    "changedElementtagname",
    "changedElementid",
    "changedChildElementcssselector",
    "changedChildElementxpath",
    "changedChildElementtagname",
    "addedElementxpath",
    "addedElementpartiallinktext",
    "addedElementclassname",
    "addedElementlinktext",
    "addedElementname",
    "addedElementcssselector",
    "addedElementtagname",
    "addedElementid",
    "addedChildElementcssselector",
    "addedChildElementxpath",
    "addedChildElementtagname",
    "deletedElementxpath",
    "deletedElementpartiallinktext",
    "deletedElementclassname",
    "deletedElementlinktext",
    "deletedElementname",
    "deletedElementcssselector",
    "deletedElementtagname",
    "deletedElementid",
    "deletedChildElementcssselector",
    "deletedChildElementxpath",
    "deletedChildElementtagname",
    # "getDiff",
    # "sendKeysToElementDiff",
    # "clickElementDiff",
    "implicitWaitdiff",
    #"setTimeoutDiff"
    ]


p2_fireplace_database='backup_phase_two_fireplace_sids'
fireplace_mv1_reference_version_sessionId_table='sessionids_mv2_p2_2015_04_14_2'
fireplace_mv1_compare_version_sessionId_table='sessionids_mv2_p2_2015_04_28'

connect_mysql = Phase2MysqlPython('localhost', 'root', '', p2_fireplace_database)
content_list,csv_filename = get_all_processed_contents('fireplace_mv1',fireplace_mv1_reference_version_sessionId_table,fireplace_mv1_compare_version_sessionId_table)
write_in_csv(fields=fields, content_list=content_list,csv_filename=csv_filename)