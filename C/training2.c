#include <GL/glut.h>
#include <math.h>

typedef struct {
float x;
float y;
} point2D_t;

typedef struct {
int x;
int y;
} point2D_t;

typedef struct {
float r;
float g;
float b;
} color_t;

void setColor(color_t col){
glColor3f(col.r, col.g, col.b);
}

void drawPolygon(point2D_t pnt[], int n){
int i;
glBegin(GL_LINE_LOOP);
for (i=0;i<n;i++){
glVertex2f(pnt[i].x,pnt[i].y);
}
glEnd();
}

void userdraw(){
point 2D_t kotak[4]={{100,100},{300,100},{300,200},{100,200}};
setColor(1,0,0);
drawPolygon(kotak,4);
}

void display(void){
glClear(GL_COLOR_BUFFER_BIT);
userdraw();
glutswapBuffers();
}
