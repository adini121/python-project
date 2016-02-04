import re
import sys
import tarfile
import os

class Dummie():
    ref_sid="7663f5fd-5c22-4668-934a-1dbf696eedd3"


    ####For reference version, from first SID till last SID match actions -> Important to identify AND get test number!!!!!!!!
    # def reader(filename):
    reference_action_file= open("/Users/adityanisal/arbit/" + ref_sid + "/" + "actions.txt")
    ref_action_file_content=reference_action_file.read()
    # comparison_action_file= open("/Users/adityanisal/arbit/42a33d42-9676-466c-9b9f-e632d772ef8f/actions.txt")
    # cmp_action_file_content=comparison_action_file.read()

    #### Counting number of actions and matching
    ref_count=ref_action_file_content.count("actions")
    # cmp_count=cmp_action_file_content.count("actions")
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


    """For matching inner content - this works"""
    # reg_actions_details=re.findall('\['+'42a33d42-9676-466c-9b9f-e632d772ef8f'+'\,\s(.*?)\s\{',ref_action_file_content, re.DOTALL|re.MULTILINE)
    reg_actions_details=re.findall('\['+ref_sid+'\,\s(.*?)\s\{',ref_action_file_content, re.DOTALL|re.MULTILINE)
    print "detailed actions=", reg_actions_details

    """Inner content and everything """
    find_element= re.findall('\['+ref_sid+'\,\sfindElement\s\{(.*?)\}\]',ref_action_file_content, re.DOTALL|re.MULTILINE)
    # find_element_CSS= re.findall('\['+ref_sid+'\,\sfindElement\s\{using\=(.*?)\,value\=(.*?)\}\]',ref_action_file_content, re.DOTALL|re.MULTILINE)
    print "find_element=", find_element
    ##### THIS WORKS #######
    reg_current_id=re.findall('\}\\n\sid\s\:\s(.*?)\s\\n\snextStateId',ref_action_file_content, re.DOTALL|re.MULTILINE)
    print "current ids =", reg_current_id

    ##### THIS WORKS #######
    reg_nextState_id=re.findall('\s\\n\snextStateId\s\:\sSome\((.*?)\)\}',ref_action_file_content, re.DOTALL|re.MULTILINE)
    # print "nextState ids=", reg_nextState_id

    """ Finding by action type """
    """ 1. sendKeysToElement
        2. get
        3. findElement
        4. setTimeout
        5. clickElement
        6. implicitlyWait
        7. findChildElements
        8. getElementText
        9.
        ...Add more
    """
    """ Find Element """
    find_element= re.findall('\['+ref_sid+'\,\sfindElement\s\{(.*?)\}\]',ref_action_file_content, re.DOTALL|re.MULTILINE)

    """ Get """

    """ Click """

    """ SendKeys """

    """ Wait """
    """ findElement type :
        1. css selector
        2. xpath
        3. linked text
        4. partial linked text
        5. name
        6. id
        7. class name
        ...Add more

    """

    """ Wait type:
        1. Implicitly wait
        2. Explicitly wait
        3. Sleep
        4. WaitforPagetoLoad
        5. FluentWait
        6. setTimeout
        ...Add more
    """
    # for line in ref_action_file_content:
    #     matches += reg.findall(line)
    # ref_action_file_content.close()


