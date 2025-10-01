.PHONY: all tests paper

all: tests paper

tests:
	python -m src.spectral_gap
	python -m src.bridge_test
	python -m src.enstrophy_decay
	python -m src.jhtdb_alignment

paper:
	cd paper && pdflatex ns_proof.tex && bibtex ns_proof && pdflatex ns_proof.tex && pdflatex ns_proof.tex
