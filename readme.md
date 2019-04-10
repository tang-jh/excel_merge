## Combine Excel files

### Purpose
A Python script to scan through a directory recursively for Excel files to be combined. The script assumes all the files to be of the same structure, and concatenates the data into a single Excel file.

### Use Case
The example given here is the evaluation of a collection of items, which can be products/personnels, distributed to a collection of assessors. Each assessor will submit an Excel scoresheet for their allocated items.

Each item is assigned three assessors and assessed on three criteria. The script `master_merge.py` is used to concatenate data from every assessor's Excel scoresheet into a single one.

It is possible to include codes to transform and aggregate the data further with `Python` via `pandas` dataframes.

### How to Use
* Place the script `master_merge.py` in the root of the target folder and run it.
	* Any files with the extension `.xlsx` will be detected and loaded to a dataframe, which is subsequently combined. 
	* The script scans for files at the same level of its location and any child folders.
	
* You can run `generate_data.py` to create a demo folder structure for testing purpose.

* Once run, a log file containing information of the import details will be generated and a `master_table.xlsx` will be created

#### Note
* A windows `merge.bat` file is included to facilitate running of the script. Ensure that `Python` and the libraries are added to the environment path for it to work.
* This method bypasses the locked single-instance of MS Office applications, allowing for data to be grabbed even when files are opened