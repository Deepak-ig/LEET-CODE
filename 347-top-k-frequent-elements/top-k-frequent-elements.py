class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count how many times each number appears
        counts = {}
        for x in nums:
            if x in counts:
                counts[x] = counts[x] + 1
            else:
                counts[x] = 1
                
        # Step 2: Separate the counts into a list so we can sort them
        # We store them as [count, number]
        frequency_list = []
        for number, count in counts.items():
            frequency_list.append([count, number])
            
        # Step 3: Sort the list from biggest count to smallest count
        frequency_list.sort(reverse=True)
        
        # Step 4: Grab just the numbers from the top 'k' items
        result = []
        for i in range(k):
            item = frequency_list[i]
            result.append(item[1]) # item[1] is the actual number
            
        return result
