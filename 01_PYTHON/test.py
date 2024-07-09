def min_deletions_to_palindrome(N, K, A, S):
    # Step 2: Count characters in S
    from collections import Counter
    char_count = Counter(S)
    
    # Step 3: Dynamic Programming initialization
    max_len = max(A)  # Maximum length we need to consider based on A
    dp = [[float('inf')] * (max_len + 1) for _ in range(N + 1)]
    
    # Step 4: Palindrome check function
    def can_form_palindrome(s):
        odd_count = sum(1 for count in Counter(s).values() if count % 2 != 0)
        return odd_count <= 1
    
    # Step 5: DP calculation
    dp[0][0] = 0  # Base case: 0 deletions needed for empty string
    
    for l in range(1, N + 1):
        for a in A:
            if l >= a:
                # Create substring of length 'a' ending at position 'l'
                substr = S[l - a:l]
                if can_form_palindrome(substr):
                    dp[l][a] = min(dp[l - a][b] + (sum(char_count[c] for c in substr) - 2), dp[l][a])
                else:
                    dp[l][a] = min(dp[l][a], dp[l - 1][a])
    
    # Step 6: Find the minimum deletions needed for any length in A
    min_deletions = float('inf')
    for a in A:
        min_deletions = min(min_deletions, dp[N][a])
    
    return min_deletions

# Example input directly integrated
input_str = """9
3
1
3
5
zacbsaabs
"""

# Split the input into lines
lines = input_str.strip().split('\n')

# First line: N
N = int(lines[0])

# Second line: K
K = int(lines[1])

# Third to (Third + K) lines: Array A
A = list(map(int, lines[2:2 + K]))

# Last line: String S
S = lines[2 + K]

# Call the function
result = min_deletions_to_palindrome(N, K, A, S)
print(result)
