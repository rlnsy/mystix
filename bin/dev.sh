#!/bin/bash

export PIPENV_VENV_IN_PROJECT=1
export PIPENV_IGNORE_VIRTUALENVS=1

_routine_=$1

_load_hooks_ () {
  printf "\nCopying git scripts...\n"
  chmod +x .githooks/pre-commit
  cp .githooks/pre-commit .git/hooks/pre-commit
  printf "Done.\n"
}

_run_init_ () {
  printf "\n\033[0;34mWelcome to the project!\033[0m\n"
  printf "This script will help set up the development environment. "
  read -r -p "Continue? [Y/n] " confirm
  if [[ ! $confirm =~ ^[Yy]$ ]]; then
    printf "Bye.\n"
    exit 0
	fi
	printf "\nFound the following git info:\n"
  git config -l | grep user.name
  git config -l | grep user.email
  read -r -p "Does this match your CWL? [Y/n] " confirm
  if [[ ! $confirm =~ ^[Yy]$ ]]; then
    read -r -p "Enter your username: " gitname
    read -r -p "Enter your email: " gitemail
    git config user.name "$gitname"
    git config user.email "$gitemail"
	else
	  printf "\nGreat!\n"
	fi
  printf "\nAttempting to setup Python dependencies\n\n"
  pipenv --version
  if [ $? != 0 ]; then
    printf "\n\033[0;31mError:\033[0m It looks like you don't have \033[1; 32mPipenv\033[0m installed.
It's a great tool for python dependency management and required for this setup. You
should install it and try again!\n"
    exit 1
  fi
  pipenv install
  _load_hooks_
  printf "\nReady to go! For more commands please consult the Makefile.\n"
  exit 0
}

_run_shell_ () {
  pipenv shell
  exit 0
}

_run_ () {
  pipenv run "$@"
  exit 0
}

_run_update_ () {
  pipenv install
  _load_hooks_
  exit 0
}

_run_add_dep_ () {
  # FIXME
  pipenv install "$1"
}

_run_tests_ () {
  pipenv run python -m unittest discover -s tests -p "test_*.py"
}

if [ "$_routine_" = "init" ]; then
  _run_init_
elif [ "$_routine_" = "run" ]; then
  _run_ "${@:2}"
elif [ "$_routine_" = "shell" ]; then
  _run_shell_
elif [ "$_routine_" = "update" ]; then
  _run_update_
elif [ "$_routine_" = "add-dependency" ]; then
  _run_add_dep_ "$2"
elif [ "$_routine_" = "test" ]; then
  _run_tests_
else
  echo "Unrecognized command: '$_routine_'"
  exit 1
fi

