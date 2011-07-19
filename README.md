KyTea wrapper for python
==========================
2011/07/20 chezou

Mykytea-python is a python wrapper module for KyTea, a general text analysis toolkit.

KyTea is developed by KyTea Development Team

Detailed information of KyTea can be found at
http://www.phontron.com/kytea

Install Dependencies
--------------------
You need install KyTea and SWIG before build.

To build Mykytea-python, run
--------------------

   % make

or

   % swig -Wall -c++ -python -shadow -c++ mykytea.i
   % python setup.py build
   % sudo python setup.py install

How to use?
--------------------

  See 'mykytea_test.py' as a sample program.

License
--------------------
MIT License