from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 255, 255, 255 ]


def generate_pattern(scale = 25):
    mat = new_matrix(rows = 0)
    xcoords = [0,3,2,4,4,3,1,0,2,0,1,2,4,2]
    ycoords = [0,3,0,2,0,1,1,2,2,4,3,4,2,4]
    for i in range(14):
        print "point: {}, {}".format( xcoords[i] * scale, ycoords[i] * scale)
        add_point( mat, xcoords[i] * scale, ycoords[i] * scale, 0)
    return mat

matrix = generate_pattern()


print_matrix(matrix)

for x in range (20):
    trans_mat = []
    trans_mat.append([1,0,0,25])
    trans_mat.append([0,1,0,0])
    trans_mat.append([0,0,1,0])
    trans_mat.append([0,0,0,1])
    matrix = matrix_mult(matrix, trans_mat)
    draw_lines( matrix, screen, color )
display(screen)
