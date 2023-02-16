install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt
	playwright install firefox
	echo "Log in. Close the window. Kill the process."
	chatgpt install