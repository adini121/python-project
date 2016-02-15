import re
from collections import Counter
from phase2_mysql_connection import Phase2MysqlPython


def extract_p2_action_file_contents(sessionId):
    """ This function extracts the contents of action file , takes as input the sessionId and action files directory"""
    p2_action_file_dir='/Users/adityanisal/Dropbox/PhaseTwoActionFiles/'
    try:
        file_content=open(p2_action_file_dir + sessionId + '.' + 'actions.txt').read()
        # print file_content
        return file_content

    except:
        print "======================================================== Following sessionID file does not exist : ", sessionId + '/' + 'actions.txt', "======================================================="

# data1=extract_p2_action_file_contents('a2da1608-5e22-4a2c-b3ce-72b8b7e10141')
# data2=extract_p2_action_file_contents('e76fe865-c7d6-45f2-aba9-5132b94915ae')

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
      # 'executeScript': [],
      # 'getPageSource': [],
      'setTimeout': [],
      # 'getElementText': [],
      # 'getTitle': []
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
    # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    return dictionary, get, exception, implicitly_wait
#
# processed_data1, get1, exception1, implicitly_wait1 = get_element_dict(data1)
# processed_data2, get2, exception2, implicitly_wait2 = get_element_dict(data2)


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
    # print list1
    return reorder_list, changed_list, deleted_list, added_list
# print_and_process(data1=processed_data1, data2=processed_data2)
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
        #dict = {}
        #for key in data:
        #    if key[0] not in dict:
        #        dict[key[0]] = {key[1][1]: key[1][0]}
        #    else:
        #        dict[key[0]].update({key[1][1]: key[1][0]})
        #if dict != {}:
        #    print type, dict
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
        # print "Changed", counting_element_type,counting_difference
        # for key, val in dictionary:
        #     print
    for key,vals in dictionary.items():
            print key,"---",vals
    # print dictionary
    return dictionary
        # print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        # print "Changed", key, one-two
        # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        # To print added and deleted separately
        # if one != two:
        #     if one > two:
        #         print "deleted", key, one-two
        #     if two > one:
        #         print "added", key, two-one

def compare_implicitly_wait(implicitly_wait1, implicitly_wait2):

    one = len(implicitly_wait1)
    two = len(implicitly_wait2)
    # print "Changed implicitlyWait", one-two
    return one-two
    # To print added and deleted separately
    # if one > two:
    #     print "implicitlyWait", "deleted", one-two
    # else:
    #     print "implicitlyWait", "deleted", 0
    # if two > one:
    #     print "implicitlyWait", "created", two-one
    # else:
    #     print "implicitlyWait", "created", 0

# reorder_list, changed_list, deleted_list, added_list = print_and_process(data1=processed_data1, data2=processed_data2)
# total_reorder = Counter(reorder_list)
# total_changed = Counter(changed_list)
""" from before, already commented"""
    #total_added = [x[1] for x in added_list]
    #total_deleted = [x[1] for x in deleted_list]
# deleted_count = get_deleted_or_added(total_deleted)
# added_count = get_deleted_or_added(total_added)
""" till here """
# reorder = print_accordance("reorder", total_reorder)
# changed = print_accordance("changed", total_changed)
# deleted = print_accordance("deleted", deleted_list)
# added   = print_accordance("added", added_list)
# compare_get(get1, get2)
# compare_exception(exception1, exception2)
# compare_implicitly_wait(implicitly_wait1, implicitly_wait2)

""" for printing """
# #for key, value in reorder.items():
#  #   print "reorder", key, value
# """ PRINT FINAL OUTPUTS """
# print "\n"
# print "======================================== REORDERED ================================================================="
# for key in reorder:
#     for value in reorder[key]:
#         if changed[key][value]!="0": #checks if not equal to zero
#             print "reordered" ,key ,"using" ,value, ":" ,reorder[key][value]
#
# print "======================================= CHANGED =============================================================="
#
# for key in changed:
#     for value in changed[key]:
#         if changed[key][value]!="0":
#             print "changed" ,key ,"using" ,value, ":" ,changed[key][value]
#
# print "======================================= ADDED =============================================================="
# for key in added:
#     for value in added[key]:
#         if added[key][value]!="0":
#             print "added" ,key ,"using" ,value, ":" ,added[key][value]
#
# print "======================================= DELETED =============================================================="
# for key in deleted:
#     for value in deleted[key]:
#         if deleted[key][value]!="0":
#             print "deleted" ,key ,"using" ,value, ":" ,deleted[key][value]

# print "======================================= lenghts =============================================================="

def do_all(data1,data2):


    processed_data1, get1, exception1, implicitly_wait1 = get_element_dict(data1)
    processed_data2, get2, exception2, implicitly_wait2 = get_element_dict(data2)
    print_and_process(data1=processed_data1, data2=processed_data2)
    reorder_list, changed_list, deleted_list, added_list = print_and_process(processed_data1, processed_data2)
    # reorder_list, changed_list, deleted_list, added_list = print_and_process(data1=processed_data1, data2=processed_data2)
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
    # print "======================================== REORDERED ================================================================="
    # for key in reorder:
    #     for value in reorder[key]:
    #         if changed[key][value]!="0": #checks if not equal to zero
    #             print "reordered" ,key ,"using" ,value, ":" ,reorder[key][value]

    print "======================================= CHANGED =============================================================="
    child_dict={}
    findElement_dict={}
    findElements_dict={}
    for key in changed:
        # print key.title()
        key_title_list=[]
        key_title_list.append(key.title())
        # print key_title_list
        for value in changed[key]:
            # print "changed" ,key ,"using" ,value, ":" ,changed[key][value]
            # print "777777777777777777"
            if key.startswith("findChild"):
                child_dict[value]=changed[key][value]
            # if key.title'findElement':
            #     findElement_dict[value]=changed[key][value]

                # print "changedChildren:", key, "with", value, ": :",changed[key][value]
            if changed[key][value]!="0":
                print "changed" ,key ,"using" ,value, ":" ,changed[key][value]
    # print "\n"
    print "Changed_children_dict:",child_dict
    # print "findElement_dict:", findElement_dict
    # for key, val in child_dict.items():
    #     val_list=[]
    #     print key, "->", val
        # val_list.append(val)
        # for val_items in val_list:
        #     final_count=val_list
        # print "val_list:", sum(val_list)
    #     print "changed children elements total:"
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

    # print "======================================= lenghts =============================================================="

def main_function(major_version_database, ref_sessionId_table_name, comp_sessionId_table_name):
    try:
        list_of_ref_sessionIds= connect_mysql.select_phase2_major_version_database(major_version_database, ref_sessionId_table_name)
    except IOError:
        print "ERROR : Reference table does not exist :", ref_sessionId_table_name
        print list_of_ref_sessionIds

    try:
        list_of_comp_sessionIds= connect_mysql.select_phase2_major_version_database(major_version_database,comp_sessionId_table_name)
    except IOError:
        print "ERROR : Comparable table does not exist :", comp_sessionId_table_name

    try:
        if len(list_of_ref_sessionIds) == len(list_of_comp_sessionIds):
            rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
            for i in rows_in_ref_sessionId_table:
                ref_action_file_data = extract_p2_action_file_contents(list_of_ref_sessionIds[i])
                comp_action_file_data = extract_p2_action_file_contents(list_of_comp_sessionIds[i])
                print "******************************************** Test #: ",i, "******************************************** \n"
                print "SessionID ", list_of_ref_sessionIds[i], " VS ", list_of_comp_sessionIds[i], "\n"
                do_all(ref_action_file_data,comp_action_file_data)
                print "\n"
                print "\n"

    except:
        print "#################################################### TABLE ERROR: Please check if given reference table", ref_sessionId_table_name,  "and comparable table exist", comp_sessionId_table_name, "########################################################"



p2_fireplace_database='backup_phase_two_fireplace_sids'
fireplace_mv1_reference_version_sessionId_table='sessionids_mv2_p2_2015_02_10'
fireplace_mv1_compare_version_sessionId_table='sessionids_mv2_p2_2015_07_31'

connect_mysql = Phase2MysqlPython('localhost', 'root', '', p2_fireplace_database)
main_function('fireplace_mv1',fireplace_mv1_reference_version_sessionId_table,fireplace_mv1_compare_version_sessionId_table)

"""
IGNORE-THIS-USE-LATER-IF-NEEDED
def process_data(data):
    dictionary = {}
    for obj, value in data.items():
        if obj[0] not in dictionary:
            dictionary[obj[0]] = {obj[1]: value}
        else:
            dictionary[obj[0]].update({obj[0]: value})
    return dictionary
"""