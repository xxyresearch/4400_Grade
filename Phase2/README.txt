Project Phase 2 Grading: Lexer
======================================================================
For grading:
  (1) Run LexTest.sh in this directory.
  (2) I recommend making a symbolic link to the student's compiler executable, from the testing directory, for testing convenience.
  Use the following command to create a symbolic link:
  ln -s compiler_path/mycc mycc
  (3) After testing each student, check for (and remove) stray files (.lexer or .error) in the testing directory.


Arguments to LexTest.sh:
  Argument 1 to the script: how to invoke the student's compiler,
  in double quotes.  Examples: "./mycc", "java mycc"

  Remaining arguments: input files to check, for example INPUTS/keywords*.c
  or INPUTS/*.c

For C/C++ compilers: ./LexTest.sh "./mycc" INPUTS/*.C
For JAVA compilers: ./LexTest.sh "java mycc" INPUTS/*.C 
For python: ./LexTest.sh "python3 mycc.py" INPUTS/*.C

The script will compare the student's compiler against the instructor's vompiler output, and extra credit, implementations.
There are two OUTPUT folders that contains instructors output.
OUTPUT_B has all the standard features.
OUTPUT_X has all the extra credit features.
For 'standard' features, these should match or be very close.
For 'extra credit' features, the outputs will likely be different,
so check if the student output matches the "bare bones" or "extra
credit" implementation.
Additionally, there is HEX folder that checks for hexadecimal number. This is a new feature implementation. Check that separately.

For valid input files, the output should perfectly match the instructor's.  For files that generate errors, the script compares
the first error message generated against the instructor's: line numbers should match and the error descriptions should be consistent
but not necessarily identical.

Some students doesn't implement a error message. But they actually a error empty stream. If that is the case, check some error files by hand. If the error messages are shown in the command line, give full marks. Otherwise, 5 marks from the total.


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
  Should also indicate which features are implemented for part 1.

15 pts  developers.pdf
  How the implementation works.
  There probably won't be any significant data structures,
  except possibly a buffer for lexemes and maybe a buffer
  for the input stream.
  Check for a high-level description of how tokens are recognized.

10 pts  Ease of building

 5 pts  Check that the compiler works in mode 0
        Just run it by hand

Basic lexer
------------------------------------------------------------
10 pts	Correct line numbers and output format.
        Run a few by hand (like, lineno1.c and lineno2.c)
        to check this, but if some valid and some invalid test
        files pass, then it is probably safe to assume that this
        is correct.  If the compiler seems to work but all test
        cases fail, it could be due to an error in the output format,
        or incorrect line numbers.
        If you (or the student) can correct the output so that
        tests pass, then do so and deduct points here.

14 pts	Keywords, types, identifiers.

        15 test files: keywords_01.c ... keywords_15.c

10 pts	Integer, real, string, character literals.

        15 test files: literals_01.c ... literals_14.c

5  pts	Comments.

        6 test files: comments_1.c ... comments_6.c

15 pts	Symbols.

        15 test files: symbols_01.c ... symbols_15.c

3  pts	Char literals with escapes

        4 test files: x_char1.c ... x_char4.c

3  pts	String literals with escapes

        4 test files:	x_str1.c ... x_str4.c

Extra features (tests 'pass' for output/errors matching "extra")
------------------------------------------------------------


3  pts	Real literals with exponents

        4 test files: x_real1.c ... x_real4.c


3  pts	Hexadecimal Numbers
        5 test files inside HEX folder: hex1.c, hex2.c ... hex5.c

3  pts	Errors for long lexemes

        4 test files: x_long1.c ... x_long4.c

3  pts	Error for invalid characters.

        3 test files: x_invalid1.c, x_invalid2.c, x_invalid3.c

3  pts  Output file removed on error

        Run by hand one of the test cases that the student
        compiler correctly catches an error.
        See if the compiler produced a partial .lexer file
        or removed it.  Give 3 points if it was removed
        (or never created).

10 pts  Include directives

        11 test files: x_inc01.c ... x_inc11.c


