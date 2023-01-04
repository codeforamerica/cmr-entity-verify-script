import pandas as pd
import sys

file_for_positives = sys.argv[1]
file_for_results = sys.argv[2]

positive_tests = pd.read_csv(file_for_positives, header=0)
results = pd.read_csv(file_for_results, header=0)


def verify_positives(positive_tests, results):
    error_array = []
    positive_matches = 0
    negative_matches = 0
    results_by_id = {result["party_id"]: result for _, result in results.iterrows()}

    for _, positive in positive_tests.iterrows():
        positive_a = results_by_id.get(positive["id_a"])
        if positive_a is None:  # or positive_b is
            error_array.append(
                # f"{positive['id_a']} is in the positive tests but not in the results."
                f"{positive['test_id']}, criteria: {positive['criteria']}"
            )
            negative_matches += 1
            continue
        positive_b = results_by_id.get(positive["id_b"])
        if positive_b is None:
            error_array.append(
                f"{positive['test_id']}, criteria: {positive['criteria']}"
                # f"{positive["test_id"]}" #f"criteria: {positive["criteria"]}"
            )
            negative_matches += 1
            continue
        if positive_a["person_id"] == positive_b["person_id"]:
            positive_matches += 1

        else:
            error_array.append(
                # positive["test_id"]
                f"{positive['test_id']}, criteria: {positive['criteria']}"
            )
            #     error_array.append(
            #         f"For positive test id {positive['test_id']} the person id associated with the two ids is not the same."
            #     )
            negative_matches += 1

    print(
        f"cases where the id is in the positive tests but not in the results: {error_array}"
    )

    return positive_matches, negative_matches, error_array


verify_positives(positive_tests, results)
