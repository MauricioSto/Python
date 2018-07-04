# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(p):
    # Your code here
    if p == [] or len(p[0]) == 1:
        return True
    nlinha = len(p)
    ncoluna = len(p[0])
    if nlinha == ncoluna:
        i = 0
        l = 0
        while i < nlinha:
            while l < ncoluna:
                if p[i][l] != p[l][i]:
                    return False
                l = l + 1
            i = i + 1
        return True
    return False


print(symmetric([[1, 2, 3],
                 [2, 3, 4],
                [3, 4, 1]]))
# >>> True

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
# >>> True

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]]))
# >>> False

print(symmetric([[1, 2],
                 [2, 1]]))
# >>> True

print(symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]]))
# >>> False

print(symmetric([[1, 2, 3],
                 [2, 3, 1]]))
# >>> False