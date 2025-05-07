
float f_special()
{
    return 1.0;
}

float f_other()
{
    return 1.414;
}

void println(float x)
{
    putfloat(x);
    putchar(10);
    return;
}

int main()
{
    float a, b;
    a = 0.0;
    b = 1.732;

    println(a);
    println(f_special());
    println(2.0);

    println(f_other());
    println(b);
    println(2.236);

    return 0;
}
