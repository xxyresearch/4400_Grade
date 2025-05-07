#!/bin/bash
# 

if [ "$#" -ne 1 ]; then 
  echo "Usage: bash GradeAll.sh <path-to-student-compiler>"
  exit 1
fi

COMPILER="$1"

print_section() {
  echo "------------------------------------------------------------"
  echo "--- $1 ($2 pts)"
  echo "------------------------------------------------------------"
}

print_subsection() {
  echo "--- $1 ($2 pts)"
}

pause() {
  read -p "Press Enter to continue..."
}

### ========== Common Output ==========
print_section "Common Output" 8

print_subsection ".class and .super lines" 2
./DotTest.sh "$COMPILER" INPUTS/minimal.c
pause

print_subsection "Special method <init>" 2
print_subsection "Java main() calls C main()" 2
print_subsection "Java main() exits with return code of C main()" 2
./AsmTest.sh "$COMPILER" INPUTS/minimal.c
pause

### ========== Code for User Functions ==========
print_section "Code for User Functions" 10

print_subsection "Correct parameters and return type" 3
print_subsection "Correct .method and .code blocks" 2
print_subsection "Reasonable stack limit" 3
print_subsection "Correct local count" 2
./DotTest.sh "$COMPILER" INPUTS/user*.c
pause

### ========== Function Calls and Returns ==========
print_section "Function Calls and Returns" 15

print_subsection "Parameter setup" 4
print_subsection "Correct calls to lib440 functions" 4
print_subsection "Correct calls to user-defined functions" 3
print_subsection "Void, char, int, float returns" 4
./AsmTest.sh "$COMPILER" INPUTS/fcall*.c
pause

### ========== Expressions ==========
print_section "Expressions" 10

print_section "Character, integer, and float literals" 3
./AsmTest.sh "$COMPILER" INPUTS/expr_literal*.c
pause

print_section "Reading local variables and parameters" 3
./AsmTest.sh "$COMPILER" INPUTS/expr_locals*.c
pause

print_section "Reading global variables" 4
./AsmTest.sh "$COMPILER" INPUTS/expr_g*.c
pause

### ========== Operators ==========
print_section "Operators" 15

print_section "Binary operators (+, -, *, /, %)" 10
./AsmTest.sh "$COMPILER" INPUTS/ops_binary*.c
pause

print_section "Unary operators and type conversions" 5
./AsmTest.sh "$COMPILER" INPUTS/ops_unary*.c
pause

### ========== Variable Writes ==========
print_section "Variable Writes" 15

print_section "Local variable initialization" 3
./AsmTest.sh "$COMPILER" INPUTS/init_lv*.c
pause

print_section "Assignment expressions (=)" 4
./AsmTest.sh "$COMPILER" INPUTS/assign_lv*.c
./AsmTest.sh "$COMPILER" INPUTS/assign_gv*.c
pause

print_section "Update assignments (+=, -=, *=, /=)" 4
./AsmTest.sh "$COMPILER" INPUTS/update_lv*.c
./AsmTest.sh "$COMPILER" INPUTS/update_gv*.c
pause

print_section "Pre and post increment/decrement" 4
./AsmTest.sh "$COMPILER" INPUTS/incdec_lv*.c
./AsmTest.sh "$COMPILER" INPUTS/incdec_gv*.c
pause

### ========== Arrays ==========
print_section "Arrays" 18

print_section "Local array allocation" 3
./AsmTest.sh "$COMPILER" INPUTS/AL_init*.c
pause

print_section "Reading array elements" 3
./AsmTest.sh "$COMPILER" INPUTS/AL_read*.c
./AsmTest.sh "$COMPILER" INPUTS/AG_read*.c
pause

print_section "Array element assignments (=)" 3
./AsmTest.sh "$COMPILER" INPUTS/AL_assign*.c
./AsmTest.sh "$COMPILER" INPUTS/AG_assign*.c
pause

print_section "Array element updates (+=, -=, *=, /=)" 3
./AsmTest.sh "$COMPILER" INPUTS/AL_update.c
./AsmTest.sh "$COMPILER" INPUTS/AG_update.c
pause

print_section "Passing arrays as parameters" 3
./AsmTest.sh "$COMPILER" INPUTS/AL_param.c
./AsmTest.sh "$COMPILER" INPUTS/AG_param.c
pause

print_section "Passing string literals as char[]" 3
./AsmTest.sh "$COMPILER" INPUTS/A_string_nc.c
./AsmTest.sh "$COMPILER" INPUTS/A_string_yc.c
./AsmTest.sh "$COMPILER" INPUTS/hewo.c
pause

### ========== Special Method <clinit> ==========
print_section "Special Method <clinit>" 10

print_section "<clinit>: Allocates global arrays" 4
./AsmTest.sh "$COMPILER" INPUTS/clinit_arr.c
pause

print_section "<clinit>: Initializes global variables" 4
./AsmTest.sh "$COMPILER" INPUTS/clinit_var.c
pause

print_section "<clinit>: Method present/omitted correctly" 2
./AsmTest.sh "$COMPILER" INPUTS/clinit_both.c
./AsmTest.sh "$COMPILER" INPUTS/clinit_omit*.c
pause

### ========== Advanced Features ==========
print_section "Advanced Features" 12

print_section "Smart stack management" 4
./AsmTest.sh "$COMPILER" INPUTS/smart.c
pause

print_section "Missing return statements" 4
./AsmTest.sh "$COMPILER" INPUTS/noreturn*.c
pause

print_section "Dead code elimination" 4
./AsmTest.sh "$COMPILER" INPUTS/dead*.c

echo "Grading script completed."
