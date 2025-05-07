
define set_T {
    bipush 116 OR sipush 116 OR ldc 116
    putstatic Field clinit_both T C
}

define carr {
    sipush 1000 OR ldc 1000
    newarray char
    putstatic Field clinit_both C [\[]C
}

define set_count {
    bipush 37 OR sipush 37 OR ldc 37
    putstatic Field clinit_both count I
}

define iarr {
    bipush 44 OR sipush 44 OR ldc 44
    newarray int
    putstatic Field clinit_both A [\[]I
}

define set_pi {
    ldc [+]?3.140*
    putstatic Field clinit_both pi F
}

define farr {
    iconst_3 OR bipush 3 OR sipush 3 OR ldc 3
    newarray float
    putstatic Field clinit_both x [\[]F
}

within <clinit>
  NAME  T='t'
  MATCH set_T

  NAME  C[1000]
  MATCH carr

  NAME  count=37
  MATCH set_count

  NAME  A[44]
  MATCH iarr

  NAME  pi=3.14
  MATCH set_pi

  NAME  x[3]
  MATCH farr
done

