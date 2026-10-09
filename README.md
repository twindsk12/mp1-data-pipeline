# MP1 Data Pipeline

This is a data processing pipeline that loads, cleans, validates and saves tabular data. It uses a YAML configuration file to specify what to do for validation and then for processing. The "src/data_loaders.py" module is respsonsible for loading input files, while the "src/data_validator.py" modules checks for required columns and validates numeric values. The "src/data_processor.py" module removes duplicates, handles missing values, and removes outliers. The "src/data_output.py" module creates the output directory and saves the cleaned data as a CSV file. The "src/utils.py" module is responsible for logging and checking that the input files exist and the  "pipeline.py" guides the entire process.

## Run Pipelie

## example code:
python pipeline.py -i fixtures/sample_data.csv -o output/cleaned.csv --config config/config.yaml -v

## example output: 
21:43:52 DEBUG    __main__ — Arguments parsed: input=fixtures/sample_data.csv, output=output/cleaned.csv, config=config/config.yaml
21:43:52 INFO     src.utils — Input file validated: fixtures/sample_data.csv
21:43:52 INFO     src.utils — Input file validated: config/config.yaml
21:43:52 INFO     src.data_loaders — Loaded CSV file: fixtures/sample_data.csv (100 rows)
21:43:52 INFO     src.data_loaders — Loaded YAML file: config/config.yaml
21:43:52 WARNING  src.data_validator — Removed 2 rows with invalid numeric values
21:43:52 DEBUG    src.data_validator — Validation: 100 -> 98 rows
21:43:52 INFO     __main__ — Validation complete: 100 -> 98 rows
21:43:52 DEBUG    src.data_processor — remove_duplicates: 98 → 96 rows
21:43:52 DEBUG    src.data_processor — handle_missing: 96 → 94 rows
21:43:52 DEBUG    src.data_processor — rating: lower=43.625, upper=106.625, removed=2
21:43:52 INFO     __main__ — Processing complete: 98 -> 92 rows
21:43:52 DEBUG    src.data_output — Saved 92 rows to output/cleaned.csv
21:43:52 INFO     __main__ — Saved cleaned data to output/cleaned.csv
