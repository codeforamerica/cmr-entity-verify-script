import pandas as pd

from verification_functions import verify_positives
def test_verify_positives():
    positive_tests =  pd.DataFrame({
        "test_id": ["test_1", "test_2", "test_3"],
        "id_a": ["a_1", "a_2", "a_3"],
        "id_b": ["b_1", "b_2", "b_3"],
        "criteria": ["name", "address", "phone"]
    })
    results = pd.DataFrame({
         
        "party_id": ["a_1", "a_2", "b_1", "b_3", "a_3"],
        "person_id": [1, 2, 1, 4, 7]
    })

    num_successful_matches, num_failed_matches, error_array = verify_positives(positive_tests, results)
    assert num_successful_matches == 1
    assert num_failed_matches == 2
    assert len(error_array) == 2
    assert error_array[0] == "test_2, criteria: address"
    assert error_array[1] == "test_3, criteria: phone"

