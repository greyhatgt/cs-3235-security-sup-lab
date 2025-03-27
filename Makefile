CC=gcc
CFLAGS=-fno-stack-protector -no-pie -m32

all: vuln.c vuln
	$(CC) $(CFLAGS) -o vuln vuln.c
