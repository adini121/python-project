from mysql_connection import MysqlPython
#
# connect_mysql = MysqlPython('localhost', 'root', '', 'jenkins_core_sessionIDs')
#
# jenkins_mv1_ref_table = ['sessionids_1_580','sessionids_1_584']
# """
# def jenkins_ref_sessionids(connection):
#     for tbl in jenkins_mv1_ref_table:
#         print "we are in table: ", tbl
#         for row in range(len(tbl)):
#             sid=connection.select_basic(tbl)
#         print sid
# """
#
# tbl='sessionids_1_584'
# tbl2='sessionids_1_586'
#
# # for row in range(len(tbl)):
# sid1=connect_mysql.select_basic(tbl)
# print sid1
#
# # for row in range(len(tbl2)):
# sid2=connect_mysql.select_basic(tbl2)
# print  sid2
#
# """ Dictionary logic
# def extract_action_file_contents(sessionId, action_file_dir):
#     try:
#         for session_id in sessionId:
#             file_content=open(action_file_dir + sessionId + '/' + 'actions.txt').read()
#         return file_content
#     except:
#         print "Following file does not exist : ", action_file_dir + sessionId + '/' + 'actions.txt'
#
# def return_actions_dict(file_contents):
#     main_dict = {}
#     actions = file_contents.split(' {', 1)[1].split('\n,')
#     total_length = range(len(actions))
#     for number in total_length:
#         data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
#         dictionary = {}
#         length = len(data)
#         total_action = range(length)
#         for i in total_action:
#             dictionary[i] = data[i].split(',', 1)[1].split('{', 1)[0].replace(' ', '')
#         main_dict[number] = dictionary
#     # print "actions",actions
#     # print "total_length",total_length
#     # print "total_action",total_action
#     return main_dict
#
# action_file_dir2="/Users/adityanisal/Dropbox/ActionFiles/"
# for i in sid1:
#     # for j in sid2:
#         reference_file_contents=extract_action_file_contents(i, action_file_dir2)
#         # print reference_file_contents
#         # comp_file_contents=extract_action_file_contents(j, action_file_dir2)
#         # dic1=return_actions_dict(reference_file_contents)
#         # dic2=return_actions_dict(comp_file_contents)
# """
# # print dic1
# # # print "\n"
# # print dic2
#
# #
# # for tbl in sessionids_1_584:
# #     for row in range(len(tbl)):
# #         sid=connect_mysql.select_basic(tbl)
# #
# #
# #
# #     # return sid
# #
# # print(jenkins_ref_sessionids(connect_mysql))
# #
# # jenkins_mv1_comp_table = ['sessionids_1_584', 'sessionids_1_586']
#
#
#
# # reference_file_contents=extract_action_file_contents('d1f0d2d5-5755-442d-b838-d0d2ff08afa8', action_file_dir)
# # comparable_action_file=extract_action_file_contents('42a33d42-9676-466c-9b9f-e632d772ef8f', action_file_dir)
# # jenkins_action_file=extract_action_file_contents('11683295-e3a7-4be5-87f2-9a1e480986e2', action_file_dir2)
# # amo_action_file=extract_action_file_contents('2177fcab-b01c-4a98-9494-407ed89ee030', action_file_dir2)
# # # print reference_file_contents
# # # print "\n"
# # # print comparable_action_file
# #
# # def return_actions_dict(file_contents):
# #     main_dict = {}
# #     actions = file_contents.split(' {', 1)[1].split('\n,')
# #     total_length = range(len(actions))
# #     for number in total_length:
# #         data = actions[number].split('}\n id :')[0].replace('\n actions : {', '').replace('[', '', 1).split('],\n', -1)
# #         dictionary = {}
# #         length = len(data)
# #         total_action = range(length)
# #         for i in total_action:
# #             dictionary[i] = data[i].split(',', 1)[1].split('{', 1)[0].replace(' ', '')
# #         main_dict[number] = dictionary
# #     print "actions",actions
# #     print "total_length",total_length
# #     # print "total_action",total_action
# #     return main_dict
# #
# #     # print main_dict
# # dic2=return_actions_dict(jenkins_action_file)
# # dic1=return_actions_dict(amo_action_file)
# #
# # print dic1
# # # print "\n"
# # print dic2
import re
import csv

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

# extract_action_file_contents("0ffb1801-a998-4c30-b54f-29c97cdec7ba")


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
    try:
        rows_in_ref_sessionId_table = range(len(list_of_ref_sessionIds))
        rows_in_comp_sessionId_table = range(len(list_of_comp_sessionIds))
        for i in rows_in_comp_sessionId_table:
            ref_action_file_data = extract_p2_action_file_contents(list_of_ref_sessionIds[i])
            comp_action_file_data = extract_p2_action_file_contents(list_of_comp_sessionIds[i])
            print "******************************************** Test #: ",i, "******************************************** \n"
            print "SessionID ", list_of_ref_sessionIds[i], " VS ", list_of_comp_sessionIds[i], "\n"
            print ref_action_file_data
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            print comp_action_file_data


    except:
        print "#################################################### TABLE ERROR: Please check if given reference table", ref_sessionId_table_name,  "and comparable table exist", comp_sessionId_table_name, "########################################################"


p2_jenkins_database='backup_phase_two_jenkins_sids'
jenkins_mv1_reference_version_sessionId_table='sessionids_phase2_1_635'
jenkins_mv1_compare_version_sessionId_table='sessionids_phase2_1_625'
connect_mysql = Phase2MysqlPython('localhost', 'root', '', p2_jenkins_database)

get_all_processed_contents('jenkins_mv1',jenkins_mv1_reference_version_sessionId_table,jenkins_mv1_compare_version_sessionId_table)