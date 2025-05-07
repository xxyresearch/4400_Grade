
void foo(int a, char b)
{
}

int bar(float x)
{
    return 0;
}

char getchar()
{
    return 'a';
}

int nest(int n)
{
    return 1;
}

void test()
{
  foo(3, '4');
  bar(5.6);
  getchar();

  foo(bar(5.7), getchar());

  nest(nest(nest(nest(nest(bar(7.6))))));
}
