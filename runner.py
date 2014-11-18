__author__ = 'Kevin'


material_dictionary = {}
with open("input/2015.csv") as f:
    for line in f:
        cat = line.split(",")[0]
        uniq = line.split(",")[1]
        check = line.split(",")[2]

        if check == 'FALSE':
            continue
        if not cat in material_dictionary.keys():
            material_dictionary[cat] = []
        material_dictionary[cat].append(uniq)


with open("input/2015.csv") as f:
    for line in f:
        lookup = line.split(",")[-2]
        result = ""
        for each_cat in material_dictionary:
            if lookup in material_dictionary[each_cat]:
                result = each_cat

        check = line.split(",")[2]
        if check == 'FALSE':
            result = ""

        with open("output/result_s.csv", 'a+') as f:
            f.write(result + "\n")