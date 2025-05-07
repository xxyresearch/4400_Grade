
Format of a spec file

# comment lines, ignored

define identifier {
  sequence
  of
  regexes
}

# use keyword OR for alternates
# can use SKIP at the end of an OR to make an item optional
# can use WAIT at the end of an OR to wait for an item
#
# e.g.
#     dup OR SKIP         (dup is optional)
#
#     iload_0 OR WAIT     (don't try matching again until iload_0)
#

define ident2 {
  instr OR defined sequence
}

within function-name
  # Optional: name a test
  NAME testname
  MATCH thing1 OR thing2

  # No name? will use "Test n"
  MATCH thing3

  # tests that pass if sequences are Missing:
  OMIT foo OR bar

done

within other-function
  # thingy
done


For labels and conditional gotos, use L%1 ... L%9
for distinct labels.

To print things to output, use (at the top level only)

note Here is a message for the grader


