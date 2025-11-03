#!/bin/bash

#This is a simple password generator

#1. prompt the user to enter the length of the password
echo "This is simple password generator"
echo "please enter the length of the password: "
read PASS_LENGTH

for p in $(seq 1);
do
	openssl rand -base64 48 | cut -c1-$PASS_LENGTH
done 
