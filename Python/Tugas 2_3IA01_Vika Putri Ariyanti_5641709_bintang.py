from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

def bintang():
     gluOrtho2D(-4,4,-4,4)
     glBegin(GL_TRIANGLE_STRIP)

     glColor3f(0,0,1)
     glVertex2f(0,0)
     glVertex2f(1,1)
     glVertex2f(0,3.5)

     glColor3f(1,0,0)
     glVertex2f(0,0)
     glVertex2f(1,1)
     glVertex2f(3.5,1)

     glColor3f(0,0,1)
     glVertex2f(0,0)
     glVertex2f(1,1)
     glVertex2f(3.5,1)

     glColor3f(1,1,0)
     glVertex2f(0,0)
     glVertex2f(1.5,-0.5)
     glVertex2f(2.25,-3)

     glColor3f(1,0,1)
     glVertex2f(0,0)
     glVertex2f(0,-1.25)
     glVertex2f(2.25,-3)

     glColor3f(0,1,1)
     glVertex2f(0,0)
     glVertex2f(0,-1.25)
     glVertex2f(-2.25,-3)
     
     glColor3f(0,1,0)
     glVertex2f(0,0)
     glVertex2f(-1.5,-0.5)
     glVertex2f(-2.25,-3)

     glColor3f(0,0,1)
     glVertex2f(0,0)
     glVertex2f(-1,1)
     glVertex2f(-3.5,1)

     glColor3f(0,1,0)
     glVertex2f(0,0)
     glVertex2f(-1.5,-0.5)
     glVertex2f(-3.5,1)

     glColor3f(1,0,1)
     glVertex2f(0,0)
     glColor3f(0,1,1)
     glVertex2f(-1,1)
     glColor3f(1,1, 0)
     glVertex2f(0,3.5)

     glEnd()
     glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("The Star Program")
glClearColor(0,1,0,1)
glutDisplayFunc(bintang)
glutMainLoop()
