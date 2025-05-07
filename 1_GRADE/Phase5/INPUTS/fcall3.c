
float first()
{
    return 0.1;
}

float second()
{
    return 0.011;
}

float third()
{
    return 0.0001111;
}

float fourth()
{
    return 0.000000011111111;
}

float fifth()
{
    return 0.0000000000000001111111111111111;
}

float ninex(float a, float b, float c, float d, float e)
{
    return 9.0 * (a+b+c+d+e);
}

int main()
{
    putfloat(ninex(first(), second(), third(), fourth(), fifth()));
    putchar(10);
    return 0;
}
