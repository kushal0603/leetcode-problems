from collections import defaultdict
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Build a mapping from attack level to defense levels.
        # - Time: O(n)
        # - Space: O(n)
        attackLevel2defenseLevels = defaultdict(list)
        for attackLevel, defenseLevel in properties:
            attackLevel2defenseLevels[attackLevel].append(defenseLevel)

        # Special case of a single attack level
        if len(attackLevel2defenseLevels) == 1:
            return 0

        # Sort the attack levels in descending order
        # - Time: O(a*log(a))
        # - Space: O(a)
        descendingAttackLevels = sorted(attackLevel2defenseLevels, reverse=True)
        descendingAttackLevelIter = iter(descendingAttackLevels)

        # Go through the attack levels in descending order, keeping track of the highest defense level seen so far
        # - Time: O(n)
        # - Space: O(1)
        maxAttackLevel = next(descendingAttackLevelIter)
        maxDefenseLevelSoFar = max(attackLevel2defenseLevels[maxAttackLevel])

        numWeakCharacters = 0
        for attackLevel in descendingAttackLevelIter:
            maxDefenseLevelForStrongerAttackLevels = maxDefenseLevelSoFar
            for defenseLevel in attackLevel2defenseLevels[attackLevel]:
                if defenseLevel < maxDefenseLevelForStrongerAttackLevels:
                    numWeakCharacters += 1
                elif defenseLevel > maxDefenseLevelSoFar:
                    maxDefenseLevelSoFar = defenseLevel

        return numWeakCharacters