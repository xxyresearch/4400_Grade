#!/bin/bash

TIMEOUT="30"
SCRIPT=$0
MODE="-4"
EXT="j"
ERR="error"
GCC="gcc"
KPATH="$HOME/Krakatau/target/release"
ASSEMBLE="$KPATH/krak2 asm"

color_echo() {
    case $1 in
        red) echo -e "\033[1;31m$2\033[0m" ;;
        green) echo -e "\033[1;32m$2\033[0m" ;;
        yellow) echo -e "\033[1;33m$2\033[0m" ;;
        cyan) echo -e "\033[1;36m$2\033[0m" ;;
        *) echo "$2" ;;
    esac
}

# Compile a test case
run_test() {
    local infile="$1"
    local base=$(basename "$infile" .c)

    if [ -f OUTPUTS_B/$base.$ERR ]; then
        color_echo yellow "$base.c: Skipped due to previous errors"
        return
    fi

    echo "Compiling $base.c"
    ./mycc $MODE "$infile" > /dev/null 2> "$base.$ERR"

    if [ -s "$base.$ERR" ]; then
        color_echo red "$base.c: Compile error"
        cat "$base.$ERR"
        return
    fi

    if ! $ASSEMBLE "$base.$EXT" --out "$base.class" > /dev/null 2> "$base.log"; then
        color_echo red "$base.c: Assembly error"
        cat "$base.log"
        return
    fi

    color_echo green "$base.c: Assembly success"

    for test_input in INPUTS/$base.input*; do
        if [ -f "$test_input" ]; then
            echo "Running: java $base < $test_input"
            if java "$base" < "$test_input" > "$base.out" 2> "$base.err"; then
                expected_output="GCC/$(basename "$test_input" | sed 's/input/output/')"
                if diff -q "$base.out" "$expected_output" > /dev/null; then
                    color_echo green "Output matches"
                else
                    color_echo red "Output differs from GCC"
                    echo "Expected:"; cat "$expected_output"
                    echo "Got:"; cat "$base.out"
                fi
            else
                color_echo red "Java error while running $base"
                cat "$base.err"
            fi
        fi
    done
    echo
}

if [ $# -lt 2 ]; then
    echo "Usage: $0 ./mycc INPUTS/*.c"
    exit 1
fi

EXE="$1"
shift

for src in "$@"; do
    run_test "$src"
    echo "--------------------------------------------------"
done

