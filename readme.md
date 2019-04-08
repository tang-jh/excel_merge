## Combine Excel files

### Purpose
A Python script to scan through a directory recursively for Excel files to be combined. The script assumes all the files to be of the same structure, and concatenates the data into a single Excel file.

### How to Use
Place the script `master_merge.py` in the root of the target folder and run it. Any files with the extension `.xlsx` will be detected and loaded to a dataframe, which is subsequently combined. 

A log file containing information of the import details will be generated after the script is run.

#### Note
* A windows `merge.bat` file is included to facilitate running of the script. Ensure that Python and the libraries are added to the environment path for it to work.
* A script `generate_data.py` is included to generate dummy data for test purpose