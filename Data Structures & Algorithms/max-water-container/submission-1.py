class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        start = 0
        end = len(heights) - 1
        while not start >= end:
            # breadth = end - start
            # length = abs(heights[end] - heights[start])
            area = (end - start) * min(heights[start], heights[end])
            if area > maximum:
                maximum = area
                #move the pointer that has smaller heights value
                if heights[end] >= heights[start]:
                    start = start + 1
                else:
                    end = end - 1
            else:
                if heights[end] >= heights[start]:
                    start = start + 1
                else:
                    end = end - 1
        return maximum


        