import math
import random
from pygame.locals import *

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from initialization import position

main_verticies = (
    (4, -1, -2),  # 0
    (4, 1, -2),  # 1
    (4, 1, -1),  # 2
    (4, -1, -1),  # 3
    (-1, -1, -2),  # 4
    (-1, 1, -2),  # 5
    (-1, -1, -1),  # 6
    (-1, 1, -1),  # 7""

)
verticies = (
    (4, -1, 1),  # 0
    (4, 1, 1),  # 1
    (4, 1, -2),  # 2
    (4, -1, -2),  # 3
    (3, -1, 1),  # 4
    (3, 1, 1),  # 5
    (3, -1, -2),  # 6
    (3, 1, -2),  # 7""

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


def Main_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        glColor3fv((1, 1, 1))
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

    gluPerspective(50, (display[0] / display[1]), 0.1, 50.0)
    # glTranslatef(5.0, 5.0, -30) x and y !!! HERE
    glTranslatef(-4.0, -4.0, -20)
    # glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glTranslatef(0.0, 0.0, 1.0)
        # glTranslatef(0.0, 0.0, .50)
        # glRotatef(0, 0, 0, 0)
        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Main_cube()
        # glTranslatef(5.0, 5.0, 0.0)
        pygame.display.flip()
        pygame.time.wait(10)


main()
