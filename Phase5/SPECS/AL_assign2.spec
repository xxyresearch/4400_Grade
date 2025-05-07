
define _test1 {
    aload[ _]1
    iload[ _]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    getstatic [Ff]ield .* c C
    dup_x2 OR SKIP
    castore
}

define _test1s {
    iload[ _]0
    iconst_3 OR [bs]ipush 3 OR ldc 3
    isub
    aload[ _]1
    swap
    getstatic [Ff]ield .* c C
    dup_x2 OR SKIP
    castore
}

within test1
    NAME A[i-3]=c
    MATCH _test1 OR _test1s
done

# ----------------------------------------------------

define _test2 {
    aload[ _]3
    aload[ _]3
    iload[ _]2
    iaload
    iload[ _]1
    dup_x2 OR SKIP
    iastore
}

define _test2s {
    iload[ _]2
    aload[ _]3
    swap
    iaload
    aload[ _]3
    swap
    iload[ _]1
    dup_x2 OR SKIP
    iastore
}

within test2
    NAME A[A[j]]=b
    MATCH _test2 OR _test2s
done

# ----------------------------------------------------

define _test3 {
    aload[ _]0
    invokestatic .* the_index
    ldc [+]?3[.]14
    dup_x2
    fastore
}

define _test3s {
    invokestatic .* the_index
    aload[ _]0
    swap
    ldc [+]?3[.]14
    dup_x2
    fastore
}

within test3
    NAME ret F[func()]=3.14
    MATCH _test3 OR _test3s
done

