
int b;
float z;

void thing1(int a)
{
    b = a;
    putint(b);
    putchar(10);
    return;
}

void thing2(float x)
{
    z = x;
    putfloat(z);
    putchar(10);
    return;
}

int main()
{
    thing1(7);
    thing2(7.0);
    return 0;
}
