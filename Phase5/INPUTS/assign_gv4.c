
int integrocitor;
float flubbrification;

void thing1(int a)
{
    putint(integrocitor = 2*a+3);
    putchar(10);
    return;
}

void thing2(float a)
{
    putfloat(flubbrification = a*a*a);
    putchar(10);
    return;
}

int main()
{
    thing1(2);
    thing2(2.0);
    return 0;
}
