
        for i in range(k,len(nums)):
            window_sum = window_sum + nums[i]
            window_sum = window_sum - nums[i-k]

            max_sum = max(max_sum,window_sum)

        return max_sum/k
