
"""
Compiles all of the different award files into one. Each year shows how many
awards/nominations were received for that year only.

To change the script to get actor data or actress data, change the variable
AWARD_TYPE to "ACTOR", "ACTRESS", or "DIRECTOR" respectively.

Change the variables STARTING_YEAR and ENDING_YEAR to whatever years you want
data for.
"""
AWARD_TYPE = "DIRECTOR"
STARTING_YEAR = 2002
ENDING_YEAR = 2017

headers = []

# NOTE: headers[0:3] (Name, Year, OscarWon, OscarLost) should NOT be changed.
#       The rest can be changed as long as they are changed every where in the
#       file.
if AWARD_TYPE == "ACTOR" or AWARD_TYPE == "ACTRESS":
    headers = ["Name", "Year","OscarWon", "OscarLost", "SAGWon", "SAGLost",
               "GGDramaWon", "GGDramaLost", "GGMusicalWon", "GGMusicalLost",
               "CCWon", "CCLost", "BAFTAWon", "BAFTALost"]
elif AWARD_TYPE == "DIRECTOR":
    headers = ["Name", "Year", "OscarWon", "OscarLost", "GGWon", "GGLost",
               "CCWon", "CCLost", "BAFTAWon", "BAFTALost"]

class Entry():
    """
    Represents award information for a person for a specific year.

    Parameters
    ----------
    Year : int
        The year of the awards

    The rest of the parameters are made up of a prefix followed by a postfix.
    The prefixes are:
        Oscar
        SAG
        GGDrama
        GGMusical
        CC
        BAFTA

    The postfixes are:
        Won
        Lost
    """

    def __init__(self, Year=0, OscarWon=0, OscarLost=0, SAGWon=0, SAGLost=0,
                 GGDramaWon=0, GGDramaLost=0, GGMusicalWon=0, GGMusicalLost=0,
                 GGWon=0, GGLost=0, CCWon=0, CCLost=0, BAFTAWon=0, BAFTALost=0):
        self.categories = {}

        if AWARD_TYPE == "ACTOR" or AWARD_TYPE == "ACTRESS":
            self.categories["Year"] = Year
            self.categories["OscarWon"] = OscarWon
            self.categories["OscarLost"] = OscarLost
            self.categories["SAGWon"] = SAGWon
            self.categories["SAGLost"] = SAGLost
            self.categories["GGDramaWon"] = GGDramaWon
            self.categories["GGDramaLost"] = GGDramaLost
            self.categories["GGMusicalWon"] = GGMusicalWon
            self.categories["GGMusicalLost"] = GGMusicalLost
            self.categories["CCWon"] = CCWon
            self.categories["CCLost"] = CCLost
            self.categories["BAFTAWon"] = BAFTAWon
            self.categories["BAFTALost"] = BAFTALost
        elif AWARD_TYPE == "DIRECTOR":
            self.categories["Year"] = Year
            self.categories["OscarWon"] = OscarWon
            self.categories["OscarLost"] = OscarLost
            self.categories["GGWon"] = GGWon
            self.categories["GGLost"] = GGLost
            self.categories["CCWon"] = CCWon
            self.categories["CCLost"] = CCLost
            self.categories["BAFTAWon"] = BAFTAWon
            self.categories["BAFTALost"] = BAFTALost

    def __lt__(self, other):
        return self.categories[year] < other.categories

    def __str__(self):
        """
        How an Entry would look if you called str() on it. E.g., if you called
        print str(ENTRY) where ENTRY is the name of instance of the Entry class.
        """
        ret = ""

        for header in headers[1:]:
            ret += str(self.categories[header]) + ","

        ret = ret[:-1] + "\n"

        return ret

    def update(self, category, new_value):
        """
        Updates one of the award categories to *new_value*

        Parameters
        ----------
        category : str
            One of the keys to the categories member dictionary. Possible
            values are all of the values in the global list headers *except*
            for "Name"
        new_value : int
            The number of awards/nominations the person got for that specific
            award/nomination.
        """

        self.categories[category] = new_value


class AwardFile():
    """
    Represents an award file

    Parameters
    ----------
    file_name : str
        The name of the award file to represent.
    """
    def __init__(self, file_name):
        self.year_data = {} # year => name_data dictionary
        name_data = {} # name => number of awards/nominations

        is_winner = True
        old_year = 0

        # Parse through the file
        with open(file_name, "r") as f:
            for line in f:
                if line.strip() == ",":
                    continue

                year = int(line.split(",")[0])
                name = line.strip().split(",")[1].split(" (TIE)")[0]

                if year != old_year:
                    self.year_data[old_year] = name_data
                    name_data = {} # name => number of awards/nominations

                    old_year = year
                    is_winner = True
                elif line.strip().split(",")[1].split(" ")[-1] == "(TIE)":
                    is_winner = True

                if is_winner == True:
                    name_data[name] = 1
                    is_winner = False
                else:
                    name_data[name] = 0

        self.year_data[old_year] = name_data

    def get_year_data(self, year):
        """
        Gets the number of awards/nominations a person received for a specific
        year.

        Parameters
        ----------
        year : int
            The year you want award information for.

        Returns
        -------
        dictionary
            A dictionary representing all people who won awards or received
            nominations for awards for a specific year. The name of the person
            is the key and the number of awards is the value.
        """
        return self.year_data[year]

    def get_summed_year_data(self, year_limit):
        """
        Gets the number of all of the awards/nominations a person received up to
        a specific year.

        Parameters
        ----------
        year : int
            The year that you want to limit your data to

        Returns
        -------
        dictionary
            A dictionary with the names of the people who won awards or were
            nominated for awards as the keys and for the values, a list
            containing the number of awards won as the zeroeth
            index and the number of awards lost (how many nominations they
            received) as the first index.
        """

        awards = {} # name => [awards, nominations]

        for year,names in sorted(self.year_data.items(), reverse=False):
            if year <= year_limit:
                for name,num_awards in names.items():
                    if name in awards:
                        if num_awards == 1:
                            awards[name][0] += 1
                        else:
                            awards[name][1] += 1
                    else:
                        if num_awards == 1:
                            awards[name] = [1, 0]
                        else:
                            awards[name] = [0, 1]

        return awards

def prepare_csv_data():
    """
    Combine all of the award files into one, limiting the people to only include
    those that were nominated for an Oscar.

    Returns
    -------
    list of str
        The properly formatted lines of the csv files
    """
    csv_lines = []

    # Get the files that we'll be using
    if AWARD_TYPE == "ACTOR":
        sag_award_file = AwardFile("Actors/SAG_Actors.csv")
        gg_drama_award_file = AwardFile("Actors/GG_Drama_Actors.csv")
        gg_musical_award_file = AwardFile("Actors/GG_Musical_Actors.csv")
        cc_award_file = AwardFile("Actors/CC_Actors.csv")
        bafta_award_file = AwardFile("Actors/BAFTA_Actors.csv")

        oscar_nomination_file = "Actors/best_actor_nominations.txt"
    elif AWARD_TYPE == "ACTRESS":
        sag_award_file = AwardFile("Actresses/SAG_Actress.csv")
        gg_drama_award_file = AwardFile("Actresses/GG_Drama_Actress.csv")
        gg_musical_award_file = AwardFile("Actresses/GG_Musical_Actress.csv")
        cc_award_file = AwardFile("Actresses/CC_Actress.csv")
        bafta_award_file = AwardFile("Actresses/BAFTA_Actress.csv")

        oscar_nomination_file = "Actresses/best_actress_nominations.txt"
    elif AWARD_TYPE == "DIRECTOR":
        gg_award_file = AwardFile("Directors/GG_Directors.csv")
        cc_award_file = AwardFile("Directors/CC_Directors.csv")
        bafta_award_file = AwardFile("Directors/BAFTA_Directors.csv")

        oscar_nomination_file = "Directors/best_director_nominations.txt"

    # Get the names that were nominated for an Oscar so we can filter our data
    # to only include the relevent names of just those who were nominated for an
    # Oscar.
    oscar_nomination_lines = []
    with open(oscar_nomination_file, "r") as f:
        for line in f:
            oscar_nomination_lines.append(line.strip())

    oscar_line_index = 0

    for year in range(STARTING_YEAR,ENDING_YEAR+1):
        list_of_data_dictionaries = []

        # NOTE: Uncomment this to get data upto each year
        # if AWARD_TYPE == "ACTOR" or AWARD_TYPE == "ACTRESS":
        #     sag_data = sag_award_file.get_summed_year_data(year)
        #     gg_drama_data = gg_drama_award_file.get_summed_year_data(year)
        #     gg_musical_data = gg_musical_award_file.get_summed_year_data(year)
        #     cc_data = cc_award_file.get_summed_year_data(year)
        #     bafta_data = bafta_award_file.get_summed_year_data(year)
        # elif AWARD_TYPE == "DIRECTOR":
        #     gg_data = gg_award_file.get_summed_year_data(year)
        #     cc_data = cc_award_file.get_summed_year_data(year)
        #     bafta_data = bafta_award_file.get_summed_year_data(year)
        ##

        # NOTE: Comment this if you want to get data upto each year
        # Get the award dictionaries for each award show
        if AWARD_TYPE == "ACTOR" or AWARD_TYPE == "ACTRESS":
            sag_data = sag_award_file.get_year_data(year)
            gg_drama_data = gg_drama_award_file.get_year_data(year)
            gg_musical_data = gg_musical_award_file.get_year_data(year)
            cc_data = cc_award_file.get_year_data(year)
            bafta_data = bafta_award_file.get_year_data(year)
        elif AWARD_TYPE == "DIRECTOR":
            gg_data = gg_award_file.get_year_data(year)
            cc_data = cc_award_file.get_year_data(year)
            bafta_data = bafta_award_file.get_year_data(year)
        ##

        # put all of the dictionaries into a list so we can iterate through them

        if AWARD_TYPE == "ACTOR" or AWARD_TYPE == "ACTRESS":
            list_of_data_dictionaries.append(sag_data)
            list_of_data_dictionaries.append(gg_drama_data)
            list_of_data_dictionaries.append(gg_musical_data)
            list_of_data_dictionaries.append(cc_data)
            list_of_data_dictionaries.append(bafta_data)
        elif AWARD_TYPE == "DIRECTOR":
            list_of_data_dictionaries.append(gg_data)
            list_of_data_dictionaries.append(cc_data)
            list_of_data_dictionaries.append(bafta_data)

        entry_dictionary = {}

        # i is an index variable for the headers at the beginning of this file.
        # We start it at 4 to skip the first 4 headers which we don't need.
        i = 4
        for dictionary in list_of_data_dictionaries:
            for name,awards in dictionary.items():
                # Check if the person was nominated for an oscar that year. If
                # they weren't, we don't care about them, so skip them.
                if name not in oscar_nomination_lines[oscar_line_index:oscar_line_index+5]:
                    continue

                if name not in entry_dictionary:
                    entry = Entry(Year=year)

                    # NOTE: Uncomment this to get data upto each year
                    # entry.update(headers[i], awards[0])
                    # entry.update(headers[i+1], awards[1])
                    ##

                    # NOTE: Comment this if you want to get data upto each year
                    # headers[i] will be the "Won" category for the award,
                    # whereas headers[i] will be the "Lost" category.
                    # If they won any awards, set "Won" category to however
                    # many awards they won. If they didn't win any, set the
                    # "Lost" category to 1.
                    if awards > 0:
                        entry.update(headers[i], awards)
                    else:
                        entry.update(headers[i+1], 1)
                    ##

                    if name == oscar_nomination_lines[oscar_line_index]:
                        entry.update("OscarWon", 1)
                    else:
                        entry.update("OscarLost", 1)

                    entry_dictionary[name] = entry
                else:
                    # NOTE: Uncomment this to get data upto each year
                    # entry_dictionary[name].update(headers[i], awards[0])
                    # entry_dictionary[name].update(headers[i+1], awards[1])
                    ##

                    # NOTE: Comment this if you want to get data upto each year
                    # headers[i] will be the "Won" category for the award,
                    # whereas headers[i] will be the "Lost" category.
                    # If they won any awards, set "Won" category to however
                    # many awards they won. If they didn't win any, set the
                    # "Lost" category to 1.
                    if awards > 0:
                        entry_dictionary[name].update(headers[i], awards)
                    else:
                        entry_dictionary[name].update(headers[i+1], 1)
                    ##

            # Each major header has a "Won" and a "Lost" category. By
            # incrementing by 2, we go from one major header to the next
            # (e.g., SAG to GG).
            i += 2

        for name,entry in entry_dictionary.items():
            csv_lines.append(name + "," + str(entry))

        # There are 5 oscar nominations per year, so add 5 to go the nominations
        # for the next year.
        oscar_line_index += 5

    # Make sure that all Oscar nominations are included in the final csv file
    counter = 0

    for i in range(0, len(oscar_nomination_lines)):
        if i == len(csv_lines):
            break

        name = oscar_nomination_lines[i].strip()

        names_already_in_csv = []
        for n in csv_lines[counter:counter+5]:
            names_already_in_csv.append(n.split(",")[0].strip())

        if name in names_already_in_csv:
            if (i+1) % 5 == 0:
                counter += 5

            continue
        else:
            new_line = name + "," + csv_lines[counter].split(",")[1] + ","

            if name == oscar_nomination_lines[counter]:
                # WINNER
                new_line += "1,0,"
            else:
                # LOSER
                new_line += "0,1,"

            for header in headers[4:]:
                new_line += "0,"

            new_line = new_line[:-1] + "\n"

            csv_lines.insert(i, new_line)

        if (i+1 )% 5 == 0:
            counter += 5

    return csv_lines

def write_csv(csv_lines):
    # Set the file that we'll write out to.
    if AWARD_TYPE == "ACTOR":
        file_name = "Actors/actor_award_data_formatted.csv"
    elif AWARD_TYPE == "ACTRESS":
        file_name = "Actresses/actress_award_data_formatted.csv"
    elif AWARD_TYPE == "DIRECTOR":
        file_name = "Directors/director_award_data_formatted.csv"

    # Write the header information
    line = ""
    for header in headers:
        line += header + ","
    line = line[:-1] + "\n"

    with open(file_name, "w") as f:
        f.write(line)

    # Write the values
    with open(file_name, "a") as f:
        for line in csv_lines:
            f.write(line)

##### START #####
csv_lines = prepare_csv_data()

write_csv(csv_lines)
