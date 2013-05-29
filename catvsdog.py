#!/usr/bin/env python
'''
Usage:
$python catvsdog.py <testfile.txt
'''
import sys
from itertools import combinations, chain

def satisfied_voters(lines):
    '''
    Prints the maximum number of satisfied voters
    '''
    lines_list = lines.split('\n')
    testcases = int(lines_list[0])
    current_line = 1
    for testcase in xrange(testcases):
        result = []
        n_cats, n_dogs, n_voters = parse_lines(lines_list[current_line])
        votes = lines_list[current_line + 1:current_line + n_voters + 1]
        contestants = construct_contestants(n_cats, n_dogs)
        possibilities = powerset(contestants)
        for p in possibilities:
            score = get_score(votes, p)
            result.append(score)
        print max(result)
        current_line += n_voters + 1

def powerset(s):
    '''
    Returns a list of each subset of the powerset of possible outcomes
    '''
    power_set = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    return [p for p in power_set]

def construct_contestants(n_cats, n_dogs):
    '''
    Returns a list of contestants ['C1', 'D1']
    '''
    contestants = []
    for n in range(n_cats):
        contestants.append('C' + str(n+1))
    for n in range(n_dogs):
        contestants.append('D' + str(n+1))
    return contestants

def get_score(votes, p):
    '''
    Returns the number of satisfied users according to the possibility of keeps and throw aways
    '''
    score = 0
    for vote in votes:
        keep_vote, throw_vote = vote.split()
        if keep_vote in p and throw_vote not in p:
            score += 1
    return score

def parse_lines(stats):
    '''
    Returns the number of cats, dogs and voters
    '''
    numbers = stats.split()
    n_cats = int(numbers[0])
    n_dogs = int(numbers[1])
    n_voters = int(numbers[2])
    return n_cats, n_dogs, n_voters

if __name__ == '__main__':
    lines = sys.stdin.read()
    lines.rstrip()
    satisfied_voters(lines)

