
def lengthOfLongestSubstring(s) -> int:
        if len(s) < 2:
            return len(s)
        if len(set(s)) == len(s):
            return len(s)
        substring = set()
        longest_substring = 0
        for i in range(0, len(s)-1):
            for j in range(i, len(s)):
                if s[j] not in substring:
                    substring.add(s[j])
                else:
                    break
            longest_substring = max(len(substring), longest_substring)
            substring = set()
        return longest_substring


s = "aab"
print(lengthOfLongestSubstring(s))

