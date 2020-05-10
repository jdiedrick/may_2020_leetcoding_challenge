class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        
        #set up dictionary to map person to who they trust
        people_trust = {}
        
        for person in range(1, N + 1):
            people_trust[person] = []
                
        for t in trust:
            person = t[0]
            who_they_trust = t[1]
            
            people_trust[person].append(who_they_trust)
                
        # set up dictionary to map person to how many people trust them
        trusted_people = {}
        for people, trust in people_trust.items():
            for t in trust:
                if t in trusted_people:
                    trusted_people[t] += 1
                else:
                    trusted_people[t] = 1
                    
        judge = -1
        
        # go through trusted people and find potential judge (a person who is trusted by everyone except one person: the judge)
        for person, trust in trusted_people.items():
            if trust == N - 1:
                judge = person
        
        # check that the judge doesn't trust anyone
        if judge in people_trust and people_trust[judge] != []:
            return -1
        else:
            return judge
