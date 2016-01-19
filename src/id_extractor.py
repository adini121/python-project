import re

class IDreader(object):

    idregex = '\}\\n\sid\s\:\s(.*?)\s\\n\snextStateId'

    def apply_regex_to_reference_sessionId(self, reference_sessionId, action_file_dir):
        self.reference_sessionId = reference_sessionId
        self.action_file_dir = action_file_dir
        idregex = IDreader.idregex

        file=ActionContentReader()
        file_content=file.extract_action_file_contents(reference_sessionId, action_file_dir)
        reg_reference_id=re.findall(idregex, file_content, re.DOTALL|re.MULTILINE)
        return reg_reference_id

    def apply_regex_to_comparable_sessionId(self, comparable_sessionId, action_file_dir):
        self.comparable_sessionId = comparable_sessionId
        self.action_file_dir = action_file_dir
        idregex = IDreader.idregex

        file=ActionContentReader()
        file_content=file.extract_action_file_contents(comparable_sessionId, action_file_dir)
        reg_comparable_id=re.findall(idregex, file_content, re.DOTALL|re.MULTILINE)
        return reg_comparable_id


## Usage:
reg=IDreader()
ref_output=reg.apply_regex_to_comparable_sessionId('5fd19324-897f-4f4c-90ee-c92f0758b0a4', '/Users/adityanisal/arbit/')
comp_output=reg.apply_regex_to_comparable_sessionId('5fd19324-897f-4f4c-90ee-c92f0758b0a4', '/Users/adityanisal/arbit/')
print ref_output
print comp_output