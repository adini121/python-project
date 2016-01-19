import re
from mysql_connection import MysqlPython
connect_mysql = MysqlPython('localhost', 'root', '', 'amo_sessionIDs')

def extract_action_file_contents(sessionId, action_file_dir):
    try:
        file_content=open(action_file_dir + sessionId + '/' + 'actions.txt').read()
        return file_content
    except:
        print "Following sessionID file does not exist : ", sessionId + '/' + 'actions.txt'

""" TODO: Check manually if this returns actual actions and correct # of actions """
def return_actions_dict(file_contents):
    """Return the actions in a form of a dictionary
    Example : actions1 = {0: {0: 'get', 1: 'implicitlyWait', 2: 'findElement'}, 1: {0: 'clickElement', 1: 'findElement'}, 2: {0: 'sendKeysToElement', 1: 'findElement'}"""
    main_dict = {}
    total_actions = file_contents.split(' {', 1)[1].split('\n,')
    total_number_of_actions = range(len(total_actions))
    for action_number in total_number_of_actions:
        data = total_actions[action_number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
        dictionary = {}
        data_length = len(data)
        total_number_of_sub_actions = range(data_length)
        for i in total_number_of_sub_actions:
            dictionary[i] = data[i].split(',', 1)[1].split('{', 1)[0].replace(' ', '')
        main_dict[action_number] = dictionary
    return main_dict

def get_the_action_id(file_contents):
    """Get the action ID only"""
    reg_current_id=re.findall('\}\\n\sid\s\:\s(.*?)\s\\n\snextStateId', file_contents, re.DOTALL | re.MULTILINE)
    return reg_current_id

IGNORE_ACTION = ['findElements']
def do_comparison(actions_in_reference_sessionId, actions_in_comp_sessionId, id_of_action_in_ref_sessionId_action_file, id_of_action_in_comp_sessionId_action_file):
# def do_comparison(actions1, actions2, one_id, second_id, ref_sessionID, comp_sessionID):
    """do comparison"""
    if len(actions_in_reference_sessionId) > len(actions_in_comp_sessionId):
        # print "the reference session has more # of actions. Reference SessionID ", ref_sessionID, "has # of actions:",len(actions_in_reference_sessionId)
        # print "Compare SessionID ", comp_sessionID, "has # of actions", len(actions_in_comp_sessionId)
        # print "number of actions in reference file are MORE than that of comparable file"
        number_of_actions_in_reference_sessionId = range(len(actions_in_reference_sessionId))
        reference_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        comp_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
        print  "More actions in Ref sessionId!"
    elif len(actions_in_reference_sessionId) == len(actions_in_comp_sessionId):
        # print "number of actions in both files are EQUAL"
        number_of_actions_in_reference_sessionId = range(len(actions_in_reference_sessionId))
        reference_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        comp_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
        # print "Same number of actions!"

    else:
        # print "Number of actions in reference file are LESS than that of comparable file"
        number_of_actions_in_reference_sessionId = range(len(actions_in_comp_sessionId))
        reference_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
        comp_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        print "Less actions in Ref sessionId!"
    print len(actions_in_reference_sessionId), len(actions_in_comp_sessionId)
    list = []
    for key in number_of_actions_in_reference_sessionId:
        """If you want to ignore some actions"""
        try:
            one_data = reference_sessionId_action[0][key]
            second_data = comp_sessionId_action[0][key]
            for k, v in one_data.items():
                if not v in IGNORE_ACTION:
                    # print value, second_data[key]
                    assert v == second_data[k]
                    list.append(0)
        # try:
        #     if not reference_sessionId_action[0][key] in IGNORE_ACTION:
        #         assert reference_sessionId_action[0][key] == comp_sessionId_action[0][key]
        #         list.append(0)
        except AssertionError:
            print "Mismatched"
            print "1st file id:", id_of_action_in_ref_sessionId_action_file[key]
            print "2nd file id:", id_of_action_in_comp_sessionId_action_file[key]
            print "action reference_action does not match with compare_action \n", reference_sessionId_action[0][key], "\n", comp_sessionId_action[0][key]
            list.append(1)
            break
        except KeyError:
            print "the action id %s can not be found" % reference_sessionId_action[1][key]
            list.append(1)
            break

    if 1 in list:
        print 1
    else:
        print 0

def get_all_data_of_session(sessionId, directory):
    file_contents = extract_action_file_contents(sessionId, directory)
    actions = return_actions_dict(file_contents)
    action_id = get_the_action_id(file_contents)
    return actions, action_id

def main(ref_sessionId_table_name, comp_sessionId_table, directory):
    # for row in range(len(tbl)):
    list_of_ref_sessionIds=connect_mysql.select_basic(ref_sessionId_table_name)
    print list_of_ref_sessionIds

    # for row in range(len(tbl2)):
    list_of_comp_sessionIds=connect_mysql.select_basic(comp_sessionId_table)
    print  list_of_comp_sessionIds
    if len(list_of_ref_sessionIds) == len(list_of_comp_sessionIds):
        rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
        for i in rows_in_ref_sessionId_table:
            print "_____________________________________________________________________________________________________________________________________________________________"
            ref_action_file_data = get_all_data_of_session(list_of_ref_sessionIds[i], directory)
            comp_action_file_data = get_all_data_of_session(list_of_comp_sessionIds[i], directory)
            do_comparison(actions_in_reference_sessionId=ref_action_file_data[0], actions_in_comp_sessionId=comp_action_file_data[0], id_of_action_in_ref_sessionId_action_file=ref_action_file_data[1], id_of_action_in_comp_sessionId_action_file=comp_action_file_data[1])
            # print "_____________________________________________________________________________________________________________________________________________________________"
            print "Test number:",i, "Reference_sessionID:",list_of_ref_sessionIds[i], "Comparable_sessionID:",list_of_comp_sessionIds[i]
    else:
        print "reference sessionId table", ref_sessionId_table_name, "and comparable sessionId tables", comp_sessionId_table, "have different number of rows"

tbl='sessionids_2015_01_01'
tbl2='sessionids_2015_01_14'

main(tbl, tbl2, "/Users/adityanisal/Dropbox/ActionFiles/")