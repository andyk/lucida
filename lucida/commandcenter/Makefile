all: thrift

thrift:
	@if [ ! -d "lucidaservice" ]; then \
		thrift --gen py ../lucidaservice.thrift; \
		thrift --gen py ../lucidatypes.thrift; \
		cd gen-py; \
		mv * ..; \
		cd ..; \
		rmdir gen-py; \
		rm __init__.py; \
	fi

clean:
	rm -rf lucidaservice lucidatypes

start_server:
	source ${PWD}/../../tools/python_2_7_12/bin/activate && python app.py

# Development version of the CC which automatically reloads code changes and activates debug mode for flask
start_server_dev:
	source ${PWD}/../../tools/python_2_7_12/bin/activate && export FLASK_APP=app.py \
	&& export FLASK_DEBUG=1 && python -m flask run -p 3000 --host=0.0.0.0

docker:
	cp ../lucidaservice.thrift .; \
	cp ../lucidatypes.thrift .; \
	docker build -t lucida_cmd .; \
	rm lucidaservice.thrift; \
	rm lucidatypes.thrift;

.PHONY:	all venv thrift clean start_server docker
