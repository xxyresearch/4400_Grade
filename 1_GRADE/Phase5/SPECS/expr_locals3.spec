
define pv0 {
  fload[_ ]0
  putfloat
}

define pv1 {
  fload[_ ]1
  putfloat
}

within print_row
  NAME Param a
  MATCH fload[_ ]0

  NAME Param b
  MATCH fload[_ ]1

  NAME Param a seq
  MATCH pv0

  NAME Param b seq
  MATCH pv1
done

define pvr1 {
  fload[_ ]0
  fload[_ ]1
  print_row
}

define pvr2 {
  fload[_ ]2
  fload[_ ]3
  print_row
}

within print2x2
  NAME Param a11
  MATCH fload[_ ]0

  NAME Param a12
  MATCH fload[_ ]1

  NAME Param a21
  MATCH fload[_ ]2

  NAME Param a22
  MATCH fload[_ ]3

  NAME print_row1
  MATCH pvr1

  NAME print_row2
  MATCH pvr2
done

define pr03 {
  fload[_ ]0
  fload[_ ]1
  fload[_ ]2
  fload[_ ]3
  print2x2
}


define pr4567 {
  fload 4
  fload 5
  fload 6
  fload 7
  print2x2
}
define pr4576 {
  fload 4
  fload 5
  fload 7
  fload 6
  print2x2
}
define pr4657 {
  fload 4
  fload 6
  fload 5
  fload 7
  print2x2
}
define pr4675 {
  fload 4
  fload 6
  fload 7
  fload 5
  print2x2
}
define pr4756 {
  fload 4
  fload 7
  fload 5
  fload 6
  print2x2
}
define pr4765 {
  fload 4
  fload 7
  fload 6
  fload 5
  print2x2
}

note The second mults test takes a while

within mults
  NAME (p11,p12,p21,p22)
  MATCH pr03

  NAME (q11,q12,q21,q22)
  MATCH pr4567 OR pr4576 OR pr4657 OR pr4675 OR pr4756 OR pr4765
done

