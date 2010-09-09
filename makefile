.PHONY: install all clean reallyclean

PREFIX ?= /usr

XSDCXX ?= xsdcxx

PYXBGEN ?= pyxbgen

all: ode-schema.hxx ode-schema.cxx ode-schema.py

ode-schema.py: ode-schema.xsd
	${PYXBGEN} -u ode-schema.xsd -m ode-schema

ode-schema.hxx ode-schema.cxx:
	${XSDCXX} cxx-tree --generate-polymorphic --generate-serialization ode-schema.xsd

install:
	echo not implemented yet

clean:
	rm -f ode-schema.hxx ode-schema.cxx ode-schema.py

reallyclean: clean
	rm -f *~



