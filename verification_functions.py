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
            error_array.append(f"Test {positive['test_id']}: {positive['criteria']}")
            num_failed_matches += 1
            continue
        # If the person IDs for the two IDs match, increment the positive matches counter
        if positive_a["person_id"] == positive_b["person_id"]:
            num_successful_matches += 1
        # Otherwise, add an error message to the error array and increment the negative matches counter
        else:
            error_array.append(f"Test {positive['test_id']}: {positive['criteria']}")

            num_failed_matches += 1

        print(f"Number of successful matches: {num_successful_matches}")
        print(f"Number of failed matches: {num_failed_matches}")
        if num_failed_matches > 0:
            print("Failed match criteria:")
            for error in error_array:
                print(f"- {error}")

        return num_successful_matches, num_failed_matches, error_array

