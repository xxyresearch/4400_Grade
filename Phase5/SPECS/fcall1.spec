
within hexdigit
    NAME int return
    MATCH ireturn
done

define fourp {
    iload[_ ]1
    iload[_ ]2
    iload[_ ]3
    iload 4
    writebits
}

within writebinary
    NAME parameters
    MATCH fourp

    NAME writebits()
    MATCH invokestatic [Mm]ethod fcall1 writebits [(]IIII[)]V

    NAME void return
    MATCH return
done

define onep {
    iload 7
    hexdigit
}

define seq {
    hexdigit
    putchar
}

within write_8hex
    NAME parameters
    MATCH onep

    NAME hexdigit()
    MATCH invokestatic [Mm]ethod fcall1 hexdigit [(]I[)]I

    NAME nested function call
    MATCH seq

    NAME char return
    MATCH ireturn
done

within write_8bin
    NAME parameters 1
    MATCH iload 6

    NAME parameters 2
    MATCH [bs]ipush 58  OR  ldc 58

    NAME writebinary()
    MATCH invokestatic [Mm]ethod fcall1 writebinary [(]I[)]V

    NAME void return
    MATCH return
done

define put_i {
  iload_0
  putint
}
define params8 {
  iload[_ ]0
  iload[_ ]1
  iload[_ ]2
  iload[_ ]3
  iload 4
  iload 5
  iload 6
  iload 7
}
define call_8hex {
  params8
  write_8hex
}
define call_8bin {
  params8
  write_8bin
}

note Some of the tests in main are slow

within main
    NAME 1 parameter
    MATCH put_i

    NAME 8 params
    MATCH call_8hex

    NAME 8 params
    MATCH call_8bin

    NAME getint()
    MATCH invokestatic [Mm]ethod lib440 getint [(][)]I

    NAME putint()
    MATCH invokestatic [Mm]ethod lib440 putint [(]I[)]V

    NAME putchar()
    MATCH invokestatic [Mm]ethod lib440 putchar [(]I[)]I

    NAME write_8hex()
    MATCH invokestatic [Mm]ethod fcall1 write_8hex [(]IIIIIIII[)]C

    NAME write_8bin()
    MATCH invokestatic [Mm]ethod fcall1 write_8bin [(]IIIIIIII[)]V

    NAME int return
    MATCH ireturn
done

