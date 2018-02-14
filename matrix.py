import math


def print_matrix( matrix ):
    pass

def ident( matrix ):
    for c in range(4):
        for r in range(4):
            if (r == c):
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
