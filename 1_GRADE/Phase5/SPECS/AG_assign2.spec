
define _test1 {
    getstatic [fF]ield .* CA [\[]C
    iload[_ ]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    iload[ _]1
    dup_x2 OR SKIP
    castore
}

define _test1s {
    iload[_ ]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    getstatic [fF]ield .* CA [\[]C
    swap
    iload[ _]1
    dup_x2 OR SKIP
    castore
}

within test1
    NAME CA[i-3]
    MATCH _test1 OR _test1s
done

# ----------------------------------------------------

define _test2 {
    getstatic [fF]ield .* IA [\[]I
    getstatic [fF]ield .* IA [\[]I
    iload[_ ]2
    iaload
    iload[_ ]1
    dup_x2 OR SKIP
    iastore
}

define _test2s {
    iload[_ ]2
    getstatic [fF]ield .* IA [\[]I
    swap
    iaload
    getstatic [fF]ield .* IA [\[]I
    swap
    iload[_ ]1
    dup_x2 OR SKIP
    iastore
}

within test2
    NAME IA[IA[j]]=b
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    getstatic [fF]ield .* FA [\[]F
    invokestatic .* the_index
    ldc [+]?2[.]7
    dup_x2
    fastore
}

define _test3s {
    invokestatic .* the_index
    getstatic [fF]ield .* FA [\[]F
    swap
    ldc [+]?2[.]7
    dup_x2
    fastore
}

within test3
    NAME ret FA[func()]=2.7
    MATCH _test3 OR _test3s
done

