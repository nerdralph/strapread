
parse: parse.c strap.h strapd.c
	$(CC) parse.c -o $@

strapd.c: gendump.py
	./gendump.py > $@

strap.h: gendef.py
	./gendef.py > $@
