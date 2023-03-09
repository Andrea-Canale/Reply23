def write_matrix_to_file(filename, matrix, snake_num):
    rows = []
    for i in range(0, snake_num + 1):
        rows.append({
            "col_partenza": 0,
            "row_partenza": 0,
            "mov": [],
            "spawn_x": 0,
            "spawn_y": 0
        })

    i = 0
    j = 0
    for infos in matrix:
        for row in infos:
            if(row["snake"] != 0):
                i_parsed = int(row["snake"])
                rows[i_parsed]["mov"].append(row["cmd"])
                if(row["first_cell"]):
                    rows[i_parsed]["col_partenza"] = i
                    rows[i_parsed]["row_partenza"] = j
    print(rows)
    return rows