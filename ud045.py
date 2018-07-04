def is_identity_matrix(matrix):
    count=0
    for i in matrix:
        for j in i:
            if count%(len(matrix)+1)==0 and j!=1:
                return False
            elif count%(len(matrix)+1)!=0 and j!=0:
                return False
            count=count+1
    return True