
define set_T {
    bipush 116 OR sipush 116 OR ldc 116
    putstatic Field clinit_var T C
}

define set_count {
    bipush 37 OR sipush 37 OR ldc 37
    putstatic Field clinit_var count I
}

define set_pi {
    ldc [+]?3.140*
    putstatic Field clinit_var pi F
}

within <clinit>
    NAME  T='t'
    MATCH set_T

    NAME  count=37
    MATCH set_count

    NAME  pi=3.14
    MATCH set_pi
done
