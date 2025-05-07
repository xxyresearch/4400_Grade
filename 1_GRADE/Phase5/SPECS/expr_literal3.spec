
within f_special
    NAME return special
    MATCH fconst_1 OR ldc [+]?1[.]0
done

within f_other
    NAME return other
    MATCH ldc [+]?1[.]414
done

within main
    NAME assign special
    MATCH fconst_0 OR ldc [+]?0[.]0

    NAME assign other
    MATCH ldc [+]?1[.]732

    NAME param special
    MATCH fconst_2 OR ldc [+]?2[.]0

    NAME param other
    MATCH ldc [+]?2[.]236
done

