from collections import Counter

def extract_action_file_contents(sessionId):
    """ This function extracts the contents of action file , takes as input the sessionId and action files directory"""
    action_file_dir = '/Users/adityanisal/Dropbox/PhaseTwoActionFiles/'
    try:
        file_content=open(action_file_dir + sessionId + '.' + 'actions.txt').read()
        # print file_content
        return file_content

    except:
        print "======================================================== Following sessionID file does not exist : ", sessionId + '/' + 'actions.txt', "======================================================="

data1 = extract_action_file_contents('a2da1608-5e22-4a2c-b3ce-72b8b7e10141')
data2 = extract_action_file_contents('e76fe865-c7d6-45f2-aba9-5132b94915ae')


