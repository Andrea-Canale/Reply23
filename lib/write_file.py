import os


def generate_file(matrix, snake_num):
    rows = []
    for i in range(0, snake_num + 1):
        rows.append({
            "col_partenza": 0,
            "row_partenza": 0,
            "mov": ["C"]
        })

    i = 0
    j = 0
    for infos in matrix:
        for row in infos:
            if (row["snake"] != 0):
                i_parsed = int(row["snake"])
                rows[i_parsed]["mov"].append(row["cmd"])
                if (row["first_cell"]):
                    rows[i_parsed]["col_partenza"] = i
                    rows[i_parsed]["row_partenza"] = j
                if (row["worm"]):
                    rows[i_parsed]["mov"].append(row["worm_out"][0])
                    rows[i_parsed]["mov"].append(row["worm_out"][1])

    return rows

def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1

def write_file(final_dict, filename):
    try:
        os.remove(filename)
    except:
        None

    f = open(filename, 'a')
    for line in final_dict:
        f.write(str(line["col_partenza"]) + " " + str(line["row_partenza"]) + " " + listToString(line["mov"]))
        f.write('\n')

    f.close()