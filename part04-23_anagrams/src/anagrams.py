# Write your solution here
def anagrams(str1: str, str2: str) -> bool:
    return sorted(str1) == sorted(str2)
