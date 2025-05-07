
void thing1(int a)
{
    int c;
    putint(c = 2*a+3);
    putchar(10);
    return;
}

void thing2(float a)
{
    float x;
    putfloat(x = a*a*a);
    putchar(10);
    return;
}

int main()
{
    thing1(2);
    thing2(2.0);
    return 0;
}
