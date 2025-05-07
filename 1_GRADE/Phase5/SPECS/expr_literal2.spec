
within i_tiny
  NAME return special
  MATCH iconst_2 OR [bs]ipush 2 OR ldc 2
done

within i_byte
  NAME return byte
  MATCH [bs]ipush 55 OR ldc 55
done

within i_short
  NAME return short
  MATCH sipush 32105 OR ldc 32105
done

within i_int
  NAME return int
  MATCH ldc 87654321
done

within main
  NAME assign special
  MATCH iconst_1 OR [bs]ipush 1 OR ldc 1

  NAME assign byte
  MATCH [bs]ipush 54 OR ldc 54

  NAME assign short
  MATCH sipush 32104 OR ldc 32104

  NAME assign int
  MATCH ldc 87654320

  NAME param special
  MATCH iconst_0 OR [bs]ipush 0 OR ldc 0

  NAME param byte
  MATCH [bs]ipush 53 OR ldc 53

  NAME param short
  MATCH sipush 32103 OR ldc 32103

  NAME param int
  MATCH ldc 87654319
done

