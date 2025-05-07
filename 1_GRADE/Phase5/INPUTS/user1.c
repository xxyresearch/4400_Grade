// NORUN
// YESDOT

int x;

void func1(int a)
{
  return;
}

void func2()
{
  int b;
  b=x;
  return;
}

void func3(int a, int b, char c, float f)
{
    int d, e;
    x=a+b+(int)c+(int)f;
    return;
}

int main()
{
    func3(1, 2, '3', 4.0);
    putint(x);
    putchar(10);
    return 15;
}
