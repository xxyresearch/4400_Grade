
======================================================================
For grading:
  (1) Run ParseTest.sh in this directory.
  (2) I recommend making a symbolic link to the student's compiler
      executable, from the testing directory, for testing convenience.
  (3) After testing each student, check for (and remove) stray files
      (.parser or .error) in the testing directory.


Arguments to ParseTest.sh:
  Argument 1 to the script: how to invoke the student's compiler,
  in double quotes.  Examples: "./mycc", "java mycc"

  Remaining arguments: input files to check, for example INPUTS/keywords*.c
  or INPUTS/*.c


The script will compare the student's compiler against
the instructor's bare bones, and extra credit, implementations.
For 'standard' features, these should match or be very close.
For 'extra credit' features, the outputs will likely be different,
so check if the student output matches the "bare bones" or "extra
credit" implementation.

For valid input files, the output should perfectly match the
instructor's.  For files that generate errors, the script compares
the first error message generated against the instructor's: line
numbers should match and the error descriptions should be consistent
but not necessarily identical (especially parsing errors).


Assigning points:
  * There will be a group of files to test for each feature
  * If all tests in the group fail, give 0 points
  * If all tests in the group pass, give full credit
  * Use something like a linear scale for in between,
    but give higher weight to the first passed tests.

    For example, for cases where there are 15 test
    files for 15 points, I would suggest a scale something like:
       0 pass:  0 points
       1 pass:  3 points
       2 pass:  5 points
       3 pass:  7 points
       4 pass:  9 points
       5 pass: 10 points
       7 pass: 11 points
       9 pass: 12 points
      11 pass: 13 points
      13 pass: 14 points
      15 pass: 15 points

    For cases where there are 4 test files for 3 points,
    I would suggest a scale something like:
       0 pass:  0   points
       1 pass:  1.5 points
       2 pass:  2.2 points
       3 pass:  2.7 points
       4 pass:  3   points


======================================================================

Grading suggestions.

5 pts   README.txt / README.md
  Instructions to build compiler and documentation are given.
  Python implementations may not need to be built at all.
  Should also indicate which features are implemented for part 2.

12 pts  developers.pdf
  How the implementation works.
  Check for added discussion about the parser.

 8 pts  Ease of building

 5 pts  Check that the compiler works in mode 0
        Just run it by hand

 5 pts  Check that the compiler works in mode 1
        Just run it by hand, but use a test file
        with no syntax errors, and check the
        generated .lexer file

Basic parser
------------------------------------------------------------
  5   global vars anywhere
      5 test files: global1.c ... global5.c

  5   function declarations / parameter lists
      5 test files: funcdec1.c ... funcdec5.c

  5   function local vars and body
      5 test files: funcbody1.c ... funcbody5.c

 10   for, while, do-while loops
      10 test files: loop1.c ... loopA.c

  5   if then else
      5 test files: ite1.c ... ite5.c

  5   break / continue / return / expression stmts
      5 test files: stmt1.c ... stmt5.c

 10   expressions with unary/binary/ternary operators
      10 test files: exprs1.c ... exprsA.c

  5   assignment operators, increment, decrement
      5 test files: assign1.c ... assign5.c

  5   identifiers and arrays
      5 test files: array1.c ... array5.c

  5   function calls and parameters
      5 test files: call1.c ... call5.c


Extra features
------------------------------------------------------------
  5   function prototypes
      5 test files: x_proto1.c ... x_proto5.c

  5   variable initialization
      5 test files: x_init1.c ... x_init5.c

  5   constants
      5 test files: x_const1.c ... x_const5.c

 10   user-defined structs
      10 test files: x_struct1.c ... x_structA.c

  5   struct member selection
      5 test files: x_member1.c ... x_member5.c


440 students: max points is 120 out of 100

