'''
42. Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''

#제일 높은 곳 5
'''
exm1
[0,1,0,2,1,0,1,3,2,1,2,1]
 0+0+1+0+1+2+1+0+1+2+0+0 : 예상
 0+0+1+0+1+2+1+0+0+1+0+0 : 답
 전체 3인 것은 중요하지 않음. 좌, 우가 중요함 
  
exm2
0+2+4+1+2 :9
어떻게 생각했는지? 4에서 2 일때는 2 부을수 있음. 근데 , 옆이 0임 
'''



#제출 답안
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) -1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right],right_max)
            
            if left_max<=right_max:
                volume += left_max - height [left]
                left +=1
            else:
                volume+= right_max - height[right]
                right -=1
        return volume
