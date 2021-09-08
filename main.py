from my_requests import get_results
from wikipedia_scrape import get_number_of_rounds
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

if __name__ == "__main__":

    year = 2013
    driver = "Fernando"

    if not os.path.exists(f"results_{year}.pkl"):
        print("file not present yet... creating it now")

        amount_of_rounds_list = get_number_of_rounds(year)

        results_to_save = pd.DataFrame()

        for round in amount_of_rounds_list:
            results_from_the_web = get_results(year, round)

            results_to_save["drivers_fullname_round_"+str(round)] = results_from_the_web["full_name"]
            results_to_save["drivers_given_name_round_"+str(round)] = results_from_the_web["given_name"]
            results_to_save["drivers_family_name_round_"+str(round)] = results_from_the_web["family_name"]
            results_to_save["position"] = results_from_the_web["position"]
            results_to_save["points"] = results_from_the_web["points"]
            results_to_save["start_position"] = results_from_the_web["start_position"]

        print(results_to_save)

        results_to_save.to_pickle(f"results_{year}.pkl")
    else:
        print("file present, ready to start!")

        results_df = pd.read_pickle(f"results_{year}.pkl")

        if driver in results_df["drivers_given_name_round_1"].values:

            amount_of_rounds_list = get_number_of_rounds(year)

            show_table_df = pd.DataFrame()

            points_scored = 0
            start_position_list = []
            finish_position_list = []
            positions_won_list = []
            points_scored_list = []
            for round in amount_of_rounds_list:
                finish_position = results_df.loc[results_df[f'drivers_given_name_round_{round}'] == driver, 'position'].iloc[0]
                finish_position_list.append(finish_position)
                start_position = results_df.loc[results_df[f'drivers_given_name_round_{round}'] == driver, 'start_position'].iloc[0]
                start_position_list.append(start_position)
                points_scored += results_df.loc[results_df[f'drivers_given_name_round_{round}'] == driver, 'points'].iloc[0]
                points_scored_list.append(results_df.loc[results_df[f'drivers_given_name_round_{round}'] == driver, 'points'].iloc[0])
                positions_won_list.append((start_position-finish_position))
                #print("Round " + str(round) + "--start position : " + str(start_position) + " --finish position : " + str(finish_position))

            show_table_df["start_position"] = start_position_list
            show_table_df["finish_position"] = finish_position_list
            show_table_df["positions_won"] = positions_won_list
            show_table_df["points_scored"] = points_scored_list

            fig, ax = plt.subplots()

            # hide axes
            fig.patch.set_visible(False)
            ax.axis('off')
            ax.axis('tight')

            ax.table(cellText=show_table_df.values, colLabels=show_table_df.columns, loc='center')

            #fig.tight_layout()

            red_patch = mpatches.Patch(color='red', label=points_scored)
            plt.legend(handles=[red_patch])

            plt.title(driver)
            plt.show()

            #print(f"Total amount of points scored: {points_scored}")
        else:
            print("Driver not found in the list!")
