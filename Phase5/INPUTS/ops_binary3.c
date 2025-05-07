
char test1()
{
  return '!' + '(';
}

char test2(char x)
{
  return '0' + x;
}

char test3(char x, char y)
{
  return x + y;
}

char test4()
{
  return 'T' - '#';
}

char test5(char x)
{
  return x - ' ';
}

char test6(char x, char y)
{
  return x - y;
}

void show(char x)
{
    putint((int)x);
    putchar(10);
    return;
}

int main()
{
    show(test1());

    show(test2('1'));
    show(test2('A'));

    show(test3(' ', 'A'));
    show(test3('+', '-'));
    show(test3('!', '!'));

    show(test4());

    show(test5('W'));
    show(test5('Q'));

    show(test6('b', 'B'));
    show(test6('9', '0'));

    return 0;
}

