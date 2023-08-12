run: clean up
	clean:
		@find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
	up:
		@docker-compose -f "local.yml" up