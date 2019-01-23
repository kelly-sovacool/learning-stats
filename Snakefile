import os

input_files = [file for file in os.listdir() if file.endswith('.Rmd') or file.endswith('.yaml')]
site_cmd = 'bookdown::render_book("index.Rmd", output_dir="docs")'
pdf_cmd = 'bookdown::render_book("index.Rmd", "bookdown::pdf_book")'

rule all:
	input:	
		'docs/index.html',
		'docs/style.css',
		'docs/stats-ref.pdf'

rule compile_site:
	input:
		input_files
	output:
		'docs/index.html',
		'docs/style.css',
	shell:
		f"Rscript -e '{site_cmd}'"

rule compile_pdf:
	input:
		input_files
	output:
		'docs/stats-ref.pdf'
	shell:
		f"Rscript -e '{pdf_cmd}'; mv _book/_main.pdf docs/stats-ref.pdf ; "
		"rmdir _book"
