from collections import Counter


class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        parties_counter = Counter(senate)

        senate = list(senate)

        while senate:
            party = senate[0]

            if party == "R":

                if parties_counter["D"] > 0:

                    senate.remove("D")
                    
                    senate.append(senate.pop(0))
                    
                    parties_counter['D'] -= 1

                else:

                    return "Radiant"

            elif party == "D":

                if parties_counter["R"] > 0:

                    senate.remove("R")

                    senate.append(senate.pop(0))

                    parties_counter['R'] -= 1

                else:

                    return "Dire"


sol = Solution()

print(sol.predictPartyVictory("RD"))
