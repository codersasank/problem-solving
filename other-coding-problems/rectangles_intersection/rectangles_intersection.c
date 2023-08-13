#include <stdio.h>
#include <stdlib.h>

int min (int a, int b) {
  if (a < b) {
    return a;
  }
  return b;
}
int max (int a, int b) {
  if (a > b) {
    return a;
  }
  return b;
}

struct rect {
  int x, y, width, height;
};

rectangle canonicalize(rectangle r) {
  if (r.width<0) {
    r.x += r.width;
    r.width = -r.width;
  }
  if (r.height<0) {
    r.y += r.height;
    r.height = -r.height;
  }

  return r;
}
rectangle intersection(rectangle r1, rectangle r2) {
  int x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8, xa,ya, xb, yb;
  r1 = canonicalize(r1);
  r2 = canonicalize(r2);
  if(r1.x<r2.x) {
    x1 = r1.x;
    y1 = r1.y;
    x2 = r1.x + r1.width;
    y2 = r1.y;
    x3 = r1.x + r1.width;
    y3 = r1.y + r1.height;
    x4 = r1.x;
    y4 = r1.y + r1.height;

    x5 = r2.x;
    y5 = r2.y;
    x6 = r2.x + r2.width;
    y6 = r2.y;
    x7 = r2.x + r2.width;
    y7 = r2.y + r2.height;
    x8 = r2.x;
    y8 = r2.y + r2.height;
  }
  else {
    x1 = r2.x;
    y1 = r2.y;
    x2 = r2.x + r2.width;
    y2 = r2.y;
    x3 = r2.x + r2.width;
    y3 = r2.y + r2.height;
    x4 = r2.x;
    y4 = r2.y + r2.height;

    x5 = r1.x;
    y5 = r1.y;
    x6 = r1.x + r1.width;
    y6 = r1.y;
    x7 = r1.x + r1.width;
    y7 = r1.y + r1.height;
    x8 = r1.x;
    y8 = r1.y + r1.height;
  }

  yb = min(y4,y8);
  ya = max(y1,y5);

  xa = max(x5,x1);
  xb = min(x2,x6);

  r1.x = xa;
  r1.y = ya;

  r1.width = xb-xa;
  r1.height = yb-ya;

  if(r1.width<0 || r1.height < 0) {
    r1.width = 0;
    r1.height = 0;
  }

  return r1;
}

void printRectangle(rectangle r) {
  r = canonicalize(r);
  if (r.width == 0 && r.height == 0) {
    printf("No intersection\n");
  }
  else {
    printf("x1,y1 are (%d,%d) and x3,y3 are (%d,%d)\n", r.x, r.y, r.x + r.width, r.y + r.height);
  }
}

int main ()
{
  rectangle r1;
  rectangle r2;
  rectangle r3;
  rectangle r4;

  r1.x = 1;
  r1.y = 2;
  r1.width = 7;
  r1.height = 10;
  printf("Rectangle r1 is :");
  printRectangle(r1);

  rectangle i = intersection(r1,r1);
  printf("intersection(r1,r1): ");
  printRectangle(i);

  return EXIT_SUCCESS;
}
