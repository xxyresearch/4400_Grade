
define _dupsti0 {
    dup
    istore[ _]0
}
define _stldi0 {
    istore[ _]0
    iload[ _]0
}

define _test1 {
    iload[ _]0
    iload[ _]1
    isub
    _dupsti0 OR _stldi0
}
define _test1s {
    iload[ _]1
    iload[ _]0
    swap
    isub
    _dupsti0 OR _stldi0
}

within test1
    NAME return a -= b
    MATCH _test1
done

# ----------------------------------------

define _dupstf0 {
    dup
    fstore[ _]0
}
define _stldf0 {
    fstore[ _]0
    fload[ _]0
}

define _test2 {
    fload[ _]0
    fload[ _]1
    swap OR SKIP
    fadd
    _dupstf0 OR _stldf0
}

define _test2s {
    fload[ _]1
    fload[ _]0
    swap OR SKIP
    fadd
    _dupstf0 OR _stldf0
}

within test2
    NAME return c += d
    MATCH _test2
done

# ----------------------------------------

define _dupsti1 {
    dup
    istore[ _]1
}
define _stldi1 {
    istore[ _]1
    iload[ _]1
}

define _test3 {
    iload[ _]1
    iload[ _]0
    swap OR SKIP
    imul
    _dupsti1 OR _stldi1
}

define _test3s {
    iload[ _]0
    iload[ _]1
    swap OR SKIP
    imul
    _dupsti1 OR _stldi1
}

within test3
    NAME return b *= a
    MATCH _test3
done

# ----------------------------------------

define _dupstf1 {
    dup
    fstore[ _]1
}
define _stldf1 {
    fstore[ _]1
    fload[ _]1
}

define _test4 {
    fload[ _]1
    fload[ _]0
    fdiv
    _dupstf1 OR _stldf1
}
define _test4s {
    fload[ _]0
    fload[ _]1
    swap
    fdiv
    _dupstf1 OR _stldf1
}

within test4
    NAME return d /= c
    MATCH _test4 OR _test4s
done


