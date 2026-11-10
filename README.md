# Gazoo Research: tagged-record filtering

An early exploratory Pandas notebook for filtering records stored in a long-form schema. The public example now uses fully synthetic rows so readers can run the filtering logic without a research-data upload.

## What it demonstrates

- Representing tagged records with columns such as `id`, `tag`, `field`, and `value`.
- Selecting records that match several conditions using a reusable `find_rows` helper.
- Preserving the DataFrame index when combining filters.

## Run

Open [`George.ipynb`](George.ipynb) in Jupyter or Google Colab and run the cells in order. Pandas is the only dependency; install it with `python -m pip install pandas` if needed. The example data is created inside the notebook.

## Project scope

This is a historical filtering example, not a complete clinical-data pipeline or a trained prediction model. The November 2026 portfolio cleanup replaced uploaded-record examples with invented data, cleared saved outputs, converted an unfinished sketch to explanatory text, and fixed filter-mask alignment for non-default indexes.

No source clinical records are distributed with this example. The original notebook's unused GazooResearchUtils dependency is not needed for the demonstrated Pandas operation.
