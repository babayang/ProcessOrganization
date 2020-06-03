

import construction
from construction import get_visualize



class Regex(object):
    def __init__(self, input_string, pattern_string):
        self.input_string = input_string
        self.pattern_string = pattern_string
        self.graph = None


    def match(self):
        pattern_string = self.pattern_string
        input_string = self.input_string
        nfa_machine = construction.pattern(pattern_string)
        self.graph =  get_visualize(nfa_machine)
        return construction.match(input_string, nfa_machine)

    def matchAll(self):
        ins = self.input_string
        for i in range(len(self.input_string)):
            result = self.match()
            if result:
                break
            self.input_string = self.input_string[1:]
        if len(result)==0:
            return "You should enter the correct expression"
        return "".join(result)

    def group(self, groupID):
        pattern_string = self.pattern_string
        input_string = self.input_string
        nfa_machine = construction.pattern(pattern_string)
        self.graph = get_visualize(nfa_machine)
        resultgroup = construction.match2(input_string, nfa_machine, groupID)
        return "".join(resultgroup)

# st = 'hwhwhwhwhaaaaabcccccasdzxc'
# pattern = '(\*?|a+)(zx|bc*)(asd|fgh)(zxc)'
# # #
# regex = Regex(st, pattern)
# result = regex.matchAll()
# print(result)
# st = 'aaaaabcccccasdzxc'
# pattern = '(\*?|a+)(zx|bc*)(asd|fgh)(zxc)'
#
# regex = Regex(st, pattern)
# #result = regex.match()
# resultgroup=regex.group(2)
# print(resultgroup)