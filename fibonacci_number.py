"""https://leetcode.com/problems/fibonacci-number/description/ """

class Solution:
    def fib(self, n: int) -> int:
        if n==0:return 0
        elif n==1:return 1
        else:return self.fib(n-1) + self.fib(n-2)


if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(3))
