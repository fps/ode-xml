.PHONY: install all clean reallyclean

PREFIX ?= /usr

XSDCXX ?= xsdcxx

PYXBGEN ?= pyxbgen

all: ode_schema.hxx ode_schema.cxx ode_schema.py

ode_schema.py: ode_schema.xsd
	${PYXBGEN} -u ode_schema.xsd -m ode_schema

ode_schema.hxx ode_schema.cxx:
	${XSDCXX} cxx-tree --generate-polymorphic --generate-serialization ode_schema.xsd

install:
	echo not implemented yet

clean:
	rm -f ode_schema.hxx ode_schema.cxx ode_schema.py

reallyclean: clean
	rm -f *~



