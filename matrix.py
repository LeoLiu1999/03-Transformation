import math

def print_matrix( matrix ):
    prtstr = ""
    for row in matrix:
        prtstr += "["
        for item in row:
            prtstr += str(item) + "\t"
        prtstr += "]\n"
    print prtstr

def ident( matrix ):
    for c in range(4):
        for r in range(4):
            if (r == c):
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    dim = len(m2[0])
    m_out = new_matrix(cols = dim)
    for a in range(4):
        for b in range(dim):
            #calculate value for (a, b)
            sum = 0
            n = 0
            while (n < 4):
                sum += m1[a][n] * m2[n][b]
                n += 1
            m_out[a][b] = sum
    for a in range(4):
        for b in range(dim):
            m2[a][b] = m_out[a][b]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


'''
test code

m1 = new_matrix()

n = 1
for x in range(4):
    for y in range(4):
        m1[x][y] = n
        n += 1

print_matrix(m1)
matrix_mult(m1, m1)
print_matrix(m1)
'''
