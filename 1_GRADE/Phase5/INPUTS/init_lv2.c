
void thing1(int a)
{
    int b = a;
    putint(b);
    putchar(10);
    return;
}

void thing2(float x)
{
    float z = x;
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
