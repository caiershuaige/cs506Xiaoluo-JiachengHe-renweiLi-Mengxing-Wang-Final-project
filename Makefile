PYTHON ?= python

.PHONY: install test model notebooks clean

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest -q -p no:cacheprovider tests

model:
	$(PYTHON) -m jupyter nbconvert --to notebook --execute --inplace notebooks/05_modeling.ipynb

notebooks:
	$(PYTHON) -m jupyter nbconvert --to notebook --execute --inplace notebooks/01_data_collection.ipynb
	$(PYTHON) -m jupyter nbconvert --to notebook --execute --inplace notebooks/02_data_cleaning.ipynb
	$(PYTHON) -m jupyter nbconvert --to notebook --execute --inplace notebooks/03_eda_visualization.ipynb
	$(PYTHON) -m jupyter nbconvert --to notebook --execute --inplace notebooks/04_feature_engineering.ipynb
	$(PYTHON) -m jupyter nbconvert --to notebook --execute --inplace notebooks/05_modeling.ipynb

clean:
	$(PYTHON) -c "from pathlib import Path; [p.unlink() for p in Path('.').rglob('__pycache__/*') if p.is_file()]"
