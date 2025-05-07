
define _test1 {
    [bs]ipush 10 OR ldc 10
    newarray char
    astore[_ ][12]
}

define _test2 {
    [bs]ipush 15 OR ldc 15
    newarray int
    astore[_ ][123]
}

define _Dalloc {
    [bs]ipush 21 OR ldc 21
    newarray char
}

define _Ealloc {
    [bs]ipush 22 OR ldc 22
    newarray int
}

define _Falloc {
    [bs]ipush 23 OR ldc 23
    newarray float
}

define _345 {
    _Dalloc
    astore[_ 3]
    _Ealloc
    astore[_ 4]
    _Falloc
    astore[_ 5]
}

define _354 {
    _Dalloc
    astore[_ 3]
    _Ealloc
    astore[_ 5]
    _Falloc
    astore[_ 4]
}

define _435 {
    _Dalloc
    astore[_ 4]
    _Ealloc
    astore[_ 3]
    _Falloc
    astore[_ 5]
}

define _453 {
    _Dalloc
    astore[_ 4]
    _Ealloc
    astore[_ 5]
    _Falloc
    astore[_ 3]
}

define _534 {
    _Dalloc
    astore[_ 5]
    _Ealloc
    astore[_ 3]
    _Falloc
    astore[_ 4]
}

define _543 {
    _Dalloc
    astore[_ 5]
    _Ealloc
    astore[_ 4]
    _Falloc
    astore[_ 3]
}

within test1
    NAME char[10]
    MATCH _test1
done

within test2
    NAME int[15]
    MATCH _test2
done

within test3
    NAME three arrays
    MATCH _345 OR _543 OR _354 OR _435 OR _453 OR _534
done

