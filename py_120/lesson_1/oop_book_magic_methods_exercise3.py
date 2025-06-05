class Candidate:
    def __init__(self, name):
        self._name = name
        self._votes = 0

    def __iadd__(self, one_vote):
        if not isinstance(one_vote, int):
            return NotImplemented
        
        self._votes += one_vote
        # Note that this method mutates the candidate object. The return value isn't used, but we return self anyway as this matches the behaviour of the inbuilt iadd method.
        return self

class Election:
    total_votes = 0

    def __init__(self, candidates):
        self._candidates = candidates # references a set containing the candidate objects

    def calculate_winner(self):
        self.candidate_percentages = {
            candidate: (candidate._votes / Election.total_votes) * 100
            for candidate in self._candidates
            }

        winning_candidate = max(self.candidate_percentages, key=self.candidate_percentages.get)

        winning_candidate_score = self.candidate_percentages[winning_candidate]
        
        return (winning_candidate._name, winning_candidate_score)

    def results(self):
        for candidate in self._candidates:
            print(f'{candidate._name}: {candidate._votes} votes')
            Election.total_votes += candidate._votes

        winner = Election.calculate_winner(self)
        name = winner[0]
        percentage = winner[1]

        print(f'{name} won: {percentage} of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes
