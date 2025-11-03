#!/bin/bash
 
 #enhancements
 # colors for output

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

#This is a simple password generator

#1. prompt the user to enter the length of the password
echo -e "${GREEN}This is simple password generator${NC}"
echo -e "${BLUE}please enter the length of the password: "
read PASS_LENGTH

for p in $(seq 1 5);
do
	openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done 
