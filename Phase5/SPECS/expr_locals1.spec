
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

define f1seq {
  pv0
  pv1
  pv2
  pv3
  pv4
}

define f1alt {
  pv0
  pv1
  pv2
  pv4
  pv3
}

define f2seq {
  pv3
  pv2
  pv1
  pv0
  pv4
}

within func1
  NAME var 0
  MATCH pv0

  NAME var 1
  MATCH pv1

  NAME var 2
  MATCH pv2

  NAME var 3
  MATCH pv3

  NAME var 4
  MATCH pv4

  NAME sequence
  MATCH f1alt OR f1seq
done

within func2
  NAME var 0
  MATCH pv0

  NAME var 1
  MATCH pv1

  NAME var 2
  MATCH pv2

  NAME var 3
  MATCH pv3

  NAME var 4
  MATCH pv4

  NAME sequence
  MATCH f2seq
done

