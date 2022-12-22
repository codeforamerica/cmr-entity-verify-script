# TODO use python's 'csv' module instead of pandas
# import 'csv'
# positive_tests = pd.read_csv('positive.csv', header=0)
# results = pd.read_csv('results.csv', header=0)

# TODO auto parse above csvs into these objects
parties = [{
  "test_id": 1,
  "criteria": "CITY_CITY NAME ABBREVIATED",
  "id_a": "C-1000",
  "id_b": "C-1001"
}, {
  "test_id": 2,
  "criteria": "ADDRESS_1_DIFFERENT ADDRESSES",
  "id_a": "C-1003",
  "id_b": "C-1004"
}]

results = [{
  "person_id": 3,
  "database": "C",
  "party_id": "C-1000",
  "match_score": 14,
  "potential_person_id": 3912265,
  "potential_match_score": 11
}, {
  "person_id": 3,
  "database": "C",
  "party_id": "C-1001",
  "match_score": 11,
  "potential_person_id": 3802264,
  "potential_match_score": 11
}, {
  "person_id": 3,
  "database": "C",
  "party_id": "C-1002",
  "match_score": 15,
  "potential_person_id": 855412,
  "potential_match_score": 12
}, {
  "person_id": 7,
  "database": "C",
  "party_id": "C-1057",
  "match_score": 11,
  "potential_person_id": 5802266,
  "potential_match_score": 10
}, {
  "person_id": 7,
  "database": "C",
  "party_id": "C-1058",
  "match_score": 14,
  "potential_person_id": 555413,
  "potential_match_score": 11
}, {
  "person_id": 7,
  "database": "C",
  "party_id": "C-1060",
  "match_score": 12,
  "potential_person_id": 5702268,
  "potential_match_score": 11
}, {
  "person_id": 7,
  "database": "C",
  "party_id": "C-1059",
  "match_score": 12,
  "potential_person_id": 515413,
  "potential_match_score": 11
}, {
  "person_id": 9,
  "database": "C",
  "party_id": "C-1029",
  "match_score": 11,
  "potential_person_id": 1030,
  "potential_match_score": 5
}, {
  "person_id": 12,
  "database": "C",
  "party_id": "C-1003",
  "match_score": 14,
  "potential_person_id": 3911268,
  "potential_match_score": 11
}, {
  "person_id": 12,
  "database": "C",
  "party_id": "C-1004",
  "match_score": 11,
  "potential_person_id": 3912269,
  "potential_match_score": 11
}, {
  "person_id": 13,
  "database": "C",
  "party_id": "C-1006",
  "match_score": 8,
  "potential_person_id": 3912359,
  "potential_match_score": 11
}, {
  "person_id": 13,
  "database": "C",
  "party_id": "C-1005",
  "match_score": 15,
  "potential_person_id": 3952258,
  "potential_match_score": 11
}, {
  "person_id": 15,
  "database": "C",
  "party_id": "C-1030",
  "match_score": 12,
  "potential_person_id": 1029,
  "potential_match_score": 4
}, {
  "person_id": 19,
  "database": "C",
  "party_id": "C-1025",
  "match_score": "",
  "potential_person_id": "",
  "potential_match_score": ""
}, {
  "person_id": 27,
  "database": "C",
  "party_id": "C-1036",
  "match_score": 11,
  "potential_person_id": 3802242,
  "potential_match_score": 10
}, {
  "person_id": 27,
  "database": "C",
  "party_id": "C-1035",
  "match_score": 15,
  "potential_person_id": 855414,
  "potential_match_score": 14
}, {
  "person_id": 38,
  "database": "C",
  "party_id": "C-1010",
  "match_score": 10,
  "potential_person_id": 1912255,
  "potential_match_score": 10
}, {
  "person_id": 38,
  "database": "C",
  "party_id": "C-1009",
  "match_score": 10,
  "potential_person_id": 1912256,
  "potential_match_score": 10
}]

# TODO parameterize tests per row in this csv
def test_positive_matches():
  id_a = parties[1]['id_a']
  id_b = parties[1]['id_b']

  person_a = ''
  person_b = ''

  for result in results:
    if id_a == result['party_id']:
      person_a = result['person_id']
    if id_b == result['party_id']:
      person_b = result['person_id']

      assert person_a == person_b
