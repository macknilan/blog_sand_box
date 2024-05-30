#!/usr/bin/env bash

countdown(){

  # DECLARE A DESCRIPTION FOR THE FUNCTION.
  declare desc="A simple countdown."

  # DEFINE A LOCAL VARIABLE 'seconds' AND ASSIGN THE FIRST ARGUMENT PASSED TO THE FUNCTION TO IT.
  local seconds="${1}"

  # DEFINE A LOCAL VARIABLE 'd' AND ASSIGN THE CURRENT UNIX TIMESTAMP PLUS THE 'seconds' VARIABLE TO IT.
  local d=$(($(date +%s) + "${seconds}"))

  # START A WHILE LOOP THAT CONTINUES AS LONG AS 'd' IS GREATER OR EQUAL TO THE CURRENT UNIX TIMESTAMP.
  while [ "$d" -ge `date +%s` ]; do

    # PRINT THE REMAINING TIME IN THE FORMAT HH:MM:SS, WITHOUT A NEWLINE AT THE END.
    echo -ne "$(date -u --date @$(($d - `date +%s`)) +%H:%M:%S)\r";

    # PAUSE EXECUTION FOR 0.1 SECONDS.
    sleep 0.1

  done
}
