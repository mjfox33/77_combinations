class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = list()
        current = [0]*k
        i=0
        while i>=0:
            current[i] += 1
            if current[i] > n-k+i+1:
                i -= 1
            elif i == k - 1:
                result.append(list(current))
            else:
                i += 1
                current[i] = current[i-1]
        return result