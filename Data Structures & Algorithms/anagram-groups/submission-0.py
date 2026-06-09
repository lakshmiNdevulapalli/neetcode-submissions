class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for word in strs:
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            sorted_key = tuple(char_count)
            if sorted_key not in hash_map:
                hash_map[sorted_key] = []
            hash_map[sorted_key].append(word)
        return list(hash_map.values())