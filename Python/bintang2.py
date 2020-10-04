from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def bintang():
     gluOrtho2D(-5, 5, -5, 5)
     glBegin(GL_TRIANGLE_STRIP)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(1,1)
     glVertex2f(0,3.75)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(1,1)
     glVertex2f(4,1)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(1.5,-0.5)
     glVertex2f(2.25,-3)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(0,-1.25)
     glVertex2f(2.25,-3)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(0,-1.25)
     glVertex2f(-2.25,-3)
     
     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(-1.5,-0.5)
     glVertex2f(-2.25,-3)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(-1.5,-0.5)
     glVertex2f(-4.,1.)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(-1,1)
     glVertex2f(0,3.75)

     glEnd()
     glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("The Star Program")
glClearColor(0,0,0,0)
glutDisplayFunc(bintang)
glutMainLoop()
