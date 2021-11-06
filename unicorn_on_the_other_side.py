from pygame.locals import *

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from initialization import position

verticies1 = (
    (1, -1, -1),  # 0
    (1, 1, -1),  # 1
    (-1, 1, -1),  # 2
    (-1, -1, -1),  # 3
    (1, -1, 1),  # 4
    (1, 1, 1),  # 5
    (-1, -1, 1),  # 6
    (-1, 1, 1)  # 7
)

verticies4 = (
    (1, -1, -40),  # 0
    (1, 1, -40),  # 1
    (-1, 1, -40),  # 2
    (-1, -1, -40),  # 3
    (1, -1, 1),  # 4
    (1, 1, 1),  # 5
    (-1, -1, -1),  # 6
    (-1, 1, -1)  # 7
)

main_verticies = (
    (10, -10, -25),
    (10, 10, -25),
    (-10, 10, -25),
    (-10, -10, -25),
    (10, -10, 25),
    (10, 10, 25),
    (-10, -10, 25),
    (-10, 10, 25)

)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)


def set_vertices(x):
    x_value_change = position[x][0] - 40  # define central gravity (-40)
    y_value_change = position[x][1] - 40
    z_value_change = -25


    new_vertices = []

    for vert in verticies1:
        new_vert = []

        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices


def Cube(verticies):
    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv((1, 1, 1))
            glVertex3fv(verticies[vertex])

    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Other_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv((1, 0, 0))
        for vertex in surface:
            glVertex3fv(verticies4[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies4[vertex])

    glEnd()


def Main_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv((1, 0, 1))
        for vertex in surface:
            glVertex3fv(main_verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(main_verticies[vertex])

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(100, (display[0] / display[1]), 0.1, 50.0)
    # glTranslatef(-10.0, 10.0, -60)# x and y !!! HERE
    glTranslatef(-4.0, -4.0, -60)
    # glRotatef(0, 0, 0, 0)

    cube_dict = {}

    for x in range(len(position)):
        cube_dict[x] = set_vertices(x)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glTranslatef(0.0, 0.0, 1.0)
        # glTranslatef(0.0, 0.0, .50)
        glRotatef(10, 0, 1, 0)
        # glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])
        Main_cube()
        Other_cube()
        # glTranslatef(5.0, 5.0, -200)
        pygame.display.flip()
        pygame.time.wait(10)


main()
