clean:
	rm -rf *.pyc
run: test
test:
	python soundcloud_stream_builder.py
reqs:
	pip freeze > requirements.txt

