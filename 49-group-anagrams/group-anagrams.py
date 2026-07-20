class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        
        for word in strs:
            # Sort the letters to create a standard key (e.g., "eat" -> "aet")
            key = "".join(sorted(word))
            
            # If the key isn't in our dictionary, add it with a new list
            if key not in groups:
                groups[key] = []
                
            # Add the original word to its sorted letter group
            groups[key].append(word)
            
        # Return all the grouped lists
        return list(groups.values())
