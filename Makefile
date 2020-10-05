init:
	chmod +x bin/*.sh
	./bin/dev.sh init

shell:
	./bin/dev.sh shell

python:
	./bin/dev.sh run python

update:
	./bin/dev.sh update

test:
	./bin/dev.sh test

run:
	./bin/dev.sh run python main.py