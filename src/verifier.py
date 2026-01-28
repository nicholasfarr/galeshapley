
from stablematching import stable_matching, prefers_new

"""Write a separate program (or a separate mode in the same program) that:
(a)  Checks validity: each hospital and each student is matched to exactly one partner, 
with no duplicates. And 
(b) checks stability: confirms there is no blocking pair."""
def main():
   hospitals, students, pairings = stable_matching('data/example.in')
   print(verifier(hospitals, students, pairings))



def blockingPairs(hospitals, students, pairings):
    ### reverse mapping to find each hospitals current student

    h_s = {h: s for s, h in pairings.items()}

    for hospital in hospitals:
        
            a = hospitals[hospital][iterator[hospital]]
            iterator[hospital] +=1
            if prefers_new(students[a], hospital, pairings[a]):
                return "Blocking Pair: Hospital {} and Student {} prefer each other over their current assignments.".format(hospital, a)
            
    return '-1'
    

def verifier(hospitals, students, pairings):
    # verify valid matches
    if len(set(pairings.values())) != len(pairings.values()):
        return 'INVALID: More than one student assigned to the same hospital.'
    
    # verify no blocking pairs
    pair = blockingPairs(hospitals, students, pairings)
    if pair != '-1':
        return 'UNSTABLE: {}'.format(pair)

    return 'VALID STABLE'
    
    
if __name__ == '__main__':
    main()