import re
import subprocess

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

IGNORE_ACTION = []
def do_comparison(app_name, ref_sessionId_table_name, comp_sessionId_table_name,test_number,ref_sessionId, comp_sessionId,actions_in_reference_sessionId, actions_in_comp_sessionId, id_of_action_in_ref_sessionId_action_file, id_of_action_in_comp_sessionId_action_file):
    """ do comparison """
    """ For printing:
    # print "the reference session has more # of actions. Reference SessionID ", ref_sessionID, "has # of actions:",len(actions_in_reference_sessionId)
    # print "Compare SessionID ", comp_sessionID, "has # of actions", len(actions_in_comp_sessionId)
    # print "number of actions in reference file are MORE than that of comparable file"
    """
    if len(actions_in_reference_sessionId) > len(actions_in_comp_sessionId):

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
        """ Printing ImageDiff """
        num = '%d' % (test_number)
        imgDir='/Users/adityanisal/ImageFiles/'
        outDir='/Users/adityanisal/Desktop/ImageComparisonResults/' + app_name + '/'
        outFileName= app_name  + ref_sessionId_table_name[-6:] + '_' + comp_sessionId_table_name[-5:] + '_Test_' + num  + '.png'
        outFile=outDir + outFileName
        ref_screenshot= imgDir + ref_sessionId + '/screenshots/'+ id_of_action_in_ref_sessionId_action_file[-1] + '.png'
        comp_screenshot= imgDir + comp_sessionId + '/screenshots/'+ id_of_action_in_comp_sessionId_action_file[-1] + '.png'
        print "########################################################################################################################################"
        print 'imgDir:', imgDir
        print 'outDir:',outDir
        print 'outFile:',outFile
        print 'ref_screenshot:',ref_screenshot
        print 'comp_screenshot:',comp_screenshot
        print 'final string:', '/usr/local/bin/convert'+'+append'+ ref_screenshot +comp_screenshot+ outFile
        print "########################################################################################################################################"
        try:
            p=subprocess.Popen(["/usr/local/bin/convert", "+append", ref_screenshot ,comp_screenshot, outFile],stdout=subprocess.PIPE)
            return_code =p.wait()
            if return_code > 0:
                raise Exception('CONVERT ERROR!!')
            # subprocess.call('/usr/local/bin/convert +append ' + imgDir + ref_sessionId + '/screenshots/'+ id_of_action_in_ref_sessionId_action_file[-1] + '.png' + ' ' + imgDir + comp_sessionId + '/screenshots/'+ id_of_action_in_comp_sessionId_action_file[-1] + '.png' + outDir + outFile, shell=False)
        except OSError:
            print "Stop !!! There was an error in printing out the file! "

        """If you want to ignore some actions"""
        # Specify : IGNORE_ACTION = ['findElements']
        # try:
        #     one_data = reference_sessionId_action[0][key]
        #     second_data = comp_sessionId_action[0][key]
        #     for k, v in one_data.items():
        #         if not v in IGNORE_ACTION:
        #             # print value, second_data[key]
        #             assert v == second_data[k]
        #             list.append(0)
        """ Original logic without ignoring actions"""
        try:
            if not reference_sessionId_action[0][key] in IGNORE_ACTION:
                assert reference_sessionId_action[0][key] == comp_sessionId_action[0][key]
                list.append(0)
        except AssertionError:
            print "Mismatched"
            print "1st file id:", id_of_action_in_ref_sessionId_action_file[key]
            print "2nd file id:", id_of_action_in_comp_sessionId_action_file[key]
            list.append(1)
            break
        except KeyError:
            print "the action id %s can not be found" % reference_sessionId_action[1][key]
            list.append(1)
            break

    if 1 in list:
        print "FAILED -------------------------->>>",1
    else:
        print "PASSED -------------------------->>>",0

def get_all_data_of_session(sessionId, directory):
    file_contents = extract_action_file_contents(sessionId, directory)
    actions = return_actions_dict(file_contents)
    action_id = get_the_action_id(file_contents)
    return actions, action_id

def main(ref_sessionId_table_name, comp_sessionId_table_name, action_files_dir, app_name):
    # for row in range(len(tbl)):
    try:
        list_of_ref_sessionIds=connect_mysql.select_jenkins_1_580(ref_sessionId_table_name)
        print list_of_ref_sessionIds
    except:
        print "ERROR : Reference table does not exist :", ref_sessionId_table_name

    # for row in range(len(tbl2)):
    try:
        list_of_comp_sessionIds=connect_mysql.select_jenkins_1_580(comp_sessionId_table_name)
        print  list_of_comp_sessionIds
    except:
        print "ERROR : Comparable table does not exist :", comp_sessionId_table_name
    try:
        if len(list_of_ref_sessionIds) == len(list_of_comp_sessionIds):
            rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
            for i in rows_in_ref_sessionId_table:
                print "_____________________________________________________________________________________________________________________________________________________________"
                ref_action_file_data = get_all_data_of_session(list_of_ref_sessionIds[i], action_files_dir)
                comp_action_file_data = get_all_data_of_session(list_of_comp_sessionIds[i], action_files_dir)
                do_comparison(app_name, ref_sessionId_table_name, comp_sessionId_table_name,i,list_of_ref_sessionIds[i],list_of_comp_sessionIds[i],actions_in_reference_sessionId=ref_action_file_data[0], actions_in_comp_sessionId=comp_action_file_data[0], id_of_action_in_ref_sessionId_action_file=ref_action_file_data[1], id_of_action_in_comp_sessionId_action_file=comp_action_file_data[1])
                print "REF SID", list_of_ref_sessionIds[i]
                # print "_____________________________________________________________________________________________________________________________________________________________"
                print "Test number:",i, "Reference_sessionID:",list_of_ref_sessionIds[i], "Comparable_sessionID:",list_of_comp_sessionIds[i]
        else:
            print "reference sessionId table", ref_sessionId_table_name, "and comparable sessionId tables", comp_sessionId_table_name, "have different number of rows"
    except:
        print "TABLE ERROR: Please check if given reference table", ref_sessionId_table_name,  "and comparable table % exist", comp_sessionId_table_name


""" Getting sessionIds from mysql tables """
from mysql_connection import MysqlPython
db_name = 'jenkins_core_sessionIDs'
connect_mysql = MysqlPython('localhost', 'root', '', db_name )
reference_version_sessionId_table= 'sessionids_1_580'
compare_version_sessionId_table_list=['sessionids_1_592', 'sessionids_1_594', 'sessionids_1_580_on_1_596']

""" Call to main function """
action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"
for table in compare_version_sessionId_table_list:
    print "=============================================================================================================================================="
    print "Version",reference_version_sessionId_table, "against",table
    main(reference_version_sessionId_table, table, action_files_dir, 'jenkins_core' )
    print "=============================================================================================================================================="
