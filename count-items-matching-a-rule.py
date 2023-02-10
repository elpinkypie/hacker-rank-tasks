"""https://leetcode.com/problems/count-items-matching-a-rule/
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
"""

from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        counter = 0
        for item in items:
            if ruleKey == "type" and ruleValue == item[0]:
                counter = counter + 1
            if ruleKey == "color" and ruleValue == item[1]:
                counter = counter + 1
            if ruleKey == "name" and ruleValue == item[2]:
                counter = counter + 1

        return counter

if __name__ == "__main__":
    solution = Solution()
    print(solution.countMatches(
        items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
    ))
