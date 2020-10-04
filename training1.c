#include <GL/glut.h>

void userdraw()
{
static int tick=0;

    /*BIKIN TITIK*/
    glColor3f(0.,0.,0.);
    glPointSize(3);
    glBegin(GL_POINTS);
        glVertex2f(125,150);
    glEnd();

    glColor3f(0.,1.,0.);
    glPointSize(10);
    glBegin(GL_POINTS);
        glVertex2f(160,150);
    glEnd();

    glColor3f(0.,0.,1.);
    glPointSize(20);
    glBegin(GL_POINTS);
        glVertex2f(200,150);
    glEnd();

}
void display(void)
{
glClear(GL_COLOR_BUFFER_BIT);
userdraw();
glutSwapBuffers();
}

int main(int argc, char **argv)
{
glutInit(&argc,argv);
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);
glutInitWindowPosition(100,100);
glutInitWindowSize(640,480);
glutCreateWindow("Program Grafikku");
glClearColor(1.0,1.0,1.0,0.0);
gluOrtho2D(0.,640.,-240.,500.);
glutIdleFunc(display);
glutDisplayFunc(display);
glutMainLoop();
return 0;
}

