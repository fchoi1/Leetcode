class Solution:
    def rankTeams(self, votes: List[str]) -> str:
    
        team_scores = defaultdict(lambda: [0] * len(votes[0]))
        for v in votes:
            for i,team in enumerate(v):
                team_scores[team][i] += 1

        sorted_teams = sorted(team_scores.keys(), key=lambda team: (team_scores[team], -ord(team)), reverse=True)
        return "".join(sorted_teams)

        