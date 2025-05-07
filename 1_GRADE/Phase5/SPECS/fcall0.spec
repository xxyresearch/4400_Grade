within myputc
    NAME putchar(I)I
    MATCH invokestatic [Mm]ethod lib440 putchar [(]I[)]I

    NAME void return
    MATCH return
done

within zero2space
    NAME char return
    MATCH ireturn
done

within digit2char
    NAME char return
    MATCH ireturn
done

within put2
    NAME digit2char(I)C
    MATCH invokestatic [Mm]ethod fcall0 digit2char [(]I[)]C

    NAME zero2space(C)C
    MATCH invokestatic [Mm]ethod fcall0 zero2space [(]C[)]C

    NAME myputc(C)V
    MATCH invokestatic [Mm]ethod fcall0 myputc [(]C[)]V

    NAME void return
    MATCH return
done

define parmwedge {
  [bs]ipush 94  OR  ldc 94
  myputc
}
define parmc2 {
  [bs]ipush 50  OR  ldc 50
  myputc
}
define parmsp {
  [bs]ipush 32  OR  ldc 32
  myputc
}
define parmeq {
  [bs]ipush 61  OR  ldc 61
  myputc
}

within row
    NAME Parameter '^'
    MATCH parmwedge

    NAME Parameter '2'
    MATCH parmc2

    NAME Parameter ' '
    MATCH parmsp

    NAME Parameter '='
    MATCH parmeq

    NAME put2(II)V
    MATCH invokestatic [Mm]ethod fcall0 put2 [(]II[)]V
done

define parm0 {
  iconst_0  OR  [bs]ipush 0  OR  ldc 0
  row
}
define parm1 {
  iconst_1  OR  [bs]ipush 1  OR  ldc 1
  row
}
define parm2 {
  iconst_2  OR  [bs]ipush 2  OR  ldc 2
  row
}
define parm3 {
  iconst_3  OR  [bs]ipush 3  OR  ldc 3
  row
}
define parm4 {
  iconst_4  OR  [bs]ipush 4  OR  ldc 4
  row
}
define parm5 {
  iconst_5  OR  [bs]ipush 5  OR  ldc 5
  row
}
define parm6 {
  [bs]ipush 6  OR  ldc 6
  row
}
define parm7 {
  [bs]ipush 7  OR  ldc 7
  row
}
define parm8 {
  [bs]ipush 8  OR  ldc 8
  row
}
define parm9 {
  [bs]ipush 9  OR  ldc 9
  row
}
define ret10 {
  [bs]ipush 10  OR  ldc 10
  ireturn
}

within main
    NAME Parameter 0
    MATCH parm0

    NAME Parameter 1
    MATCH parm1

    NAME Parameter 2
    MATCH parm2

    NAME Parameter 3
    MATCH parm3

    NAME Parameter 4
    MATCH parm4

    NAME Parameter 5
    MATCH parm5

    NAME Parameter 6
    MATCH parm6

    NAME Parameter 7
    MATCH parm7

    NAME Parameter 8
    MATCH parm8

    NAME Parameter 9
    MATCH parm9

    NAME int return
    MATCH ireturn

    NAME Return 10
    MATCH ret10
done

