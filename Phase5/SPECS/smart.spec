
define _test1a {
    iconst_5 OR [bs]ipush 5 OR ldc 5
    dup
    istore[_ ]0
}

define _test1b {
    iconst_5 OR [bs]ipush 5 OR ldc 5
    istore[_ ]0
    iload[_ ]0
}

define _sm1 {
    [bs]ipush 6 OR ldc 6
    istore[_ ]0
    return
}

within test1
    NAME needed
    MATCH _test1a OR _test1b

    NAME pops extra
    MATCH pop

    NAME smart
    MATCH _sm1
done

# ------------------------------------------------------------

define _test2a {
    [bs]ipush 15 OR ldc 15
    iload[_ ]1 OR SKIP
    swap OR SKIP
    iadd
    dup
    istore[_ ]1
}

define _test2b {
    [bs]ipush 15 OR ldc 15
    iload[_ ]1 OR SKIP
    swap OR SKIP
    iadd
    istore[_ ]1
    iload[_ ]1
}

define _sm2 {
    [bs]ipush 17 OR ldc 17
    iload[_ ]1 OR SKIP
    swap OR SKIP
    iadd
    istore[_ ]1
    return
}

within test2
    NAME needed
    MATCH _test2a OR _test2b

    NAME smart
    MATCH _sm2
done

# ------------------------------------------------------------

define _test3a {
    [bs]ipush 11 OR ldc 11
    dup
    istore[_ ]0
    istore[_ ]1
}

define _test3b {
    [bs]ipush 11 OR ldc 11
    istore[_ ]0
    iload[_ ]0
    istore[_ ]1
}

define _sm3 {
    [bs]ipush 22 OR ldc 22
    istore[_ ]0
    return
}

within test3
    NAME needed
    MATCH _test3a OR _test3b

    NAME smart
    MATCH _sm3
done

# ------------------------------------------------------------

note Does the student generate a+9 correctly when needed?

within need4
    NAME needed: a
    MATCH iload
    NAME needed: 9
    MATCH 9
    NAME needed: +
    MATCH iadd
done

note What about a pointless expression a+9; ?
note This is a bit beyond what the specs asked for

within omit4
    NAME really smart: a
    OMIT iload

    NAME really smart: 9
    OMIT 9

    NAME really smart: +
    OMIT iadd
done
