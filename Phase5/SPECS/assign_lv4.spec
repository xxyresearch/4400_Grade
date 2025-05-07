
define _dupi {
    dup
    istore[_ ]1
}

define _stild {
    istore[_ ]1
    iload[_ ]1
}

define _test1 {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iload[_ ]0
    imul
    iconst_3 OR [bs]ipush 3 OR ldc 3
    iadd
    _dupi OR _stild
}

within thing1
    NAME int c = expr
    MATCH _test1
done

# ------------------------

define _dupf {
    dup
    fstore[_ ]1
}

define _stfld {
    fstore[_ ]1
    fload[_ ]1
}


define _test2a {
    fload[_ ]0
    fload[_ ]0
    fmul
    fload[_ ]0
    fmul
    _dupf OR _stfld
}

define _test2b {
    fload[_ ]0
    fload[_ ]0
    fload[_ ]0
    fmul
    fmul
    _dupf OR _stfld
}

within thing2
    NAME float x = expr
    MATCH _test2a OR _test2b
done

