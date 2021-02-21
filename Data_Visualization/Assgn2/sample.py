from datascience import Table;
hiv_prev_data = Table.read_table(
    './' + 'estimated_hiv_prevelance_indicator.csv')
 hiv_prev_data.row(1).
# print(hiv_prev_data)
hiv_prev_data_original = hiv_prev_data.copy(deep=True)
hiv_prev_data_original = hiv_prev_data.copy(deep=True)
hiv_prev_data["continent"] = "Rest of the world"
for ind in hiv_prev_data.index:
	try:
		country_code = pc.country_name_to_country_alpha2(
		    hiv_prev_data["country"][ind], cn_name_format="default")
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        if continent_code == "AF":
            hiv_prev_data["continent"][ind] = "Africa"
        elif continent_code == "AS":
            hiv_prev_data["continent"][ind] = "Asia"
        elif continent_code == "EU":
            hiv_prev_data["continent"][ind] = "Europe"
        elif continent_code == "OC":
            hiv_prev_data["continent"][ind] = "Australia/Oceania"
        elif continent_code == "NA":
            hiv_prev_data["continent"][ind] = "North America"
        elif continent_code == "SA":
			hiv_prev_data["continent"][ind] = "South America"
        elif continent_code == "AN":
            hiv_prev_data["continent"][ind] = "Antarctica"
    except:
		continue
export_csv = hiv_prev_data.to_csv('./estimated_hiv_prevelance_indicator_modified.csv')
# Correctness of the labelling can be verified by grouping the country names under each continent and verifying the data.
print(hiv_prev_data.groupby(['continent', 'country']).size()) ##printing the list of countries under each continent
# checking the list of rows in the orginal file and newly generated file to check if all the listed countries data exist.
print("row count in original file: ", hiv_prev_data_original.groupby(['country']).size().sum())
print("row count in newly generated file: ", hiv_prev_data.groupby(['continent']).size().sum())        
