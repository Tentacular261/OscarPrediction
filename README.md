# OscarTeam2
Data Science project attempting to build a model to predict who will win the Oscars.

# To Update
###### Update award files (bafta, sag, best_actor, etc..) in all directories using reference websites
###### Run Movies/extract_movie_data.py to scrape movie review websites for info on movies listed in best_picture_nominations.txt
###### Run combine_award_data.py for ACTOR, ACTRESS, and DIRECTOR to get correctly formatted data for each one respectively
###### Run R Prediction scripts
  1. Actor/Actress/Director
    * Script name is just {actor,actress,director}Prediction.R
  2. Best Picture
    1. Run bafta.py with best_picture_nominations.txt as a command line arg (make sure print_best_picture() is at the end of the script)
    2. Output comes out as noms, wins
    3. Copy output into appropriate columns in Movies/movies.csv
    4. Run gg.py (best_picture_nominations.txt as a command line arg) with print_best_drama() at the end of the script, and
    5. Run with print_best_picture() at the end of the script for the musical/comedy category
    6. Output comes out as noms, wins
    7. Copy output into appropriate columns in Movies/movies.csv
    8. R Script is named logisticRegressionWinners.R

# Reference Websites
## Best Actor
* Oscars: https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor
* Screen Actor's Guild (SAG): https://en.wikipedia.org/wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Male_Actor_in_a_Leading_Role
* Golden Globe (GG) - Drama: https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Actor_–_Motion_Picture_Drama
* Golden Globe (GG) - Musical/Comedy: https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Actor_–_Motion_Picture_Musical_or_Comedy
* Critic's Choice (CC): https://en.wikipedia.org/wiki/Critics'_Choice_Movie_Award_for_Best_Actor
* BAFTA (Leading Role): https://en.wikipedia.org/wiki/BAFTA_Award_for_Best_Actor_in_a_Leading_Role

## Best Actress
* Oscars: https://en.wikipedia.org/wiki/Academy_Award_for_Best_Actress
* Screen Actor's Guild (SAG): https://en.wikipedia.org/wiki/Screen_Actors_Guild_Award_for_Outstanding_Performance_by_a_Female_Actor_in_a_Leading_Role
* Golden Globe (GG) - Drama: https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Actress_in_a_Motion_Picture_–_Motion_Picture_Drama
* Golden Globe (GG) - Musical/Comedy: https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Actress_–_Motion_Picture_Musical_or_Comedy
* Critic's Choice (CC): https://en.wikipedia.org/wiki/Critics'_Choice_Movie_Award_for_Best_Actress
* BAFTA (Leading Role): https://en.wikipedia.org/wiki/BAFTA_Award_for_Best_Actress_in_a_Leading_Role

## Best Director
* Oscars: https://en.wikipedia.org/wiki/Academy_Award_for_Best_Director
* Golden Globe (GG): https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Director
* Critic's Choice (CC): https://en.wikipedia.org/wiki/Critics'_Choice_Movie_Award_for_Best_Director
* BAFTA: https://en.wikipedia.org/wiki/BAFTA_Award_for_Best_Direction

## Best Picture
* Oscars: https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture
* Golden Globe (GG) - Drama: https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Motion_Picture_–_Drama
* Golden Globe (GG) - Musical/Comedy: https://en.wikipedia.org/wiki/Golden_Globe_Award_for_Best_Motion_Picture_–_Musical_or_Comedy
* BAFTA: https://en.wikipedia.org/wiki/BAFTA_Award_for_Best_Film
