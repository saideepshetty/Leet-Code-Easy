'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Code By Saideep Shetty
'''
class Solution(object):
    def getRow(self, numRows):
        if numRows == 0:
            return [1]
        output = [[1]]
        for i in range(1, numRows+1):
            temp = list(output[-1])
            temp.insert(0, '0')
            temp.append('0')
            op = []
            for j in range(len(temp)-1):
                num = int(temp[j]) + int(temp[j+1])
                op.append(num)
            output.append(op)
        return op
