
define _test1 {
    getstatic [fF]ield .* CA [\[]C
    iconst_3 OR [bs]ipush 3 OR ldc 3
    iload[ _]0
    dup_x2 OR SKIP
    castore
}

define _test1s {
    iconst_3 OR [bs]ipush 3 OR ldc 3
    getstatic [fF]ield .* CA [\[]C
    swap
    iload[ _]0
    dup_x2 OR SKIP
    castore
}

within test1
    NAME CA[3]=c
    MATCH _test1 OR _test1s
done

# ----------------------------------------------------

define _test2 {
    getstatic [fF]ield .* IA [\[]I
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iload[ _]0
    dup_x2 OR SKIP
    iastore
}

define _test2s {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    getstatic [fF]ield .* IA [\[]I
    swap
    iload[ _]0
    dup_x2 OR SKIP
    iastore
}

within test2
    NAME IA[2]=b
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    getstatic [fF]ield .* FA [\[]F
    iload_0
    ldc [+]?2[.]7
    dup_x2
    fastore
}

define _test3s {
    iload_0
    getstatic [fF]ield .* FA [\[]F
    swap
    ldc [+]?2[.]7
    dup_x2
    fastore
}

within test3
    NAME ret F[i]=2.7
    MATCH _test3 OR _test3s
done

