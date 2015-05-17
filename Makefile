all:
	swig -Wall -c++ -python -shadow -c++ -I/usr/local/include lib/kytea/mykytea.i
	python setup.py build_ext --inplace

install:
	python setup.py install

test:
	python ./lib/test/mykytea_test.py

.PHONY: clean
clean:
	find . -name "*.pyc" -delete
	rm -rf build
	rm -rf dist
