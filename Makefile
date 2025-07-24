.PHONY: test pytest coverage htmlcov lint format clean
pytest:
	@echo "Running pytest..."
	pytest

# Run mypy analysis
mypy:
	@echo "Running mypy static analysis..."
	mypy app/
# Run tests with coverage and show missing lines
coverage:
	@echo "Running pytest with coverage..."
	pytest --cov=app/ --cov-report=term-missing app/

# Generate HTML coverage report
htmlcov:
	@echo "Generating HTML coverage report..."
	pytest --cov=app/ --cov-report=html app/
	@echo "Report saved in htmlcov/index.html"

# Lint using flake8
lint:
	@echo "Linting code with flake8..."
	flake8 app/

# Auto-format using black
format:
	@echo "Formatting code with black..."
	black app/
# Clean up pycache and coverage
clean:
	@echo "Cleaning workspace..."
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	rm -rf htmlcov .coverage
