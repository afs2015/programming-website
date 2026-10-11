PY = uv run
PELICAN = $(PY) pelican
PELICANOPTS =

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py

.PHONY: help html clean regenerate serve devserver publish

help:
	@echo 'Usage:'
	@echo '   make html           (re)generate the web site'
	@echo '   make clean          remove the generated files'
	@echo '   make regenerate     regenerate files upon modification'
	@echo '   make serve          serve site at http://localhost:8000'
	@echo '   make devserver      serve and regenerate together'
	@echo '   make publish        generate using production settings'

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	rm -rf $(OUTPUTDIR)/*

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)
