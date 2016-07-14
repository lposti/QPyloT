#!/bin/bash
#
# this shell script syncs the lposti/fJnew fork
# Use: git remote -v     to view the repos
#

git fetch upstream
git checkout master
git merge upstream/master

echo
echo "Now commit changes and push!"
echo

git status
