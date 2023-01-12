import pandas as pd

from verification_functions import verify_positives
def test_verify_positives():
    # Create a positive_tests dataframe with test_id, id_a, id_b and criteria columns
    positive_tests =  pd.DataFrame({
        "test_id": ["test_1", "test_2", "test_3"],
        "id_a": ["a_1", "a_2", "a_3"],
        "id_b": ["b_1", "b_2", "b_3"],
        "criteria": ["name", "address", "phone"]
    })
    # Create a results dataframe with party_id and person_id columns
    results = pd.DataFrame({
        "party_id": ["a_1", "a_2", "b_1", "b_3", "a_3"],
        "person_id": [1, 2, 1, 4, 7]
    })
    # Call the verify_positives function with the positive_tests and results dataframes
    num_successful_matches, num_failed_matches, error_array = verify_positives(positive_tests, results)
    assert num_successful_matches == 1
    assert num_failed_matches == 2
    assert len(error_array) == 2
    assert error_array[0] == "test_2, criteria: address"
    assert error_array[1] == "test_3, criteria: phone"

def test_missing_columns_in_positives():
    # Create a positive_tests dataframe with test_id, id_a, and criteria columns, but missing 'id_b' column
    positive_tests =  pd.DataFrame({
        "test_id": ["test_1", "test_2", "test_3"],
        "id_a": ["a_1", "a_2", "a_3"],
        "criteria": ["name", "address", "phone"]
    })
    # Create a results dataframe with party_id and person_id columns
    results = pd.DataFrame({
        "party_id": ["a_1", "a_2", "b_1", "b_3", "a_3"],
        "person_id": [1, 2, 1, 4, 7]
    })

    # Test the function with the test data
    num_successful_matches, num_failed_matches, error_array = verify_positives(positive_tests, results)

    # Assert that the number of successful matches is 0
    assert num_successful_matches == 0
    # Assert that the number of failed matches is 1
    assert num_failed_matches == 3
    # Assert that the error array contains the expected error message
    assert error_array == ["Missing column in positive_tests dataframe", "Missing column in positive_tests dataframe", "Missing column in positive_tests dataframe"]
def test_missing_columns_in_results():
 # Create a positive_tests dataframe with test_id, id_a, id_b and criteria columns
    positive_tests =  pd.DataFrame({
        "test_id": ["test_1", "test_2", "test_3"],
        "id_a": ["a_1", "a_2", "a_3"],
        "id_b": ["b_1", "b_2", "b_3"],
        "criteria": ["name", "address", "phone"]
    })
    # Create a results dataframe with party_id and person_id columns
    results = pd.DataFrame({
        "party_id": ["a_1", "a_2", "b_1", "b_3", "a_3"],
    })

 
    num_successful_matches, num_failed_matches, error_array = verify_positives(positive_tests, results)
    assert num_successful_matches == 0
    assert num_failed_matches == 3
    assert error_array == ["Missing column in results dataframe", "Missing column in results dataframe", "Missing column in results dataframe"]
