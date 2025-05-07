
char v()
{
    return 'v';     // char literal as a return
}

void myputc(char x)
{
    int c;
    c = (int) x;
    c = c + 1;
    putchar(c);
}

int main()
{
    char a;
    a = 'k';
    myputc('G');
    myputc('d');
    myputc(a);
    myputc(a);
    myputc('n');
    putchar(10);
    myputc(v());
    myputc('n');
    myputc('q');
    myputc(a);
    myputc('c');
    myputc(' ');
    putchar(10);
    return 0;
}
