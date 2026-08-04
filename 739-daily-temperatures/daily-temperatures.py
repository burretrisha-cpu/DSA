class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack = []
        answer = [0] * n
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temperatures[j] > temperatures[i]:
        #             answer[i]=j-1
        #             break
        # return answer
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                index=stack.pop()
                answer[index]=i-index
            stack.append(i)
        return answer
        



        