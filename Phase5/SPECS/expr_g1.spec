
within print4
    NAME read a
    MATCH getstatic Field expr_g1 a C

    NAME read b
    MATCH getstatic Field expr_g1 b C

    NAME read c
    MATCH getstatic Field expr_g1 c C
done

define wra1 {
    72
    putstatic Field expr_g1 a C
}
define wra1dp {
    72
    dup
    putstatic Field expr_g1 a C
    pop
}

define wrb1 {
    101
    putstatic Field expr_g1 b C
}
define wrb1dp {
    101
    dup
    putstatic Field expr_g1 b C
    pop
}

define wrc1 {
    108
    putstatic Field expr_g1 c C
}
define wrc1dp {
    108
    dup
    putstatic Field expr_g1 c C
    pop
}

define wra2 {
    111
    putstatic Field expr_g1 a C
}
define wra2dp {
    111
    dup
    putstatic Field expr_g1 a C
    pop
}

define wrb2 {
    32
    putstatic Field expr_g1 b C
}
define wrb2dp {
    32
    dup
    putstatic Field expr_g1 b C
    pop
}

define wrc2 {
    87
    putstatic Field expr_g1 c C
}
define wrc2dp {
    87
    dup
    putstatic Field expr_g1 c C
    pop
}

within main
    NAME write a
    MATCH wra1 OR wra1dp

    NAME write a
    MATCH wra2 OR wra2dp

    NAME write b
    MATCH wrb1 OR wrb1dp

    NAME write b
    MATCH wrb2 OR wrb2dp

    NAME write c
    MATCH wrc1 OR wrc1dp

    NAME write c
    MATCH wrc2 OR wrc2dp
done
