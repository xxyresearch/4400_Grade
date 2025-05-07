
define intarr {
    bipush 44 OR sipush 44 OR ldc 44
    newarray int
    putstatic Field clinit_arr A [\[]I
}

define charr {
    sipush 1000 OR ldc 1000
    newarray char
    putstatic Field clinit_arr C [\[]C
}

define flarr {
    iconst_3 OR bipush 3 OR sipush 3 OR ldc 3
    newarray float
    putstatic Field clinit_arr x [\[]F
}

within <clinit>
  NAME A[44]
  MATCH intarr

  NAME C[1000]
  MATCH charr

  NAME x[3]
  MATCH flarr
done

