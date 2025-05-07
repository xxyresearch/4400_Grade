
define _dupst1 {
    dup
    putstatic [Ff]ield .* integrocitor I
}

define _ldst1 {
    putstatic [Ff]ield .* integrocitor I
    getstatic [Ff]ield .* integrocitor I
}

define _test1 {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iload[_ ]0
    imul
    iconst_3 OR [bs]ipush 3 OR ldc 3
    iadd
    _dupst1 OR _stld1
}

within thing1
    NAME int c = expr
    MATCH _test1
done

# ------------------------------------------

define _dupst2 {
    dup
    putstatic [Ff]ield .* flubbrification F
}

define _ldst2 {
    putstatic [Ff]ield .* flubbrification F
    getstatic [Ff]ield .* flubbrification F
}

define _test2a {
    fload[_ ]0
    fload[_ ]0
    fmul
    fload[_ ]0
    fmul
    _dupst2 OR _ldst2
}

define _test2b {
    fload[_ ]0
    fload[_ ]0
    fload[_ ]0
    fmul
    fmul
    _dupst2 OR _ldst2
}

within thing2
    NAME float x = expr
    MATCH _test2a OR _test2b
done

