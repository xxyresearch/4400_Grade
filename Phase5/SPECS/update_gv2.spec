
define _dupsti0 {
    dup
    putstatic [Ff]ield .* a I
}
define _stldi0 {
    putstatic [Ff]ield .* a I
    getstatic [Ff]ield .* a I
}

define _test1 {
    getstatic [Ff]ield .* a I
    iload[ _]0
    isub
    _dupsti0 OR _stldi0
}
define _test1s {
    iload[ _]0
    getstatic [Ff]ield .* a I
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
    putstatic [Ff]ield .* c F
}
define _stldf0 {
    putstatic [Ff]ield .* c F
    getstatic [Ff]ield .* c F
}

define _test2 {
    getstatic [Ff]ield .* c F
    fload[ _]0
    swap OR SKIP
    fadd
    _dupstf0 OR _stldf0
}

define _test2s {
    getstatic [Ff]ield .* c F
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
    putstatic [Ff]ield .* b I
}
define _stldi1 {
    putstatic [Ff]ield .* b I
    getstatic [Ff]ield .* b I
}

define _test3 {
    getstatic [Ff]ield .* b I
    iload[ _]0
    swap OR SKIP
    imul
    _dupsti1 OR _stldi1
}

define _test3s {
    iload[ _]0
    getstatic [Ff]ield .* b I
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
    putstatic [Ff]ield .* d F
}
define _stldf1 {
    putstatic [Ff]ield .* d F
    getstatic [Ff]ield .* d F
}

define _test4 {
    getstatic [Ff]ield .* d F
    fload[ _]0
    fdiv
    _dupstf1 OR _stldf1
}
define _test4s {
    fload[ _]0
    getstatic [Ff]ield .* d F
    swap
    fdiv
    _dupstf1 OR _stldf1
}

within test4
    NAME return d /= c
    MATCH _test4 OR _test4s
done


