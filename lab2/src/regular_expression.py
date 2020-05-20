

import construction
from src.construction import get_visualize



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

    def group(self):
        pass



st = 'aaaaabcccccasdzxc'
pattern = '(\*?|a+)(zx|bc*)(asd|fgh)(zxc)'

for i in range(len(st)):
    regex = Regex(st[i:], pattern)
    result = regex.match()
    if result:
        print("".join(result))
        print(regex.graph)
        break