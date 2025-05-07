
// YESDOT

int A;

void voidfunc(int b)
{
    A = b;
}

float floatfunc()
{
    return 4.321;
}

int main()
{
    A = 0;
    voidfunc(5);
    return A;
}
