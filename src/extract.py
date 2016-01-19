import re
import sys
import tarfile
import os

class extract():
    def untar(fname):
        target_folder="."
        for file in os.listdir("/Users/adityanisal/arbit/"):
            with tarfile.open(fname) as tf:
                tf.extract(target_folder)

    ref_sid="42a33d42-9676-466c-9b9f-e632d772ef8f"


    ####For reference version, from first SID till last SID match actions -> Important to identify AND get test number!!!!!!!!
    # def reader(filename):
    ref_action_file= open("/Users/adityanisal/arbit/42a33d42-9676-466c-9b9f-e632d772ef8f/42a33d42-9676-466c-9b9f-e632d772ef8f.txt")
    ref_action_file_content=ref_action_file.read()
    cmp_action_file= open("/Users/adityanisal/arbit/42a33d42-9676-466c-9b9f-e632d772ef8f/actions.txt")
    cmp_action_file_content=cmp_action_file.read()

    #### Counting number of actions and matching
    ref_count=ref_action_file_content.count("actions")
    cmp_count=cmp_action_file_content.count("actions")
    # print "ref content:", ref_action_file_content.count("actions")
    # print "cmp content:", cmp_action_file_content.count("actions")

    # if (ref_count == cmp_count):
    #     print("Same content")
    # elif (ref_count > cmp_count):
    #     print "some condition"
    # else:
    #     print "some condition"




    # ref_regex


    matches = []
    # reg = re.compile('actions\s\:\s\{(.*?)\}\]\,',re.MULTILINE|re.DOTALL)
    # for line in ref_action_file:
    #     result = reg.search(line)
    #     print(result)
    # reg = re.compile('actions\s\:\s\{(.*?)\}\]\,', ref_action_file_content, re.DOTALL|re.MULTILINE)

    ##### THIS WORKS #######
    # reg1=re.findall('Session\s(.*?)\s\{', ref_action_file_content, re.DOTALL|re.MULTILINE)
    # print(reg1)

    # reg = re.findall('Session(.*?)None', ref_action_file_content, re.DOTALL|re.MULTILINE)
    # print(reg)

    ##### THIS WORKS #######
    # reg_actions=re.findall('actions\s\:\s\\{\s\\n(.*?)\\n\}\\n\sid',ref_action_file_content, re.DOTALL|re.MULTILINE)
    # print "actions =",reg_actions[1]



    # reg_actions_details=re.findall('\['+re.escape(ref_sid)+'\,\s(.*?)\s\{',reg_actions, re.DOTALL|re.MULTILINE)
    # reg_actions_details=re.findall('\['+ref_sid+'\,\s(.*?)\s\{',reg_actions, re.DOTALL|re.MULTILINE)
    # print "detailed actions=", reg_actions_details



    ##### THIS WORKS #######
    reg_current_id=re.findall('\}\\n\sid\s\:\s(.*?)\s\\n\snextStateId',ref_action_file_content, re.DOTALL|re.MULTILINE)
    # print "current ids =", reg_current_id

    ##### THIS WORKS #######
    reg_nextState_id=re.findall('\s\\n\snextStateId\s\:\sSome\((.*?)\)\}',ref_action_file_content, re.DOTALL|re.MULTILINE)
    # print "nextState ids=", reg_nextState_id



    # for line in ref_action_file_content:
    #     matches += reg.findall(line)
    # ref_action_file_content.close()


