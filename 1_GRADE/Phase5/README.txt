
There are 3 grading scripts this time.
They all are invoked using
      script "command to execute student compiler"  INPUTS/files_to_test*.c

Scripts will skip any input file that does not have a corresponding "key"
file for comparison, or for input files that ask to be skipped
(with comments like // NODOT ).


What the scripts do:

    AsmTest.sh

        Runs student compiler, then analyzes the output,
        comparing against a spec file (in the SPECS directory).
        The spec file defines a number of tests, each one
        involving finding (or not) a sequence of instructions
        in the compiler output for a given function.

        The script won't work if a compiler's output does not
        have a .method section for the requested function.

        When a test case fails, the compiler's output
        is displayed, along with one of the expected sequences.
        These should be examined, in case a student finds another
        correct sequence of instructions.  In this case, contact
        the instructor so that the spec can be updated.

        Check using the list of Java instructions at
        https://en.wikipedia.org/wiki/List_of_Java_bytecode_instructions

        For (rare) cases when the input file causes an error,
        this script will also compare against expected error messages.


    DotTest.sh

        Runs student compiler, and compares the student's output
        against the instructor's output, but only for lines that
        begin with ".", such as   .method, .code, etc.

        For (rare) cases when the input file causes an error,
        this script will also compare against expected error messages.


    RunTest.sh

        The preferred testing method, but also the hardest to pass.
        Runs student compiler, assembles student's .j file into
        a .class file, and runs it under the JVM on each set of inputs
        (or none, if none are given; these are .input files in INPUTS)
        and compares output against the program compiled with gcc.
        In other words, this method compares the actual "executable"
        produced by the student's compiler against the executable
        produced by gcc.

        Unfortunately, gcc and java tend to write floats differently,
        so some outputs with floats will not match, and will need
        to be inspected manually.

    RunTest_Sum.sh
        This is to test the functions with input files. Only run this 
        script for the following files
        fcall0.c
        fcall1.c
        fcall2.c
        fcall3.c
======================================================================

Suggested grading procedure


------------------------------------------------------------
Common output
------------------------------------------------------------

.class and .super lines (2 pts)

    Run DotTest.sh on INPUTS/minimal.c

    If result is "Different output", manually check that the
    .class and .super lines match.  Give credit accordingly.

    If the result is ".code stack/locals differences" or "Output matches",
    give full credit.

    On script failure, run manually and check the first few lines
    of the produced .j file for lines

      .class public minimal
      .super java/lang/Object


Special method <init>                             (2 pts)
Java main() calls C main()                        (2 pts)
Java main() exits with return code of C main()    (2 pts)

    Run AsmTest.sh on INPUTS/minimal.c

    init: MATCH         -> full credit for "Special method <init>"

    call C main: MATCH  -> full credit for "Java main() calls C main()"

    sequence: MATCH     -> full credit for "Java main() exits with..."


    If "call C main" fails then likely "sequence" will also fail;
    in that case:
        exit statis: MATCH -> full credit for "Java main() exits with..."


------------------------------------------------------------
Code for user functions
------------------------------------------------------------

Run DotTest.sh on INPUTS/user?.c


Correct parameters and return type (3 pts)

    MATCH: test passes
    Small stack differences: test passes.
    Otherwise make sure the student's .method lines match

Correct .method and .code blocks (2 pts)

    MATCH: test passes.
    Small stack differences: test passes.
    .code stack/locals differences: test passes.
    Otherwise make sure student output for a method is in order:
        .method ...
        .code ...
        .end code
        .end method

Reasonable stack limit (3 pts)

    MATCH: test passes
    Small stack differences: test passes
    Otherwise look at instructor stack size vs student
    stack size.  If the student stack size appears to be
    dynamic but different, give full or partial credit based
    on "how different".
    If the student stack size is fixed or extremely large,
    give no credit.

Correct local count (2 pts)

    MATCH: test passes
    Small stack differences: test passes.
    Otherwise compare student locals with instructor locals,
    they need to match perfectly.


------------------------------------------------------------
Function calls and returns
------------------------------------------------------------

Use RunTest_Sum.sh and/or AsmTest.sh on INPUTS/fcall?.c (4 files)
If all tests pass, give full credit for this section.

Parameter set up (4 pts)
    AsmTest.sh tests for this are named 'Parameter ...'

Correct calls to lib440 functions (4 pts)
    AsmTest.sh tests for this are named by the lib440 functions
    with parameter and return types
        putchar(I)I
        getchar()I
        putint(I)V
        getint()I
        putfloat(F)V
        getfloat()F
        putstring([C)V

Correct calls to user functions (3 points)
    AsmTest.sh tests for this will give the user-defined function
    with parameter and return types.  If it is not a lib440 function,
    then it must be a user-defined function.

Void, char, int, float returns (4 points)
    AsmTest.sh tests for these are named appropriately

------------------------------------------------------------
Expressions: literals, variables
------------------------------------------------------------

Use RunTest.sh and/or AsmTest.sh on the following files.
For this part, we only care about variable "reads".

    expr_literal1.c     character literals
    expr_literal2.c     integer literals
    expr_literal3.c     float literals

    expr_locals1.c      character param/local reads
    expr_locals2.c      integer param/local reads
    expr_locals3.c      float param/local reads

    expr_g1.c           character global reads/writes
    expr_g2.c           integer global reads/writes
    expr_g3.c           float global reads/writes

------------------------------------------------------------
Operators
------------------------------------------------------------

Use RunTest.sh and/or AsmTest.sh on the following files.

    ops_binary1.c       binary operations on integers
    ops_binary2.c       binary operations on floats
    ops_binary3.c       addition, subtraction on chars
    ops_binary4.c       precedence check: 2 binary ops on integers

    ops_unary1.c        unary operations (-) on integers
    ops_unary2.c        unary operations (-) on floats
    ops_unary3.c        int to char typecasts
    ops_unary4.c        float to int typecasts
    ops_unary5.c        int to float typecasts

------------------------------------------------------------
Global variable, local variable, and parameter writes
------------------------------------------------------------

Use RunTest.sh and/or AsmTest.sh on the following files.

    init_lv?.c          Local variable initialization,
                        e.g., int a = 3;   inside a function

    assign_lv?.c        Local variable assignments.
                        e.g., int a; a = 3; inside a function

    assign_gv?.c        Global variable assignments.

    update_lv?.c        Update assignments, for locals
    update_gv?.c        Update assignments, for globals

    incdec_lv?.c        Pre, post, increment, decrement for locals
    incdec_gv?.c        Pre, post, increment, decrement for globals

------------------------------------------------------------
Arrays
------------------------------------------------------------

Use AsmTest.sh on the following files.

    AL_init?.c          local array allocation
    AL_read?.c          reading local array elements in expressions
    AG_read?.c          reading global array elements in expressions

    AL_assign?.c        local array assignments with =
    AG_assign?.c        global array assignments with =

    AL_update.c         local array updates (+=, -=, *=, /=)
    AG_update.c         global array updates (+=, -=, *=, /=)

    AG_param.c          global arrays passed as parameters
    AL_param.c          local arrays passed and used as parameters

    A_string_nc.c
    A_string_yc.c
                        Two versions of the same test.
                        Passes string literals to user-defined
                        functions that take char[] parameters.

                        Only one of these will pass, depending on
                        if students implemented "const" or not.
                          "nc" is for "no const"
                          "yc" is for "yes const"

                        If students implemented const, then
                        A_string_nc will generate a type checking error.

                        If students did not implement const, then
                        A_string_yc may generate a parser error.

                        Just run both and see if one of them passes.


Use RunTest.sh or AsmTest.sh:

    hewo.c              Passing string literals as char[] parameters
                        to putstring()

------------------------------------------------------------
Special method <clinit>
------------------------------------------------------------

Use AsmTest.sh on the following files.

    clinit_arr.c        Check for global array initialization
                        in special method <clinit>

    clinit_var.c        Check for global variable initialization
                        (e.g., int thing = 45; )
                        in special method <clinit>

    clinit_both.c       Check for both global array, variable
                        initializations in special method <clinit>

    clinit_omit?.c      Check if special method <clinit> is missing
                        when it is not needed.  Obviously, if a
                        student never outputs this method, then
                        these tests will pass but students should
                        only receive points if there is some test
                        where student generate method <clinit>


------------------------------------------------------------
Smart stack management
------------------------------------------------------------

Use AsmTest.sh on

    smart.c             For each test method, there are (at least)
                        two tests.  The 'needed' test checks that
                        student code is correct when an expression
                        result is needed; the 'smart' test checks
                        for smart stack management when the result
                        is not needed.  Student code needs to pass
                        both tests to receive points for 'smart
                        stack management'.

------------------------------------------------------------
Missing return statements
------------------------------------------------------------

Use AsmTest.sh on the following files

    noreturn1.c         A void function without a return;
                        the test checks if the generated code
                        has a return statement.
                        Also checks that a float function
                        has an freturn and does not have a return.

    noreturn2.c         A character function without a return;
                        should give a compiler error

    noreturn3.c         An integer function without a return;
                        should give a compiler error


------------------------------------------------------------
Dead code elimination
------------------------------------------------------------

Use AsmTest.sh on the following files.

    dead?.c

The tests check that code after a return statement is omitted.


