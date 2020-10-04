from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
     
def gambar():
     gluOrtho2D(0.0, 2.5, 0.0, 2.5)
     glBegin(GL_TRIANGLE_STRIP)

     glColor3f(1.0,1.0,0.0)
     glVertex2f(0.2,0.5)
     
     glColor3f(0.,1.,0.)
     glVertex2f(0.2,2.0)
     
     glColor3f(0.,1.,1.)
     glVertex2f(2.0,0.5)
     
     glColor3f(1.,0.,1.)
     glVertex2f(2,2.0)

     glEnd()
     glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow("KOTAK")
glClearColor(0.0, 0.0, 0.0, 0.0)
glutDisplayFunc(gambar)
glutMainLoop()
