
define pv0 {
  iload[_ ]0
  dummy
}
define pv1 {
  iload[_ ]1
  dummy
}
define pv2 {
  iload[_ ]2
  dummy
}
define pv3 {
  iload[_ ]3
  dummy
}
define pv4 {
  iload 4
  dummy
}
define pv5 {
  iload 5
  dummy
}

define f1seq {
  pv1
  pv0
}

define f2seq {
  pv0
  pv0
}

define f3seq {
  pv1
  pv2
  pv0
}

define f4seq {
  pv4
  pv3
  pv5
  pv2
  pv1
  pv0
}

within func1
  NAME  Param b
  MATCH  pv1

  NAME  Param a
  MATCH pv0

  NAME sequence
  MATCH f1seq
done

within func2
  NAME  Param c
  MATCH pv0

  NAME  sequence
  MATCH f2seq
done

within func3
  NAME  Param a
  MATCH pv0

  NAME  Local b
  MATCH pv2

  NAME  Param c
  MATCH pv1

  NAME  sequence
  MATCH f3seq
done

within func4
  NAME Param 1
  MATCH pv0

  NAME Param 2
  MATCH pv1

  NAME Param 3
  MATCH pv2

  NAME Param 4
  MATCH pv3

  NAME Param 5
  MATCH pv4

  NAME Local 1
  MATCH pv5

  NAME sequence
  MATCH f4seq
done

