import re
from mysql_connection import MysqlPython
connect_mysql = MysqlPython('localhost', 'root', '', 'amo_sessionIDs')

# tbl='sessionids_1_625'
# tbl2='sessionids_1_590'
#
# # for row in range(len(tbl)):
# sid1_result=connect_mysql.select_basic(tbl)
# print sid1_result
#
# # for row in range(len(tbl2)):
# sid2_result=connect_mysql.select_basic(tbl2)
# print  sid2_result

# sid1_result=['b044eed6-be46-433d-b1bc-b10d6c45d105',]


# sid2_result=['b044eed6-be46-433d-b1bc-b10d6c45d105', '07875439-2134-46ad-865f-5418ac9ec2cb', '92c51250-c2d9-4e08-b516-60d1e0e57a38', '56ad6d67-2702-4321-bd14-b79777a79793', '88bee7b0-7fab-4834-ab69-f4ed66c3451a', '310dd187-a251-4e31-a795-031ea59a3571', '4a893038-41e7-4fb9-b1f0-1575d5690bc2', '0755ffcf-9dd0-4bfc-888e-7fd048ddb8c3', 'eac0dfd5-f7df-405f-9194-e6d872795781', '143aba88-f001-46c0-858e-58634299164f', '8aa4f4cc-a6c7-4dd5-9013-596c00e36c1d', 'd4b9623c-bf9c-4eb6-a0cb-4bb0bdbe6695', 'a414c9c4-4a66-4bd0-b227-67cf7cc5666b', 'bd343e7c-fc38-46e3-8223-1c5276505971', 'abf5c82f-ca1c-4ba2-ba91-b1206f4a1a46', 'cfae4dec-75a8-4e68-980c-7935035a2021', 'ce04a1b3-5a18-47fe-993c-a3a67b2a3cf0', '41c9aa93-98ad-4ac4-ae1a-165ca7657003', 'd395cd60-4b11-4d42-9ba8-c2a0bcfd8407', '60e36eb1-6b5a-459c-af04-e48a1493f17c', 'ddfa56ba-058c-44e9-b82a-9788f93a5467', 'be6aead6-fe30-45b1-8735-1582694af136', '9b53896f-2c5b-482d-ad55-fbc6b0da5a02']

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