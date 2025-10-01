.PHONY: all tests paper

all: tests 

tests:
	python -m src.spectral_gap
	python -m src.bridge_test
	python -m src.enstrophy_decay
	python -m src.jhtdb_alignment
	python -m src.utils

paper:
	cd paper && pdflatex ns_proof.tex && bibtex ns_proof && pdflatex ns_proof.tex && pdflatex ns_proof.tex
