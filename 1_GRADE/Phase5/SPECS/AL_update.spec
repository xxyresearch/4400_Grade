
define _test1a {
    aload[ _]0
    dup
    iconst_0 OR [bs]ipush 0 OR ldc 0
    dup_x1
    caload
    [bs]ipush 48 OR ldc 48
    iadd
    i2c OR SKIP
    dup_x2 OR SKIP
    castore
}
define _test1b {
    [bs]ipush 48 OR ldc 48
    iconst_0 OR [bs]ipush 0 OR ldc 0
    aload[ _]0
    swap
    dup2_x1
    caload
    swap OR SKIP
    iadd
    i2c OR SKIP
    dup_x2 OR SKIP
    castore
}

within test1
    NAME A[0]+='0'
    MATCH _test1a OR _test1b
done

# --------------------------------------------------

define _test2a {
    aload[ _]1
    dup
    iload[ _]0
    dup_x1
    iaload
    [bs]ipush 49 OR ldc 49
    imul
    dup_x2 OR SKIP
    iastore
}
define _test2b {
    [bs]ipush 49 OR ldc 49
    iload[ _]0
    aload[ _]1
    swap
    dup2_x1
    iaload
    swap OR SKIP
    imul
    dup_x2 OR SKIP
    iastore
}

within test2
    NAME A[i]*=49
    MATCH _test2a OR _test2b
done

# --------------------------------------------------

define _test3a {
    aload[ _]1
    dup
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    dup_x1
    faload
    ldc [+]?3[.]0
    fdiv
    dup_x2 OR SKIP
    fastore
}
define _test3b {
    ldc [+]?3[.]0
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    isub
    aload[ _]1
    swap
    dup2_x1
    faload
    swap
    fdiv
    dup_x2 OR SKIP
    fastore
}

within test3
    NAME A[i-1]/=3.0
    MATCH _test3a OR _test3b
done

# --------------------------------------------------

define _savei1 {
    dup
    istore[ _]0
}
define _savei2 {
    istore[ _]0
    iload[ _]0
}

define _preinci_0 {
    iinc 0 1
    iload[ _]0
}
define _preinci_1 {
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    _savei1 OR _savei2
}
define _preinci_2 {
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap OR SKIP
    iadd
    _savei1 OR _savei2
}

define _test4a {
    aload[ _]1
    dup
    _preinci_0 OR _preinci_1 OR _preinci_2
    dup_x1
    caload
    [bs]ipush 51 OR ldc 51
    isub
    i2c OR SKIP
    dup_x2 OR SKIP
    castore
}
define _test4b {
    [bs]ipush 51 OR ldc 51
    _preinci_0 OR _preinci_1 OR _preinci_2
    aload[ _]1
    swap
    dup2_x1
    caload
    swap
    isub
    i2c OR SKIP
    dup_x2 OR SKIP
    castore
}

within test4
    NAME A[++i]-='3'
    MATCH _test4a OR _test4b
done

# --------------------------------------------------

define _test5a {
    aload[ _]1
    dup
    iconst_3 OR [bs]ipush 3 OR ldc 3
    dup_x1
    faload
    ldc [+]?7[.]7
    swap OR SKIP
    fadd
    dup_x2
    fastore
    freturn
}
define _test5b {
    ldc [+]?7[.]7
    iconst_3 OR [bs]ipush 3 OR ldc 3
    aload[ _]1
    swap
    dup2_x1
    caload
    swap OR SKIP
    fadd
    dup_x2
    fastore
    freturn
}

within test5
    NAME ret C[3]+=7.7
    MATCH _test5a OR _test5b
done

# --------------------------------------------------

define _postinci_0 {
    iload[ _]0
    iinc 0 1
}
define _postinci_1 {
    iload[ _]0
    iload[ _]0 OR dup
    iconst_1 OR [bs]ipush 1 OR ldc 1
    swap OR SKIP
    iadd
    istore[ _]0
}
define _postinci_2 {
    iload[ _]0
    iconst_1 OR [bs]ipush 1 OR ldc 1
    iload[ _]0
    swap OR SKIP
    iadd
    istore[ _]0
}

define _test6a {
    aload[ _]1
    dup
    _postinci_0 OR _postinci_1 OR _postinci_2
    dup_x1
    iaload
    [bs]ipush 11 OR ldc 11
    isub
    dup_x2
    iastore
    ireturn
}
define _test6b {
    [bs]ipush 11 OR ldc 11
    _postinci_0 OR _postinci_1 OR _postinci_2
    aload[ _]1
    swap
    dup2_x1
    iaload
    swap
    isub
    dup_x2
    iastore
    ireturn
}

within test6
    NAME ret B[i++]-=11
    MATCH _test6a OR _test6b
done


