# Makefile for LaTeX document compilation

# Variables
TEX = pdflatex
BIB = bibtex
DOC = abstract_topic_modeling
LATEX_DIR = doc/paper

# Default target
all:
	cd $(LATEX_DIR) && $(TEX) $(DOC).tex
	cd $(LATEX_DIR) && $(TEX) $(DOC).tex

# Clean auxiliary files
clean:
	cd $(LATEX_DIR) && rm -f *.aux *.log *.bbl *.blg *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.synctex.gz

# Clean everything including PDF
distclean: clean
	cd $(LATEX_DIR) && rm -f $(DOC).pdf

# View the PDF
view:
	open $(LATEX_DIR)/$(DOC).pdf &

.PHONY: all clean distclean view
