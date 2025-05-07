
void myputc(char c)
{
    putchar( (int) c);
    return;
}

char zero2space(char x)
{
    return x-(char)16 + (char)16 * (x / '1');
}

char digit2char(int x)
{
    return '0' + (char) x;
}

void put2(int d1, int d0)
{
    myputc(zero2space(digit2char(d1)));
    myputc(digit2char(d0));
    return;
}

void row(int i)
{
    myputc(digit2char(i));
    myputc('^');
    myputc('2');
    myputc(' ');
    myputc('=');
    myputc(' ');
    put2( i*i/10, i*i%10 );
    putchar(10);
    return;
}

int main()
{
    row(0);
    row(1);
    row(2);
    row(3);
    row(4);
    row(5);
    row(6);
    row(7);
    row(8);
    row(9);
    return 10;
}
