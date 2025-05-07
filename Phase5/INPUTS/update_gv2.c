
int a, b;
float c, d;

int test1(int b)
{
  return a -= b;
}

float test2(float d)
{
  return c += d;
}

int test3(int a)
{
  return b *= a;
}

float test4(float c)
{
  return d /= c;
}
