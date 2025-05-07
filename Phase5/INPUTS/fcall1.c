
int hexdigit(int d)
{
    return d + 48 + (d/10)*39;
}

void writebits(int d0, int d1, int d2, int d3)
{
    putchar(d3+48);
    putchar(d2+48);
    putchar(d1+48);
    putchar(d0+48);
    return;
}

void writebinary(int hex)
{
    int b1, b2, b3, b4;
    b1 = hex % 2;
    b2 = (hex / 2) % 2;
    b3 = (hex / 4) % 2;
    b4 = (hex / 8) % 2;
    writebits(b1, b2, b3, b4);
    return;
}

char write_8hex(int h0, int h1, int h2, int h3, int h4, int h5, int h6, int h7)
{
    putchar(hexdigit(h7));
    putchar(hexdigit(h6));
    putchar(hexdigit(h5));
    putchar(hexdigit(h4));
    putchar(hexdigit(h3));
    putchar(hexdigit(h2));
    putchar(hexdigit(h1));
    putchar(hexdigit(h0));
    putchar(10);
    return 'a';
}

void write_8bin(int h0, int h1, int h2, int h3, int h4, int h5, int h6, int h7)
{
    writebinary(h7);
    putchar(58);
    writebinary(h6);
    putchar(58);
    writebinary(h5);
    putchar(58);
    writebinary(h4);
    putchar(58);
    writebinary(h3);
    putchar(58);
    writebinary(h2);
    putchar(58);
    writebinary(h1);
    putchar(58);
    writebinary(h0);
    putchar(10);
    return;
}

int main()
{
    int i, id1, id2, id3, id4, id5, id6, id7;
    i = getint();
    id1 = i / 16;
    id2 = id1 / 16;
    id3 = id2 / 16;
    id4 = id3 / 16;
    id5 = id4 / 16;
    id6 = id5 / 16;
    id7 = id6 / 16;
    putint(i);
    putchar(10);
    i = i % 16;
    id1 = id1 % 16;
    id2 = id2 % 16;
    id3 = id3 % 16;
    id4 = id4 % 16;
    id5 = id5 % 16;
    id6 = id6 % 16;
    id7 = id7 % 16;
    write_8hex(i, id1, id2, id3, id4, id5, id6, id7);
    write_8bin(i, id1, id2, id3, id4, id5, id6, id7);
    return 0;
}
