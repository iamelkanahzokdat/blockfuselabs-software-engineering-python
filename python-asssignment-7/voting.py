"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.


candidates = {}
voters = set()

def register_candidates(*args, **kwargs):
    Register candidates with optional metadata.
    
    pass

def cast_vote(voter_id, candidate):
    Cast vote if voter has not voted before.
        after all the vote logic is completeted sucessfully,
        return: Vote casted for {candidate}.
    
    pass

def election_result():
    Return the winner(s).
    # max_votes = #add logic
    # winners = #add logic
    # return {"winners": winners, "candidates": candidates}
    """
'''
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.
'''

candidates = {}
voters = set()

# register multiple candidates using *args
def register_candidates(*args):
    for candidate in args:
        if candidate not in candidates:
            candidates[candidate] = {"votes": 0, "details": {}}

# update candidate details using **kwargs
def update_candidate(name, **kwargs):
    if name in candidates:
        candidates[name]["details"].update(kwargs)
    else:
        return f"Candidate {name} not found."

