import pandas as pd
import sys

# Get the file names for the positive tests and results from the command line arguments
file_for_positives = sys.argv[1]
file_for_results = sys.argv[2]

expected_matches = pd.read_csv(file_for_positives, header=0)
results = pd.read_csv(file_for_results, header=0)


def verify_positives(expected_matches, results):
    """
    Verify that the expected matches match the expected results.

    Parameters:
        expected_matches (pandas.DataFrame): A DataFrame containing the expected matches.
        results (pandas.DataFrame): A DataFrame containing the test results.

    Returns:
        tuple: A tuple containing the number of successful matches, the number of failed
            matches, and a list of error messages.
    """

    # Initialize variables to store the results
    error_array = []
    num_successful_matches = 0
    num_failed_matches = 0
    # Create a dictionary mapping IDs to rows in the results dataframe
    results_by_id = {result["party_id"]: result for _, result in results.iterrows()}
    # Iterate over the positive tests
    for _, positive in expected_matches.iterrows():
        # Look up the rows for the IDs in the positive test
        positive_a = results_by_id.get(positive["id_a"])
        positive_b = results_by_id.get(positive["id_b"])
        # If either ID is not present in the results, add an error message to the error array
        if positive_a is None or positive_b is None:
            error_array.append(
                f"Test {positive['test_id']} failed criteria: {positive['criteria']}"
            )
            num_failed_matches += 1
            continue
        # If the person IDs for the two IDs match, increment the positive matches counter
        if positive_a["person_id"] == positive_b["person_id"]:
            num_successful_matches += 1
        # Otherwise, add an error message to the error array and increment the negative matches counter
        else:
            error_array.append(
                f"Test {positive['test_id']} failed criteria: {positive['criteria']}"
            )

            num_failed_matches += 1

    print(
        f"cases where the id is in the expected matches but not in the results: {error_array}"
    )

    return num_successful_matches, num_failed_matches, error_array


verify_positives(expected_matches, results)
