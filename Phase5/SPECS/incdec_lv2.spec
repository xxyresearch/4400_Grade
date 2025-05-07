
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

# --------------------------------------------------

define _dupi0 {
    dup
    istore[ _]0
}
define _stldi0 {
    istore[ _]0
    iload[ _]0
}

define _addi0 {
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    _dupi0 OR _stldi0
}

define _addi0s {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap OR SKIP
    iadd
    _dupi0 OR _stldi0
}

within test1
    NAME return ++a
    MATCH iinc 0 1  OR  _addi0  OR  _addi0s
done

# --------------------------------------------------

define _dupf0 {
    dup
    fstore[ _]0
}
define _stldf0 {
    fstore[ _]0
    fload[ _]0
}

define _addf0 {
    fload[ _]0
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    _dupf0 OR _stldf0
}

define _addf0s {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]0
    swap OR SKIP
    fadd
    _dupf0 OR _stldf0
}

within test2
    NAME return ++x
    MATCH _addf0  OR  _addf0s
done

# --------------------------------------------------

define _dupi1 {
    dup
    istore[ _]1
}
define _stldi1 {
    istore[ _]1
    iload[ _]1
}

define _addi1 {
    iload[ _]1
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    _dupi1 OR _stldi1
}

define _addi1s {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]1
    swap OR SKIP
    iadd
    _dupi1 OR _stldi1
}

within test3
    NAME return ++b
    MATCH iinc 1 1  OR  _addi1  OR  _addi1s
done

# --------------------------------------------------

define _dupf1 {
    dup
    fstore[ _]1
}
define _stldf1 {
    fstore[ _]1
    fload[ _]1
}

define _addf1 {
    fload[ _]1
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    _dupf1 OR _stldf1
}

define _addf1s {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]1
    swap OR SKIP
    fadd
    _dupf1 OR _stldf1
}

within test4
    NAME return ++x
    MATCH _addf1  OR  _addf1s
done

