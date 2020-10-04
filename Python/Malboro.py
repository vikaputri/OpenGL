from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def garis():
    gluOrtho2D(-3,3,-3,3)
    glBegin(GL_TRIANGLE_STRIP)

    glColor3d(1,1,1)
    glVertex2d(1,1)
    glVertex2d(1,0)
    glVertex2d(0,0)
    glVertex2d(0,1)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3d(0, 1, 1)
    glVertex2f(0, 0)
    glVertex2f(0, -1.0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-1.0, -1.0)
    glVertex2f(-1.0, 0.0)

    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3d(0, 1, 1)
    glVertex2f(0, 0)
    glVertex2f(0, 1.0)
    glVertex2f(-0.5, 0.5)
    glVertex2f(-1.0, 1.0)
    glVertex2f(-1.0, 0.0)

    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    glColor3d(1, 1, 1)
    glVertex2d(1, -1)
    glVertex2d(1, 0)
    glVertex2d(0, 0)
    glVertex2d(0, -1)
    glEnd()

    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutInitWindowPosition(100,100)
glutCreateWindow("Holo-Holo")
glutDisplayFunc(garis)
glutMainLoop()
