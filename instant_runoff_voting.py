from collections import defaultdict, Counter
def runoff(voters):
    """
    a function that calculates an election winner from a list of voter selections using an
    Instant Runoff Voting algorithm. https://en.wikipedia.org/wiki/Instant-runoff_voting

    Each voter selects several candidates in order of preference.
    The votes are tallied from the each voter's first choice.
    If the first-place candidate has more than half the total votes, they win.
    Otherwise, find the candidate who got the least votes and remove them from each person's voting list.
    In case of a tie for least, remove all of the tying candidates.
    In case of a complete tie between every candidate, return None
    Continue until somebody has more than half the votes; they are the winner.

The function takes a list of voter ballots; each ballot will be a list of candidates in descending order of
preference. 
Returns the symbol corresponding to the winning candidate.
    """
    final_tally = defaultdict(int)
    removed_candidates = []
    for this_round in range(len(voters[0])):
        this_round_votes = [voter[this_round] for voter in voters if voter[this_round] not in removed_candidates]
        tally = dict(Counter(this_round_votes))
        for candidate in tally:
            final_tally[candidate] +=tally[candidate]
        leader = max(final_tally, key=tally.get)
        total_votes = sum([final_tally[i] for i in final_tally])
        if final_tally[leader] >= total_votes / 2.0:
                return leader
        # no clear winner
        knockout_candidate = min(tally, key=tally.get)
        knockout_candidate_votes = tally[knockout_candidate]
        for candidate in tally:
            if tally[candidate] == knockout_candidate_votes:
                removed_candidates.append(candidate)
                del final_tally[knockout_candidate]
        

voters =  [
['c', 'a', 'b', 'd', 'e'], 
['b', 'e', 'd', 'c', 'a'], 
['b', 'e', 'c', 'a', 'd'], 
['d', 'b', 'c', 'a', 'e'], 
['c', 'b', 'd', 'a', 'e']
]

assert(runoff(voters) == "b")
