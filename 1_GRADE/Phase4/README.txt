
======================================================================
For grading:
  (1) Run TypesTest.sh in this directory.
  (2) I recommend making a symbolic link to the student's compiler
      executable, from the testing directory, for testing convenience.
  (3) After testing each student, check for (and remove) stray files
      (.parser or .error) in the testing directory.


Arguments to TypesTest.sh:
  Argument 1 to the script: how to invoke the student's compiler,
  in double quotes.  Examples: "./mycc", "java mycc"

  Remaining arguments: input files to check, for example INPUTS/keywords*.c
  or INPUTS/*.c


The script will compare the student's compiler against
the instructor's bare bones, and extra credit, implementations.
For 'standard' features, these should match or be very close.
For 'extra credit' features, the bare bones and extra credit
outputs are often different, so check which one the student matches.

For valid input files, student output should perfectly match the
instructor's.  For files that generate errors, the script compares
the first error message generated against the instructor's: line
numbers should match and the error descriptions should be consistent
but not necessarily identical (especially parsing errors).  The student
type checking error messages should be descriptive enough to tell that
they are catching the same error as the instructor.


Assigning points:
  * There will be a group of files to test for each feature
  * If all tests in the group fail, give 0 points
  * If all tests in the group pass, give full credit
  * Use a sort of linear scale, but with more weight to the first
    passed tests, for compilers that do not pass all tests.
  * Some suggested scales:

      4 test cases:   |  5 test cases:   |  6 test cases:
     -----------------+------------------+------------------
      0 passed:   0%  |  0 passed:   0%  |  0 passed:   0%
      1 passed:  40%  |  1 passed:  40%  |  1 passed:  40%
      2 passed:  70%  |  2 passed:  64%  |  2 passed:  60%
      3 passed:  90%  |  3 passed:  82%  |  3 passed:  76%
      4 passed: 100%  |  4 passed:  94%  |  4 passed:  88%
                      |  5 passed: 100%  |  5 passed:  96%
                                         |  6 passed: 100%

      9 test cases:   | 10 test cases:
     -----------------+-----------------
      0 passed:   0%  |  0 passed:   0%
      1 passed:  40%  |  1 passed:  40%
      2 passed:  50%  |  2 passed:  48%
      3 passed:  60%  |  3 passed:  56%
      4 passed:  70%  |  4 passed:  64%
      5 passed:  80%  |  5 passed:  72%
      6 passed:  88%  |  6 passed:  80%
      7 passed:  94%  |  7 passed:  88%
      8 passed:  98%  |  8 passed:  94%
      9 passed: 100%  |  9 passed:  98%
                      | 10 passed: 100%

======================================================================

Grading suggestions.

3 pts   README.txt / README.md
  Instructions to build compiler and documentation are given.
  Python implementations may not need to be built at all.
  Should also indicate which features are implemented for part 3.

12 pts  developers.pdf
  How the implementation works.
  Check for added discussion about the symbol table, and type information.

 6 pts  Ease of building

 8 pts  Check that the compiler works in modes 0, 1, and 2
        Just run it by hand, but use a test file
        with no errors.


Type checking (standard features)
------------------------------------------------------------
  4   Literals
      literals?.c (4 files)

 10   Identifiers
      idents?.c (9 files)

 10   Function calls (9 files)
      fcall?.c

  4   Function returns
      return?.c (4 files)

  4   Unary operators
      unary?.c (4 files)

  4   Casts
      cast?.c (4 files)

  6   Binary operators: arithmetic
      arith?.c (6 files)

  6   Binary operators: comparison and logic
      logic?.c (6 files)

  6   Assignment and update operators
      assign?.c (6 files)

  4   Increment and decrement
      inc?.c (4 files)

  4   Array indexing
      array?.c (4 files)

  4   Ternary operator
      ternary?.c (4 files)


Extra features (should match "extra output" or "extra error")
------------------------------------------------------------

  5   Prototype checking
      x_proto?.c  (5 files)

  5   Widening
      x_widen?.c  (10 files)

  5   Initializations
      x_init?.c  (5 files)

  5   Constants
      x_const?.c (5 files)

  5   User-defined structs
      x_struct?.c (5 files)

  5   Struct member selection
      x_member?.c (5 files)

  5   const with struct
      x_struct_const?.c (5 files)


Max points for students in 440 is 120 points
