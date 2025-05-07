
define my4 {
  iload[_ ]0
  iload[_ ]3
  iload[_ ]2
  iload[_ ]1
  writebits
}

within write_low4
    NAME 4 params
    MATCH my4

    NAME writebits()
    MATCH invokestatic [Mm]ethod fcall2 writebits [(]IIII[)]V
done

define my1 {
  iload[_ ]1
  write_low
}

define putdot {
  [bs]ipush 46   OR   ldc 46
  invokestatic Method lib440 putchar [(]I[)]I
}

within writebinary
    NAME 1 param
    MATCH my1

    NAME putchar(46)
    MATCH putdot
done


within main
    NAME getfloat()F
    MATCH invokestatic [Mm]ethod lib440 getfloat [(][)]F

    NAME putfloat(F)V
    MATCH invokestatic [Mm]ethod lib440 putfloat [(]F[)]V

    NAME putchar(I)I
    MATCH invokestatic [Mm]ethod lib440 putchar [(]I[)]I
done
