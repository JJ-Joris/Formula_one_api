import pandas as pd

def get_number_of_rounds(year):

    dfs = pd.read_html(f"https://en.wikipedia.org/wiki/{year}_Formula_One_World_Championship")

    round_list = []

    print("Checking the amount of races for this season.")

    for df in dfs:
        if "Round" in df.columns:
            for value in df["Round"].values:
                try:
                    round_list.append(int(value))
                except:
                    print("Value found that cannot be converted to an integer, this means we do not want it!")
            break

    return round_list