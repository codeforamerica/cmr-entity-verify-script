 # verify_positives
This script is written to test our entity resolution script. This script verifies that expected matches match the expected results. It takes two input CSV files, one containing the expected matches and another containing the test results. It returns the number of successful matches, the number of failed matches, and a list of error messages.

## Requirements
Python 3
<p>pandas</p>
## Usage
To run the script, use the following command:

<pre>
<code> python3 main.py positives.csv results.csv </code>
</pre>
The script will print the number of successful matches, the number of failed matches, and a list of error messages.

## Input Files
The expected matches file should be a CSV file with the following columns:

<code>test_id</code>: a unique identifier for the expected match
<code>id_a</code>: the first ID in the expected match
<code>id_b</code>: the second ID in the expected match
<code>criteria</code>: a description of the criteria for the expected match
The results file should be a CSV file with the following columns:

<p><code>party_id</code>: the ID of the party</p>
<p><code>person_id</code>: the ID of the person associated with the party</p>
<p>Output</p>
The script will print the following output to the console:

The number of successful matches
The number of failed matches
A list of error messages for failed matches, including the test ID and criteria for each failed match

## Pytest Example

<code>pytest</code>
The output might look like this:
## Usage
To run the script, use the following command:
<code>pytest</code>
<pre><code>
Number of successful matches: 1
Number of failed matches: 2
Failed matches:
- test_2, criteria: address
- test_3, criteria: phone
</code>
</pre>
