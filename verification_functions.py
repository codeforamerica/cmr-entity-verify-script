def verify_positives(positive_tests, results):
    # Initialize an empty list to store any errors that are encountered
    error_array = []

    # Initialize counters for the number of successful and failed matches
    num_successful_matches = 0
    num_failed_matches = 0

    # Create a dictionary mapping party IDs to rows in the results dataframe
    results_by_id = {result["party_id"]: result for _, result in results.iterrows()}

    # Iterate over the rows in the positive tests dataframe
    for _, positive in positive_tests.iterrows():
        # Look up the results for the IDs in the positive test
        positive_a = results_by_id.get(positive["id_a"])
        positive_b = results_by_id.get(positive["id_b"])

        # If either of the IDs is not found in the results, add an error to the error array and skip to the next iteration
        if positive_a is None or positive_b is None:
            error_array.append(f"{positive['test_id']}, criteria: {positive['criteria']}")
            num_failed_matches += 1
            continue

        # If the person IDs for the two IDs are not the same, add an error to the error array and increment the failed matches counter
        if positive_a["person_id"] != positive_b["person_id"]:
            error_array.append(f"{positive['test_id']}, criteria: {positive['criteria']}")
            num_failed_matches += 1
        # Otherwise, increment the successful matches counter
        else:
            num_successful_matches += 1

    # Print the number of successful and failed matches, and any errors that were encountered
    print(f"Number of successful matches: {num_successful_matches}")
    print(f"Number of failed matches: {num_failed_matches}")
    if num_failed_matches > 0:
        print("Failed match criteria:")
        for error in error_array:
            print(f"- {error}")

    # Return the number of successful and failed matches, and the error array
    return num_successful_matches, num_failed_matches, error_array
