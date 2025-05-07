
within print4
    NAME read i
    MATCH getstatic Field expr_g2 i I

    NAME read j
    MATCH getstatic Field expr_g2 j I

    NAME read k
    MATCH getstatic Field expr_g2 k I
done

define wra1 {
    72
    putstatic Field expr_g2 i I
}
define wra1dp {
    72
    dup
    putstatic Field expr_g2 i I
    pop
}

define wrb1 {
    101
    putstatic Field expr_g2 j I
}
define wrb1dp {
    101
    dup
    putstatic Field expr_g2 j I
    pop
}

define wrc1 {
    108
    putstatic Field expr_g2 k I
}
define wrc1dp {
    108
    dup
    putstatic Field expr_g2 k I
    pop
}

define wra2 {
    111
    putstatic Field expr_g2 i I
}
define wra2dp {
    111
    dup
    putstatic Field expr_g2 i I
    pop
}

define wrb2 {
    32
    putstatic Field expr_g2 j I
}
define wrb2dp {
    32
    dup
    putstatic Field expr_g2 j I
    pop
}

define wrc2 {
    87
    putstatic Field expr_g2 k I
}
define wrc2dp {
    87
    dup
    putstatic Field expr_g2 k I
    pop
}

within main
    NAME write i
    MATCH wra1 OR wra1dp

    NAME write i
    MATCH wra2 OR wra2dp

    NAME write j
    MATCH wrb1 OR wrb1dp

    NAME write j
    MATCH wrb2 OR wrb2dp

    NAME write k
    MATCH wrc1 OR wrc1dp

    NAME write k
    MATCH wrc2 OR wrc2dp
done
