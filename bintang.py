from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def star() :
    gluOrtho2D(-4.0, 4.0, -4.0, 4.0)
    glBegin(GL_TRIANGLE_STRIP)

    #1
    glColor3f(0., 1., 0.)
    glVertex2f(0., 0.)
    glColor3f(1., 0., 0.)
    glVertex2f(1., 1.)
    glColor3f(0., 0., 1.)
    glVertex2f(0., 3.75)

    #2
    glColor3f(1., 1., 0.)
    glVertex2f(0., 0.)
    glColor3f(1., 0., 1.)
    glVertex2f(1., 1.)
    glColor3f(0., 1., 1.)
    glVertex2f(4., 1.)

    #3
    glColor3f(0., 1., 0.)
    glVertex2f(0., 0.)
    glColor3f(0., 0., 1.)
    glVertex2f(1.5, 0.5)
    glColor3f(1., 0., 0.)
    glVertex2f(4., 1.)

    #4
    glColor3f(0., 1., 1.)
    glVertex2f(0., 0.)
    glColor3f(1., 0., 1.)
    glVertex2f(1.5, 0.5)
    glColor3f(1., 1., 0.)
    glVertex2f(2.5, -3.)

    #5
    glColor3f(0., 0., 1.)
    glVertex2f(0., 0.)
    glColor3f(0., 1., 0.)
    glVertex2f(0., -1.25)
    glColor3f(1., 0., 0.)
    glVertex2f(2.25, -3.)

    #6
    glColor3f(1., 0., 1.)
    glVertex2f(0., 0.)
    glColor3f(1., 1., 0.)
    glVertex2f(0., -1.25)
    glColor3f(0., 1., 1.)
    glVertex2f(-2.25, -3.)

    #7
    glColor3f(1., 0., 0.)
    glVertex2f(0., 0.)
    glColor3f(0., 1., 0.)
    glVertex2f(-1.5, -0.5)
    glColor3f(0., 0., 1.)
    glVertex2f(-2.25, -3.)

    #8
    glColor3f(1., 1., 0.)
    glVertex2f(0., 0.)
    glColor3f(1., 0., 1.)
    glVertex2f(-1.5, -0.5)
    glColor3f(0., 1., 1.)
    glVertex2f(-4., 1.)

    #9
    glColor3f(0., 0., 1.)
    glVertex2f(0., 0.)
    glColor3f(0., 1., 0.)
    glVertex2f(-1., 1.)
    glColor3f(1., 0., 0.)
    glVertex2f(-4., 1.)

    #10
    glColor3f(1., 0., 1.)
    glVertex2f(0., 0.)
    glColor3f(0., 1., 1.)
    glVertex2f(-1., 1.)
    glColor3f(1., 1., 0.)
    glVertex2f(0., 3.75)

    glEnd()
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Star Program")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(star)
glutMainLoop()
# End of program
