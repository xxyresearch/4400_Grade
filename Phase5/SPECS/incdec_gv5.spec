
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

# --------------------------------------------------

define _addi0 {
    getstatic [Ff]ield .* donuts_consumed I
    dup OR SKIP
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* donuts_consumed I
}

define _addi0s {
    getstatic [Ff]ield .* donuts_consumed I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* donuts_consumed I
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* donuts_consumed I
}

within test1
    NAME donuts_consumed++
    MATCH _addi0  OR  _addi0s
done

# --------------------------------------------------

define _addf0 {
    getstatic [Ff]ield .* calories F
    dup OR SKIP
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* calories F
}

define _addf0s {
    getstatic [Ff]ield .* calories F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* calories F
    swap OR SKIP
    fadd
    dup OR SKIP
    putstatic [Ff]ield .* calories F
}

within test2
    NAME calories++
    MATCH _addf0  OR  _addf0s
done

