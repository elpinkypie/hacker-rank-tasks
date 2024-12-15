"""https://leetcode.com/problems/fizz-buzz/"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.fizzBuzz(n=3))


# Here is another solution: 

def fizzBuzz(n: int):
    for i in range(1, n + 1):
        result = ("Fizz" * (i % 3 == 0)) + ("Buzz" * (i % 5 == 0))
        print(result or i)
