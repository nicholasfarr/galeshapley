"""

Pseudocode for Stable Matching Algorithm

Initialize each person and hospital to be free.
while (some hospital is free and hasn’t been matched/assigned
to every applicant) {
Choose such a hospital h
a = 1st applicant on h's list to whom h has not been
matched
if (a is free)
assign h and a
else if (a prefers h to her/his current assignment h')
assign a and h, and h’ has a slot free
else
a rejects h }          
 """

def is_unstable(pairings):
    vals = set(pairings.values())
    if '-1' in vals:
        return True
    return False
    


def prefers_new(student_prefs, new_hospital, current_hospital):
    for h in student_prefs:
        if h == new_hospital:
            return True
        if h == current_hospital:
            return False
    return False


def output(pairings):
    with open('pairings.out', 'w') as file:
        for i in pairings.keys():
            file.write('{} {}\n'.format(pairings[i], i))
    file.close()


def stable_matching(filename):
    hospitals = {}
    students = {}
    pairings = {} ## flipped dict to key: student val : hospital in order to check for existing pairs. If this was a student centric version we would reverse this dictionary
    with open(filename, 'r') as file:
        n = int(file.readline().strip())

        for x in range(1,n+1):
            hospitals[x] = list(map(int, file.readline().split()))
            
        for x in range(1, n+1):
            students[x] = list(map(int, file.readline().split()))
            pairings[x] = '-1'
    file.close()


    prop_index = {h: 0 for h in hospitals}

    while is_unstable(pairings):
        ### iterate over the keys of the hospitals 
        for hospital in hospitals.keys():
            if hospital not in pairings.values():
                a = hospitals[hospital][prop_index[hospital]]
                prop_index[hospital] +=1
                if pairings[a] == '-1':
                    pairings[a] = hospital
                elif prefers_new(students[a], hospital, pairings[a]):
                    pairings[a] = hospital
                else:
                    continue
    
    output(pairings)
    return hospitals, students, pairings



