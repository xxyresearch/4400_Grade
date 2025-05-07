
define _test1 {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iload[_ ]0
    imul
    iconst_3 OR [bs]ipush 3 OR ldc 3
    iadd
    dup OR SKIP
    putstatic [Ff]ield .* gvc I
}

within thing1
    NAME int c = expr
    MATCH _test1
done

define _test2a {
    fload[_ ]0
    fload[_ ]0
    fmul
    fload[_ ]0
    fmul
    dup OR SKIP
    putstatic [Ff]ield .* gvx F
}

define _test2b {
    fload[_ ]0
    fload[_ ]0
    fload[_ ]0
    fmul
    fmul
    dup OR SKIP
    putstatic [Ff]ield .* gvx F
}

within thing2
    NAME float x = expr
    MATCH _test2a OR _test2b
done

