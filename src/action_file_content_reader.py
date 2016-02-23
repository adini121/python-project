# from mysql_connection import MysqlPython
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

str='fireplace_mv1'
print str[:-4]