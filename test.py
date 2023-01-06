import pandas as pd

from main import verify_positives


def test_verify_positives():
    # Create a sample dataframe for the positive tests
    positive_tests = pd.DataFrame(
        {
            "test_id": [1, 2, 3],
            "id_a": [1, 2, 3],
            "id_b": [2, 3, 4],
            "criteria": ["criteria1", "criteria2", "criteria3"],
        }
    )

    # Create a sample dataframe for the results
    results = pd.DataFrame({"party_id": [1, 2, 3, 4], "person_id": [1, 1, 2, 3]})

    # Test the verify_positives function with the sample data
    success, failure, errors = verify_positives(positive_tests, results)

    # Assert that the function returns the expected values
    assert success == 1
    assert failure == 2
    assert errors == [
        "Test 1 failed criteria: criteria1",
        "Test 3 failed criteria: criteria3",
    ]
