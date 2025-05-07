
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

# --------------------------------------------------

define _addi0 {
    iload[ _]0
    dup OR iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    istore[ _]0
}

define _addi0s {
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap OR SKIP
    iadd
    istore[ _]0
}

within test1
    NAME return a++
    MATCH iinc 0 1  OR  _addi0  OR  _addi0s
done

# --------------------------------------------------

define _addf0 {
    fload[ _]0
    dup OR fload[ _]0
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    fstore[ _]0
}

define _addf0s {
    fload[ _]0
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]0
    swap OR SKIP
    fadd
    fstore[ _]0
}

within test2
    NAME return x++
    MATCH _addf0  OR  _addf0s
done

# --------------------------------------------------

define _addi1 {
    iload[ _]1
    dup OR iload[ _]1
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    istore[ _]1
}

define _addi1s {
    iload[ _]1
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]1
    swap OR SKIP
    iadd
    istore[ _]1
}

within test3
    NAME return b++
    MATCH iinc 1 1  OR  _addi1  OR  _addi1s
done

# --------------------------------------------------

define _addf1 {
    fload[ _]1
    dup OR fload[ _]1
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    fstore[ _]1
}

define _addf1s {
    fload[ _]1
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    fload[ _]1
    swap OR SKIP
    fadd
    fstore[ _]1
}

within test4
    NAME return y++
    MATCH _addf1  OR  _addf1s
done

