# Recursion Depth Limit

import sys
print(sys.getrecursionlimit()) # Default recursion depth limit is 1000

# GETTER & SETTER for recursion depth limit
sys.setrecursionlimit(2000) # Setting recursion depth limit to 2000
print(sys.getrecursionlimit()) # New recursion depth limit is 2000