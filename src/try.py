import re
from mysql_connection import MysqlPython
connect_mysql = MysqlPython('localhost', 'root', '', 'jenkins_core_sessionIDs')

tbl='sessionids_1_625'
tbl2='sessionids_1_627'
#
# # for row in range(len(tbl)):
sid1_result=connect_mysql.select_basic(tbl)
print sid1_result
#
# # for row in range(len(tbl2)):
sid2_result=connect_mysql.select_basic(tbl2)
print  sid2_result

# sid1_result=['b044eed6-be46-433d-b1bc-b10d6c45d105',]


# sid2_result=['b044eed6-be46-433d-b1bc-b10d6c45d105', '07875439-2134-46ad-865f-5418ac9ec2cb', '92c51250-c2d9-4e08-b516-60d1e0e57a38', '56ad6d67-2702-4321-bd14-b79777a79793', '88bee7b0-7fab-4834-ab69-f4ed66c3451a', '310dd187-a251-4e31-a795-031ea59a3571', '4a893038-41e7-4fb9-b1f0-1575d5690bc2', '0755ffcf-9dd0-4bfc-888e-7fd048ddb8c3', 'eac0dfd5-f7df-405f-9194-e6d872795781', '143aba88-f001-46c0-858e-58634299164f', '8aa4f4cc-a6c7-4dd5-9013-596c00e36c1d', 'd4b9623c-bf9c-4eb6-a0cb-4bb0bdbe6695', 'a414c9c4-4a66-4bd0-b227-67cf7cc5666b', 'bd343e7c-fc38-46e3-8223-1c5276505971', 'abf5c82f-ca1c-4ba2-ba91-b1206f4a1a46', 'cfae4dec-75a8-4e68-980c-7935035a2021', 'ce04a1b3-5a18-47fe-993c-a3a67b2a3cf0', '41c9aa93-98ad-4ac4-ae1a-165ca7657003', 'd395cd60-4b11-4d42-9ba8-c2a0bcfd8407', '60e36eb1-6b5a-459c-af04-e48a1493f17c', 'ddfa56ba-058c-44e9-b82a-9788f93a5467', 'be6aead6-fe30-45b1-8735-1582694af136', '9b53896f-2c5b-482d-ad55-fbc6b0da5a02']
# IGNORE_ACTION = ['getCookies','getPageSource', 'setWindowSize']
IGNORE_ACTION= []
def extract_action_file_contents(sessionId, action_file_dir):
    try:
        file_content=open(action_file_dir + sessionId + '/' + 'actions.txt').read()
        return file_content
    except:
        print "Following file does not exist : ", action_file_dir + sessionId + '/' + 'actions.txt'

        """ MAIN FUNCTION - return TRUE OR FALSE """

def return_actions_dict(file_contents):
    """Return the actions in a dictionary"""
    main_dict = {}
    actions = file_contents.split(' {', 1)[1].split('\n,')
    total_length = range(len(actions))
    for number in total_length:
        data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
        dictionary = {}
        length = len(data)
        total_action = range(length)
        for i in total_action:
            dictionary[i] = data[i].split(',', 1)[1].split('{', 1)[0].replace(' ', '')
        main_dict[number] = dictionary
    return main_dict

def get_the_action_id(file_content):
    """Get the action ID only"""
    list = []
    actions = file_content.split(' {', 1)[1].split('\n,')
    total_length = range(len(actions))
    for number in total_length:
    	data = actions[number].split('}\n id :')[1].split('\n nextStateId :')[0].replace(' ', '')
    	list.append(data)
    return list

def do_comparison(actions1, actions2, one_id, second_id):
    """do comparison"""
    if len(actions1) > len(actions2):
        print "the first file is bigger"
        reference_actions = range(len(actions1))
        print reference_actions
        bigger_action = (actions1, one_id)
        lower_action = (actions2, second_id)

    elif len(actions1) == len(actions2):
        print "both file is equal"
        reference_actions = range(len(actions1))
        bigger_action = (actions1, one_id)
        lower_action = (actions2, second_id)

    else:
        print "the second file is bigger"
        reference_actions = range(len(actions2))
        bigger_action = (actions2, second_id)
        lower_action = (actions1, one_id)
    print len(actions1), len(one_id)

    for key in reference_actions:
        try:
            one_data = bigger_action[0][key]
            second_data = lower_action[0][key]
            for k, v in one_data.items():
                if not v in IGNORE_ACTION:
                    try:
                        assert v == second_data[k]

                    except AssertionError:
                        print "Mismatched"
                        print "1st file id:", one_id[key]
                        print "2nd file id:", second_id[key]
                        print "1 action:", v
                        print "2 action:", second_data[k]
                        print 1
                        return None
                    except KeyError:
                        print "This action item is not present", v
                        print 1
                        return None

        except KeyError:
            print "the action id %s can not be found" % bigger_action[1][key]
            print 1
            return None

    print 0

def get_all_data_of_session(session, directory):
    file_contents = extract_action_file_contents(session, directory)
    actions = return_actions_dict(file_contents)
    action_id = get_the_action_id(file_contents)
    return actions, action_id

def do_all(ref_session, comp_session, directory):
    if len(ref_session) == len(comp_session):
        total_number = range(len(ref_session))
        for i in total_number:
            file1_data = get_all_data_of_session(ref_session[i], directory)
            file2_data = get_all_data_of_session(comp_session[i], directory)
            do_comparison(actions1=file1_data[0], actions2=file2_data[0], one_id=file1_data[1], second_id=file2_data[1])
        print "success"
    else:
        print "Both has different number of session id"

do_all(sid1_result, sid2_result,"/Users/adityanisal/Dropbox/ActionFiles/")