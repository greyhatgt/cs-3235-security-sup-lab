CC=gcc
CFLAGS=-fno-stack-protector -no-pie -g -m32

all: pwnme.c
	$(CC) $(CFLAGS) -o pwnme pwnme.c
