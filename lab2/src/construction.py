from lexer import Regular
from lexer import Lexer

# This file contains the parser

from graphviz import Digraph


#A epsilon edge
EPSILON = -1
# Edges correspond to character sets
CCL = -2
#The corresponding node has two outgoing epsilon sides
EMPTY = -3
ASCII_COUNT = 127
groupCount = 0

# NFA node
class Nfa(object):
    # Node number
    STATUS_NUM = 0

    def __init__(self):
        self.groupID=groupCount
        self.edge = EPSILON
        self.next_1 = None
        self.next_2 = None
        self.visited = False
        self.input_set = set()
        self.set_status_num()
        # self.value = None

    def set_status_num(self):
        self.status_num = Nfa.STATUS_NUM
        Nfa.STATUS_NUM = Nfa.STATUS_NUM + 1

    def set_input_set(self):
        self.input_set = set()
        for i in range(ASCII_COUNT):
            self.input_set.add(chr(i))


class NfaPair(object):
    def __init__(self):
        self.start_node = None
        self.end_node = None


def get_visualize( start_node):
    dot = Digraph(comment='The Test Table')
    res = []
    res.append("digraph G {")
    res.append(" rankdir=LR;")
    def visualize(start_node,res):
        next_1 = start_node.next_1 is not None
        next_2 = start_node.next_2 is not None

        if next_1:
            res.append(" {} -> {} [label=\"{}\"];".format(start_node.status_num,start_node.next_1.status_num,start_node.edge))
        if next_2:
            res.append(" {} -> {} [label=\"{}\"];".format(start_node.status_num,start_node.next_2.status_num, start_node.edge))
        start_node.visited = True
        if start_node.next_1 is not None and not start_node.next_1.visited:
            visualize(start_node.next_1,res)
        if start_node.next_2 is not None and not start_node.next_2.visited:
            visualize(start_node.next_2,res)
        return "\n".join(res)

    return visualize(start_node,res)+"\n}"


lexer = None


def pattern(pattern_string):
    global lexer
    lexer = Lexer(pattern_string)
    lexer.advance()
    nfa_pair = NfaPair()
    group(nfa_pair)

    return nfa_pair.start_node


# use Bottom-up method
# # Matches. a (single character) []
def term(pair_out):
    if lexer.match(Regular.L):
        nfa_single_char(pair_out)
    elif lexer.match(Regular.ANY):
        nfa_dot_char(pair_out)


# Match a single character
def nfa_single_char(pair_out):
    if not lexer.match(Regular.L):
        return False

    start = pair_out.start_node = Nfa()
    pair_out.end_node = pair_out.start_node.next_1 = Nfa()
    start.edge = lexer.lexeme
    lexer.advance()
    return True


# . Matches any single character
def nfa_dot_char(pair_out):
    if not lexer.match(Regular.ANY):
        return False

    start = pair_out.start_node = Nfa()
    pair_out.end_node = pair_out.start_node.next_1 = Nfa()
    start.edge = CCL
    start.set_input_set()

    lexer.advance()
    return False


# factor connect
def factor_conn(pair_out):
    if is_conn(lexer.current_token):
        factor(pair_out)

    while is_conn(lexer.current_token):
        pair = NfaPair()
        factor(pair)
        pair_out.end_node.next_1 = pair.start_node
        pair_out.end_node = pair.end_node

    return True


def is_conn(token):
    nc = [
        Regular.OPEN_PAREN,
        Regular.CLOSE_PAREN,
        Regular.AT_EOL,
        Regular.EOS,
        Regular.CLOSURE,
        Regular.PLUS_CLOSE,
        Regular.CCL_END,
        Regular.AT_BOL,
        Regular.OR,
    ]
    return token not in nc

# ?
def nfa_option_closure(pair_out):
    if not lexer.match(Regular.OPTIONAL):
        return False
    start = Nfa()
    end = Nfa()

    start.next_1 = pair_out.start_node
    start.next_2 = end
    pair_out.end_node.next_1 = end

    pair_out.start_node = start
    pair_out.end_node = end

    lexer.advance()
    return True

# factor * + ? closure
def factor(pair_out):
    term(pair_out)
    if lexer.match(Regular.CLOSURE):
        nfa_star_closure(pair_out)
    elif lexer.match(Regular.PLUS_CLOSE):
        nfa_plus_closure(pair_out)
    elif lexer.match(Regular.OPTIONAL):
        nfa_option_closure(pair_out)


# * closure operations
def nfa_star_closure(pair_out):
    if not lexer.match(Regular.CLOSURE):
        return False
    start = Nfa()
    end = Nfa()
    start.next_1 = pair_out.start_node
    start.next_2 = end

    pair_out.end_node.next_1 = pair_out.start_node
    pair_out.end_node.next_2 = end

    pair_out.start_node = start
    pair_out.end_node = end

    lexer.advance()
    return True


# + is closure
def nfa_plus_closure(pair_out):
    if not lexer.match(Regular.PLUS_CLOSE):
        return False
    start = Nfa()
    end = Nfa()
    start.next_1 = pair_out.start_node

    pair_out.end_node.next_1 = pair_out.start_node
    pair_out.end_node.next_2 = end

    pair_out.start_node = start
    pair_out.end_node = end

    lexer.advance()
    return True

def expr(pair_out):
    factor_conn(pair_out)
    pair = NfaPair()

    while lexer.match(Regular.OR):
        lexer.advance()
        factor_conn(pair)
        start = Nfa()
        start.next_1 = pair.start_node
        start.next_2 = pair_out.start_node
        pair_out.start_node = start

        end = Nfa()
        pair.end_node.next_1 = end
        pair_out.end_node.next_2 = end
        pair_out.end_node = end

    return True


# factor connect
def factor_conn(pair_out):
    if is_conn(lexer.current_token):
        factor(pair_out)

    while is_conn(lexer.current_token):
        pair = NfaPair()
        factor(pair)
        pair_out.end_node.next_1 = pair.start_node
        pair_out.end_node = pair.end_node

    return True


def is_conn(token):
    nc = [
        Regular.OPEN_PAREN,
        Regular.CLOSE_PAREN,
        Regular.AT_EOL,
        Regular.EOS,
        Regular.CLOSURE,
        Regular.PLUS_CLOSE,
        Regular.CCL_END,
        Regular.AT_BOL,
        Regular.OR,
    ]
    return token not in nc


def group(pair_out):
    global groupCount
    if lexer.match(Regular.OPEN_PAREN):
        groupCount = groupCount+1
        lexer.advance()
        expr(pair_out)
        if lexer.match(Regular.CLOSE_PAREN):
            lexer.advance()
    elif lexer.match(Regular.EOS):
        return False
    else:
        expr(pair_out)

    while True:
        pair = NfaPair()

        if lexer.match(Regular.OPEN_PAREN):
            groupCount = groupCount + 1
            lexer.advance()
            expr(pair)
            pair_out.end_node.next_1 = pair.start_node
            pair_out.end_node = pair.end_node
            if lexer.match(Regular.CLOSE_PAREN):
                lexer.advance()
        elif lexer.match(Regular.EOS):
            return False
        elif lexer.match(Regular.AT_BOL):
            lexer.advance()
            group(pair_out)
        elif lexer.match(Regular.AT_EOL):
            return False
        else:
            expr(pair)
            pair_out.end_node.next_1 = pair.start_node
            pair_out.end_node = pair.end_node


def match(input_string, nfa_machine):
    ls = []
    start_node = nfa_machine

    current_nfa_set = [start_node]
    next_nfa_set = closure(current_nfa_set)

    for i, ch in enumerate(input_string):
        current_nfa_set = move(next_nfa_set, ch)
        next_nfa_set = closure(current_nfa_set)
        if next_nfa_set is None:
            return ls
        else:
            ls.append(ch)

        # if len(ls)>0 and next_nfa_set is None:
        #     return ls



        if has_accepted_state(next_nfa_set) and i == len(input_string) - 1:
            return ls

    return None

def match2(input_string, nfa_machine,groupID):
    ls = []
    start_node = nfa_machine
    current_nfa_set = [start_node]
    next_nfa_set = closure(current_nfa_set)

    for i, ch in enumerate(input_string):
        current_nfa_set = move(next_nfa_set, ch)
        next_nfa_set = closure(current_nfa_set)

        if next_nfa_set is None:
            return None
        elif groupID==0:
            ls.append(ch)
        elif ( len(current_nfa_set)!=0 and current_nfa_set[0].groupID==groupID):
            ls.append(ch)

        if has_accepted_state(next_nfa_set) and i == len(input_string) - 1:
            return ls

    return None


def closure(input_set):
    if len(input_set) <= 0:
        return None

    nfa_stack = []
    for i in input_set:
        nfa_stack.append(i)

    while len(nfa_stack) > 0:
        nfa = nfa_stack.pop()
        next1 = nfa.next_1
        next2 = nfa.next_2
        if next1 is not None and nfa.edge == EPSILON:
            if next1 not in input_set:
                input_set.append(next1)
                nfa_stack.append(next1)

        if next2 is not None and nfa.edge == EPSILON:
            if next2 not in input_set:
                input_set.append(next2)
                nfa_stack.append(next2)

    return input_set


def move(input_set, ch):
    out_set = []
    for nfa in input_set:
        if nfa.edge == ch or (nfa.edge == CCL and ch in nfa.input_set):
            out_set.append(nfa.next_1)

    return out_set

# Match success
def has_accepted_state(nfa_set):
    for nfa in nfa_set:
        if nfa.next_1 is None and nfa.next_2 is None:
            return True

