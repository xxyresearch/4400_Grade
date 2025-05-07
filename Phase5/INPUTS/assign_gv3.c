
int gvc;
float gvx;

void thing1(int a)
{
    gvc = 2*a+3;
    putint(gvc);
    putchar(10);
    return;
}

void thing2(float a)
{
    gvx = a*a*a;
    putfloat(gvx);
    putchar(10);
    return;
}

int main()
{
    thing1(2);
    thing2(2.0);
    return 0;
}
