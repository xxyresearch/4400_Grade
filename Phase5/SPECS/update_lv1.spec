
define _test1 {
    iload[ _]0
    iload[ _]1
    isub
    dup OR SKIP
    istore[ _]0
}
define _test1s {
    iload[ _]1
    iload[ _]0
    swap
    isub
    dup OR SKIP
    istore[ _]0
}

within test1
    NAME a -= b
    MATCH _test1
done

# ----------------------------------------

define _test2 {
    fload[ _]0
    fload[ _]1
    swap OR SKIP
    fadd
    dup OR SKIP
    fstore[ _]0
}

define _test2s {
    fload[ _]1
    fload[ _]0
    swap OR SKIP
    fadd
    dup OR SKIP
    fstore[ _]0
}

within test2
    NAME c += d
    MATCH _test2
done

# ----------------------------------------

define _test3 {
    iload[ _]1
    iload[ _]0
    swap OR SKIP
    imul
    dup OR SKIP
    istore[ _]1
}

define _test3s {
    iload[ _]0
    iload[ _]1
    swap OR SKIP
    imul
    dup OR SKIP
    istore[ _]1
}

within test3
    NAME b *= a
    MATCH _test3
done

# ----------------------------------------

define _test4 {
    fload[ _]1
    fload[ _]0
    fdiv
    dup OR SKIP
    fstore[ _]1
}
define _test4s {
    fload[ _]0
    fload[ _]1
    swap
    fdiv
    dup OR SKIP
    fstore[ _]1
}

within test4
    NAME d /= c
    MATCH _test4 OR _test4s
done


