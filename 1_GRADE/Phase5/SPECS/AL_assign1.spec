
define _test1_0 {
    aload[ _]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    iload[ _]1
    dup_x2 OR SKIP
    castore
}

define _test1_1 {
    aload[ _]1
    iconst_3 OR [bs]ipush 3 OR ldc 3
    iload[ _]0
    dup_x2 OR SKIP
    castore
}

define _test1_0s {
    iconst_3 OR [bs]ipush 3 OR ldc 3
    aload[ _]0
    swap
    iload[ _]1
    dup_x2 OR SKIP
    castore
}

define _test1_1s {
    iconst_3 OR [bs]ipush 3 OR ldc 3
    aload[ _]1
    swap
    iload[ _]0
    dup_x2 OR SKIP
    castore
}

within test1
    NAME A[3]=c
    MATCH _test1_0 OR _test1_1 OR _test1_0s OR _test1_1s
done

# ----------------------------------------------------

define _test2 {
    aload[ _]1
    iconst_2 OR [bs]ipush 2 OR ldc 2
    iload[ _]0
    dup_x2 OR SKIP
    iastore
}

define _test2s {
    iconst_2 OR [bs]ipush 2 OR ldc 2
    aload[ _]1
    swap
    iload[ _]0
    dup_x2 OR SKIP
    iastore
}

within test2
    NAME A[2]=b
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    aload[ _]1
    iload_0
    ldc [+]?3[.]14
    dup_x2
    fastore
}

define _test3s {
    iload_0
    aload[ _]1
    swap
    ldc [+]?3[.]14
    dup_x2
    fastore
}

within test3
    NAME ret F[i]=3.14
    MATCH _test3 OR _test3s
done

