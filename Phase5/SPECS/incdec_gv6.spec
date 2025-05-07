
define _int1tofloat {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    i2f
}

# --------------------------------------------------

define _addi0 {
    getstatic [Ff]ield .* Ga I
    dup OR getstatic [Ff]ield .* Ga I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* Ga I
}

define _addi0s {
    getstatic [Ff]ield .* Ga I
    iconst_1 OR [bs]ipush 1 OR ldc 1
    getstatic [Ff]ield .* Ga I
    swap OR SKIP
    iadd
    putstatic [Ff]ield .* Ga I
}

within test1
    NAME return Ga++
    MATCH _addi0  OR  _addi0s
done

# --------------------------------------------------

define _addf0 {
    getstatic [Ff]ield .* Gx F
    dup OR getstatic [Ff]ield .* Gx F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* Gx F
}

define _addf0s {
    getstatic [Ff]ield .* Gx F
    fconst_1 OR ldc [+]?1[.]0 OR _int1tofloat
    getstatic [Ff]ield .* Gx F
    swap OR SKIP
    fadd
    putstatic [Ff]ield .* Gx F
}

within test2
    NAME return Gx++
    MATCH _addf0  OR  _addf0s
done

