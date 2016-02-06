import re
import subprocess
import humanfriendly
from humanfriendly.tables import format_pretty_table
from humanfriendly.tables import format_robust_table

""" Filename: MyParser.py
    What it does: For each pair of reference and comparable sessionId, parse and compare action files to output image differences and comparison result
"""
def extract_action_file_contents(sessionId, action_file_dir):
    """ This function extracts the contents of action file , takes as input the sessionId and action files directory"""
    try:
        file_content=open(action_file_dir + sessionId + '/' + 'actions.txt').read()
        return file_content
    except:
        print "======================================================== Following sessionID file does not exist : ", sessionId + '/' + 'actions.txt', "======================================================="

""" TODO: Check manually if this returns actual actions and correct # of actions """
def return_actions_dict(file_contents):
    """This function returns the actions in the form of a dictionary, takes as input the contents of action file """
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
    """This function gets the action ID of all actions including current action using regular expression"""
    reg_current_id=re.findall('\}\\n\sid\s\:\s(.*?)\s\\n\snextStateId', file_contents, re.DOTALL | re.MULTILINE)
    return reg_current_id

IGNORE_ACTION = []
def do_comparison(app_name, ref_sessionId_table_name, comp_sessionId_table_name,test_number,ref_sessionId, comp_sessionId,actions_in_reference_sessionId, actions_in_comp_sessionId, id_of_action_in_ref_sessionId_action_file, id_of_action_in_comp_sessionId_action_file):
    """ This function performs the comparison of two action files to generate visual and state-based differences
        Takes as input application name, reference and comparable sessionId table names as app=-versions, reference and comparable sessoinId, actions in reference and comparable sessionId, ID of action in reference and comparable action files
    """

    if len(actions_in_reference_sessionId) > len(actions_in_comp_sessionId):
        number_of_actions_in_reference_sessionId = range(len(actions_in_reference_sessionId))
        reference_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        comp_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
    elif len(actions_in_reference_sessionId) == len(actions_in_comp_sessionId):
        number_of_actions_in_reference_sessionId = range(len(actions_in_reference_sessionId))
        reference_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)
        comp_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
    else:
        number_of_actions_in_reference_sessionId = range(len(actions_in_comp_sessionId))
        reference_sessionId_action = (actions_in_comp_sessionId, id_of_action_in_comp_sessionId_action_file)
        comp_sessionId_action = (actions_in_reference_sessionId, id_of_action_in_ref_sessionId_action_file)

    num_of_ref_actions = '%d' % (len(actions_in_reference_sessionId))
    num_of_comp_actions = '%d' % (len(actions_in_comp_sessionId))

    list = []
    for key in number_of_actions_in_reference_sessionId:

        """ Code to generate ImageDiff. Makes use of Imagemagick's convert (http://www.imagemagick.org/script/convert.php) """
        num = '%d' % (test_number)
        imgDir='/Users/adityanisal/ImageFiles/'
        outDir='/Users/adityanisal/Desktop/ImageComparisonResults/' + app_name + '/'
        outFileName= app_name  + '_'+ ref_sessionId_table_name[11:] + '_' + comp_sessionId_table_name[11:] + '_Test_' + num  + '.png'
        outFile=outDir + outFileName
        ref_screenshot= imgDir + ref_sessionId + '/screenshots/'+ id_of_action_in_ref_sessionId_action_file[-1] + '.png'
        comp_screenshot= imgDir + comp_sessionId + '/screenshots/'+ id_of_action_in_comp_sessionId_action_file[-1] + '.png'
        try:
            p=subprocess.Popen(["/usr/local/bin/convert", "+append", ref_screenshot ,comp_screenshot, outFile],stdout=subprocess.PIPE)
            return_code =p.wait()
            if return_code > 0:
                raise Exception('CONVERT ERROR!!')
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

        """ Code to generate action file differences """
        ref_action_Id = id_of_action_in_ref_sessionId_action_file[key]
        comp_action_Id = id_of_action_in_comp_sessionId_action_file[key]
        ref_action = []
        comp_action = []
        try:
            if not reference_sessionId_action[0][key] in IGNORE_ACTION:
                assert reference_sessionId_action[0][key] == comp_sessionId_action[0][key]
                list.append(0)
        except AssertionError:
            ref_action = reference_sessionId_action[0][key]
            comp_action = comp_sessionId_action[0][key]
            list.append(1)
            break
        except KeyError:
            list.append(1)
            break

    if 1 in list:
        result= '1'
    else:
        result= '0'

    actions_difference = ''
    if ref_action and comp_action:
          actions_difference = '\nAction differences for test number ' + '%d' % (test_number) + ': \n' #, ref_action, comp_action
          actions_difference = actions_difference + '%s' % str(ref_action) + '\n'
          actions_difference = actions_difference + '%s' % str(comp_action)

    humanfriendly_results=[test_number, result, num_of_ref_actions, num_of_comp_actions, ref_sessionId[:18], comp_sessionId[:18], ref_action_Id[:18], comp_action_Id[:18]]
    return humanfriendly_results, actions_difference

def get_all_data_of_session(sessionId, directory):
    """
    :param sessionId: sessionId of a test
    :param directory:
    :return:
    """
    file_contents = extract_action_file_contents(sessionId, directory)
    actions = return_actions_dict(file_contents)
    action_id = get_the_action_id(file_contents)
    return actions, action_id

def main(major_version_database, ref_sessionId_table_name, comp_sessionId_table_name, action_files_dir, app_name):
    """SQL Query app version : eg. jenkins_mv1, moodle """
    try:
        list_of_ref_sessionIds= connect_mysql.select_major_version_database(major_version_database, ref_sessionId_table_name)
    except IOError:
        print "ERROR : Reference table does not exist :", ref_sessionId_table_name
        print list_of_ref_sessionIds

    try:
        list_of_comp_sessionIds= connect_mysql.select_major_version_database(major_version_database,comp_sessionId_table_name)
    except IOError:
        print "ERROR : Comparable table does not exist :", comp_sessionId_table_name

    column_names = ['Test #','Test Result','#ref_actions', '#comp_actions', 'ref sessionId', 'comp sessionId', 'ref action Id', 'comp action Id']
    final_list=[]
    action_differences_dictionary= []
    try:
        if len(list_of_ref_sessionIds) == len(list_of_comp_sessionIds):
            rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
            for i in rows_in_ref_sessionId_table:
                ref_action_file_data = get_all_data_of_session(list_of_ref_sessionIds[i], action_files_dir)
                comp_action_file_data = get_all_data_of_session(list_of_comp_sessionIds[i], action_files_dir)
                # do_comparison(app_name, ref_sessionId_table_name, comp_sessionId_table_name,i,list_of_ref_sessionIds[i],list_of_comp_sessionIds[i],actions_in_reference_sessionId=ref_action_file_data[0], actions_in_comp_sessionId=comp_action_file_data[0], id_of_action_in_ref_sessionId_action_file=ref_action_file_data[1], id_of_action_in_comp_sessionId_action_file=comp_action_file_data[1])
                humanfriendly_results, action_differences_string=do_comparison(app_name, ref_sessionId_table_name, comp_sessionId_table_name, i, list_of_ref_sessionIds[i], list_of_comp_sessionIds[i], actions_in_reference_sessionId=ref_action_file_data[0], actions_in_comp_sessionId=comp_action_file_data[0], id_of_action_in_ref_sessionId_action_file=ref_action_file_data[1], id_of_action_in_comp_sessionId_action_file=comp_action_file_data[1])
                final_list.append(humanfriendly_results)
                if action_differences_string != '':
                    action_differences_dictionary.append(action_differences_string)
            """ This command prints results in a table by making use of humanfriendly tabels (https://humanfriendly.readthedocs.org/en/latest/#module-humanfriendly.tables) """
            with open('/Users/adityanisal/Dropbox/ExtractedResultFiles/' + app_name + '/'+ app_name + '_' + ref_sessionId_table_name[11:] + '_' + comp_sessionId_table_name[11:] + '_Results.txt', 'w+') as resultfile:
                print >> resultfile, (format_pretty_table(final_list, column_names))
                for action_differences_string in action_differences_dictionary:
                    print >> resultfile, action_differences_string
                    print action_differences_string
                print ".............................................................. SUCCESS ..................................................................."
        else:
            print "----------------------------------------------- CAUTION! reference sessionId table: ", ref_sessionId_table_name, "and comparable sessionId table:", comp_sessionId_table_name, "Both have different number of rows --------------------------------"
    except:
        print "#################################################### TABLE ERROR: Please check if given reference table", ref_sessionId_table_name,  "and comparable table exist", comp_sessionId_table_name, "########################################################"



""" Getting sessionIds from mysql tables """
from mysql_connection import MysqlPython
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
jenkins_core_MV1_compare_version_sessionId_table_list=['sessionids_1_580_1','sessionids_1_580_2','sessionids_1_580_3','sessionids_1_582','sessionids_1_584','sessionids_1_586','sessionids_1_588','sessionids_1_590','sessionids_1_592','sessionids_1_594','sessionids_1_596']

# Jenkins core MV2
jenkins_core_MV2_reference_version_sessionId_table = 'sessionids_1_596_new'
jenkins_core_MV2_compare_version_sessionId_table_list = ['sessionids_1_596_1','sessionids_1_596_2','sessionids_1_596_3','sessionids_1_598','sessionids_1_600','sessionids_1_602','sessionids_1_604','sessionids_1_606','sessionids_1_596_on_1_609']

# Jenkins core MV3
jenkins_core_MV3_reference_version_sessionId_table = 'sessionids_1_609'
jenkins_core_MV3_compare_version_sessionId_table_list = ['sessionids_1_609_1','sessionids_1_609_2','sessionids_1_609_3','sessionids_1_611','sessionids_1_613','sessionids_1_615','sessionids_1_617','sessionids_1_619','sessionids_1_621','sessionids_1_623','sessionids_1_609_on_1_625']

# Jenkins core MV4
jenkins_core_MV4_reference_version_sessionId_table = 'sessionids_1_625'
jenkins_core_MV4_compare_version_sessionId_table_list = ['sessionids_1_625_1','sessionids_1_625_2','sessionids_1_625_3','sessionids_1_627','sessionids_1_629','sessionids_1_631','sessionids_1_633','sessionids_1_635','sessionids_1_637','sessionids_1_639','sessionids_1_641']


############################################## Moodle ##############################################
# Moodle MV1
moodle_reference_version_sessionId_table= 'sessionids_230_beta_fin'
moodle_compare_version_sessionId_table_list=['sessionids_230_retest','sessionids_231_fin','sessionids_232_fin','sessionids_233_fin','sessionids_234_retest','sessionids_236_fin','sessionids_237_fin','sessionids_238_fin','sessionids_239_fin','sessionids_2310_fin','sessionids_2311_fin']

# Moodle Reordered
moodle_reordered_reference_version_sessionId_table='sessionids_230_beta_reordered'
moodle_reordered_comparable_version_sessionId_table_list=['sessionids_230_rc1_reordered','sessionids_230_reordered','sessionids_231_reordered','sessionids_232_reordered','sessionids_233_reordered','sessionids_234_reordered','sessionids_235_reordered','sessionids_236_reordered','sessionids_237_reordered','sessionids_238_reordered','sessionids_239_reordered','sessionids_2310_reordered','sessionids_2311_reordered']
############################################## Fireplace (Mozilla Marketplace) ##############################################
# Fireplace MV1
fireplace_mv1_reference_version_sessionId_table='sessionids_mv1_2014_12_16'
fireplace_mv1_compare_version_sessionId_table_list=['sessionids_mv1_2014_12_22_02','sessionids_mv1_2015_01_06', 'sessionids_mv1_2015_01_20','sessionids_mv1_2015_01_27','sessionids_mv1_2015_02_10']

# Fireplace MV2
fireplace_mv2_reference_version_sessionId_table='sessionids_MV2_2015_02_10'
fireplace_mv2_compare_version_sessionId_table_list=['sessionids_MV2_2015_02_24','sessionids_MV2_2015_03_10','sessionids_MV2_2015_04_01','sessionids_MV2_2015_04_10','sessionids_MV2_2015_04_21','sessionids_MV2_2015_04_28']

# Fireplace MV3
fireplace_mv3_reference_version_sessionId_table='sessionids_MV3_2015_07_07'
fireplace_mv3_compare_version_sessionId_table_list=['sessionids_MV3_2015_07_21','sessionids_MV3_2015_07_31','sessionids_MV3_2015_08_11','sessionids_MV3_2015_08_25','sessionids_MV3_2015_09_08','sessionids_MV3_2015_09_22','sessionids_MV3_2015_09_29','sessionids_MV3_2015_10_13','sessionids_MV3_2015_11_02']

# Fireplace MV4
fireplace_mv4_reference_version_sessionId_table='sessionids_MV4_2015_11_02'
fireplace_mv4_compare_version_sessionId_table_list=['sessionids_MV4_2015_11_17','sessionids_MV4_2015_11_24','sessionids_MV4_2015_12_01','sessionids_MV4_2015_12_22','sessionids_MV4_2016_01_12']

############################################## AMO ##############################################
# AMO MV1
amo_mv1_reference_version_sessionId_table='sessionids_2015_01_01'
amo_mv1_compare_version_sessionId_table_list=['sessionids_2015_01_14','sessionids_2015_02_11','sessionids_2015_03_05','sessionids_2015_03_18','sessionids_2015_03_26','sessionids_2015_04_16','sessionids_2015_04_25_mv0']

#AMO MV2
amo_mv2_reference_version_sessionId_table='sessionids_2015_04_25'
amo_mv2_compare_version_sessionId_table_list=['sessionids_2015_05_06','sessionids_2015_05_21','sessionids_2015_05_29','sessionids_2015_06_09','sessionids_2015_06_15','sessionids_2015_07_13','sessionids_2015_07_28','sessionids_mv1_on_2015_07_31']

#AMO MV3
amo_mv3_reference_version_sessionId_table='sessionids_2015_07_31'
amo_mv3_compare_version_sessionId_table_list=['sessionids_2015_08_11','sessionids_2015_08_27','sessionids_2015_09_10','sessionids_2015_10_08','sessionids_2015_10_22']

############################################## Bedrock (Mozilla.org) ##############################################
#Bedrock MV1
bedrock_mv1_reference_version_sessionId_table='sessionids_mv1_2015_01_13'
bedrock_mv1_compare_version_sessionId_table_list=['sessionids_mv1_2015_01_30','sessionids_mv1_2015_02_13','sessionids_mv1_2015_02_26','sessionids_mv1_2015_03_12','sessionids_mv1_2015_03_30','sessionids_mv1_2015_04_10','sessionids_mv1_2015_04_20']

#Bedrock MV2
bedrock_mv2_reference_version_sessionId_table=''
bedrock_mv2_compare_version_sessionId_table_list=''
""" Call to main function """
""" Change app name to reflect proper DB name """
""" Change reference and comparable table names """
""" Input parameters to be given in sequence:
    1. SQL query version (eg. jenkins_mv1, moodle, amo_mv0)
    5. app name
"""

""" !!! Input parameters: Select DATABASE name !!! """
connect_mysql = MysqlPython('localhost', 'root', '', moodle_reordered_database)
action_files_dir = "/Users/adityanisal/Dropbox/ActionFiles/"

""" !!! Input parameters: Select reference table and comparable table name, APP Name !!! """
for table in moodle_reordered_comparable_version_sessionId_table_list:
    main('moodle_reordered', moodle_reordered_reference_version_sessionId_table, table, action_files_dir, 'moodle_reordered')
