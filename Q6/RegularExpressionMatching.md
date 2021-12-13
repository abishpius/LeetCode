Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input: s = "mississippi", p = "mis*is*p*."
Output: false

Approach 2: Dynamic Programming
Intuition

As the problem has an optimal substructure, it is natural to cache intermediate results. We ask the question \text{dp(i, j)}dp(i, j): does \text{text[i:]}text[i:] and \text{pattern[j:]}pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

Algorithm

We proceed with the same recursion as in Approach 1, except because calls will only ever be made to match(text[i:], pattern[j:]), we use \text{dp(i, j)}dp(i, j) to handle those calls instead, saving us expensive string-building operations and allowing us to cache the intermediate results.

Top-Down Variation

Complexity Analysis

Time Complexity: Let T, PT,P be the lengths of the text and the pattern respectively. The work for every call to dp(i, j) for i=0, ... ,Ti=0,...,T; j=0, ... ,Pj=0,...,P is done once, and it is O(1)O(1) work. Hence, the time complexity is O(TP)O(TP).

Space Complexity: The only memory we use is the O(TP)O(TP) boolean entries in our cache. Hence, the space complexity is O(TP)O(TP).