.PHONY:	all start_server clean

all:
	ngrok version 2>/dev/null | grep -Pe "ngrok version 2\." 2>&1 1>/dev/null || sudo ./deps/install_ngrok.sh
	phantomjs -v 2>/dev/null  | grep -Pe "^2\." 2>&1 1>/dev/null || sudo ./deps/install_phantomjs.sh
	which node || sudo ./deps/install_node.sh
	which npm || sudo ./deps/install_node.sh
	# Make sure this potentially non-root user has permission to access the npm cache
	# per https://stackoverflow.com/questions/50639690/on-npm-install-unhandled-rejection-error-eacces-permission-denied
	sudo chown -R $USER:$GROUP ~/.npm
	sudo chown -R $USER:$GROUP ~/.config
	npm install

start_server:
	bash start_interface.sh

clean:
	rm -rf node_modules
	rm -f config.tmp
	rm -f phantom.out
	rm -f credentials.js
	rm -f last_pushed_host
	rm -rf deps/downloads
	mv config.sh config.bak 2>/dev/null && echo "Backed up old config to config.bak" || :
