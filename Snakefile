rule all:
	input:	
		'docs/index.html',
		'docs/style.css',
		'_book/stats-ref.pdf'

rule compile_site:
	output:
		'docs/index.html',
		'docs/style.css',
	shell:
		"Rscript -e '{}'".format('bookdown::render_book("index.rmd", output_dir="docs")')

rule compile_pdf:
	output:
		'_book/stats-ref.pdf'
	shell:
		"Rscript -e '{}'; mv _book/_main.pdf _book/stats-ref.pdf ".format('bookdown::render_book("index.Rmd", "bookdown::pdf_book")')
