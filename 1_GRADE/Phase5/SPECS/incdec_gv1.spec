
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

# --------------------------------------------------

define _addi0 {
    getstatic [Ff]ield .* a I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    dup OR SKIP
    putstatic [Ff]ield .* a I
}

define _addi0s {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* a I
    swap OR SKIP
    iadd
    dup OR SKIP
    putstatic [Ff]ield .* a I
}

within test1
    NAME ++a
    MATCH _addi0  OR  _addi0s
done

# --------------------------------------------------

define _addf0 {
    getstatic [Ff]ield .* x F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* x F
}

define _addf0s {
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* x F
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* x F
}

within test2
    NAME ++x
    MATCH _addf0  OR  _addf0s
done

