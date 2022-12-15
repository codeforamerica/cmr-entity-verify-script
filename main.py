import pandas as pd
positive_tests = pd.read_csv('positive.csv', header=0)
results = pd.read_csv('results.csv', header=0)

def verify_positives(positive_tests, results):
    errorArray = []
    positiveMatches = 0
    negativeMatches = 0
    results_by_id = { result["party_id"]: result for _, result in results.iterrows() }
    for _, positive in positive_tests.iterrows():
        positive_a = results_by_id.get(positive["id_a"])
        if positive_a is None:
            errorArray.append(f"{positive['id_a']} is in the positive tests but not in the results.")
            negativeMatches += 1
            continue;
        positive_b = results_by_id.get(positive["id_b"])
        if positive_b is None:
            errorArray.append(f"{positive['id_b']} is in the positive tests but not in the results.")
            negativeMatches += 1
            continue;
        if positive_a["person_id"] == positive_b["person_id"]:
            positiveMatches += 1
        else:
            errorArray.append(f"For positive test id {positive['test_id']} the person id associated with the two ids is not the same.")
            negativeMatches += 1
    return positiveMatches, negativeMatches, errorArray


print(verify_positives(positive_tests, results))


