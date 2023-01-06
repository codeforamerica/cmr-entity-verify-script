import pandas as pd
import sys
from verification_functions import verify_positives

# Get the file names for the positive tests and results from the command line arguments
file_for_positives = sys.argv[1]
file_for_results = sys.argv[2]

expected_matches = pd.read_csv(file_for_positives, header=0)
results = pd.read_csv(file_for_results, header=0)

verify_positives(expected_matches, results)
