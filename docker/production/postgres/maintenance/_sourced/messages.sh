#!/usr/bin/env bash

message_newline(){
  echo
}

# It takes any number of arguments and prints them prefixed with "DEBUG: ".
# The '-e' option of 'echo' enables interpretation of backslash escapes.
# The '${@}' is a special shell variable which holds all the arguments provided to the function.
message_debug(){
  echo -e "DEBUG: ${@}"
}

# It takes any number of arguments and prints them in bold.
# The '-e' option of 'echo' enables interpretation of backslash escapes.
# The '${@}' is a special shell variable which holds all the arguments provided to the function.
message_welcome(){
  echo -e "\e[1m${@}\e[0m"
}

# It takes any number of arguments and prints them prefixed with "WARNING: " in yellow color.
message_warning(){
  echo -e "\e[33mWARNING\e[0m: ${@}"
}

# It takes any number of arguments and prints them prefixed with "ERROR: " in red color.
message_error(){
  echo -e "\e[31mERROR\e[0m: ${@}"
}

# It takes any number of arguments and prints them prefixed with "INFO: " in white color.
message_info(){
  echo -e "\e[37mINFO\e[0m: ${@}"
}

# It takes any number of arguments and prints them prefixed with "SUGGESTION: " in yellow color.
message_suggestion(){
  echo -e "\e[33mSUGGESTION\e[0m: ${@}"
}

# It takes any number of arguments and prints them prefixed with "SUCCESS: " in green color.
message_success(){
  echo -e "\e[32mSUCCESS\e[0m: ${@}"
}