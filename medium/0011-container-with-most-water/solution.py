             width = right - left

             water_height = min(height[left],height[right])

             area = width * water_height

             max_water = max(max_water,area)

             if height[left] < height[right]:
                 left += 1
             else:
                 right -= 1
        
