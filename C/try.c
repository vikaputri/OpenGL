#include <stdio.h>
#include <stdlib.h>
#include <GL/glut.h>
void userdraw(void);
void drawDot(float x, float y)
{
    glBegin(GL_POINTS);
        glVertex2f(x,y);
    glEnd();
}
void drawLine (float x1, float y1, float x2, float y2)
{
    glBegin(GL_LINES);
        glVertex2f(x1,y1);
        glVertex2f(x2,y2);
        glEnd();
}
void setColor(float red, float green, float blue)
{
    glColor3f(red,green,blue);
}
void userdraw(void)
{
    glPointSize(4);
    setColor(1.,1.,1.);
            drawDot(100,40); //point
            
                drawLine(1,1,100,100);//line
                
                    glBegin(GL_POLYGON); //polygon
                    glVertex2f(210,260);
                    glVertex2f(260,260);
                    glVertex2f(260,210);
                    glEnd();
                    
                        glBegin(GL_LINE_STRIP); //polyline
                        glVertex2f(110,160);
                        glVertex2f(110,110);
                        glVertex2f(160,110);
                        glEnd();
}               
void display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    userdraw();
    glFlush();
}
void main(int argc, char **argv)
{
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(640,480);
    glutInitWindowPosition(100,150);
    glutCreateWindow("My First Open Graphic Library");
    glClearColor(0.0,0.0,0.0,0.0);
    gluOrtho2D(0.,640.,0.0,480.0);
    glutDisplayFunc(display);
    glutMainLoop();
}
