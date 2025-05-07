
int foo(int x)
{
    return x;
}

void bar()
{
}

int cruft(int a)
{
  foo(a);
  bar();
  foo();  /* error */
}
