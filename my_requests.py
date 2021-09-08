import pandas as pd

def get_results(year, round):
    results_endpoint = f"http://ergast.com/api/f1/{year}/{round}/results.json"

    df = pd.read_json(results_endpoint)

    round = df["MRData"]["RaceTable"]["Races"][0]["round"]

    ResulstsList = df["MRData"]["RaceTable"]["Races"][0]["Results"]

    results_df = pd.DataFrame(columns={"position", "given_name", "family_name", "full_name", "points", "start_position"})

    position_list = []
    given_name_list = []
    family_name_list = []
    full_name_list = []
    points_list = []
    start_position_list = []
    for result in ResulstsList:
        try:
            position_list.append(int(result["position"]))
            given_name_list.append(result["Driver"]["givenName"])
            family_name_list.append(result["Driver"]["familyName"])
            full_name_list.append(result["Driver"]["givenName"]+"_"+result["Driver"]["familyName"])
            points_list.append(int(result["points"]))
            start_position_list.append(int(result["grid"]))
        except:
            print("Values not able to be added, something is wrong!")

    results_df["position"] = position_list
    results_df["given_name"] = given_name_list
    results_df["family_name"] = family_name_list
    results_df["full_name"] = full_name_list
    results_df["points"] = points_list
    results_df["start_position"] = start_position_list

    return results_df