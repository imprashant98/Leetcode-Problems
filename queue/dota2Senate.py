class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_count = 0
        dire_count = 0
        ban_r = 0
        ban_d = 0

        for party in senate:
            if party == 'R':
                radiant_count += 1
            else:
                dire_count += 1

        while radiant_count > 0 and dire_count > 0:
            new_senate = []
            for party in senate:
                if party == 'R':
                    if ban_r > 0:
                        ban_r -= 1
                        radiant_count -= 1
                    else:
                        new_senate.append(party)
                        ban_d += 1
                elif ban_d > 0:
                    ban_d -= 1
                    dire_count -= 1
                else:
                    new_senate.append(party)
                    ban_r += 1
            senate = new_senate

        return "Radiant" if radiant_count > 0 else "Dire"
