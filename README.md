 #verify_positives
This script verifies that expected matches match the expected results. It takes two input CSV files, one containing the expected matches and another containing the test results. It returns the number of successful matches, the number of failed matches, and a list of error messages.

##Requirements
Python 3
pandas
##Usage
To run the script, use the following command:


<code> python main.py positives.csv results.csv </code>
or
<code> python3 main.py positives.csv results.csv </code>
The script will print the number of successful matches, the number of failed matches, and a list of error messages.

##Input Files
The expected matches file should be a CSV file with the following columns:

<code>test_id</code>: a unique identifier for the expected match
<code>id_a</code>: the first ID in the expected match
<code>id_b</code>: the second ID in the expected match
<code>criteria</code>: a description of the criteria for the expected match
The results file should be a CSV file with the following columns:

party_id: the ID of the party
person_id: the ID of the person associated with the party
Output
The script will print the following output to the console:

The number of successful matches
The number of failed matches
A list of error messages for failed matches, including the test ID and criteria for each failed match

##Example

<code>python verify_positives.py expected_matches.csv results.csv</code>
The output might look like this:

<code>
Number of successful matches: 3
Number of failed matches: 2
Failed matches:
- Test 1 failed criteria: criteria1
</code>
