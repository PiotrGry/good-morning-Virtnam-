def import_file(file_name="DZIALKI.TXT"):
    dzialki = open(file_name)
    dzialki_list = []
    for line in dzialki.readlines():
        dzialki_list.append(line.strip("\n").split(";"))

    dzialki.close()
    return(dzialki_list[1:])


def smallest_area(dzialki_list):
    minimum = dzialki_list[0][1]
    typ_min_dzialki = ""
    for i in range(1, len(dzialki_list)):
        if minimum > dzialki_list[i][1]:
            minimum = dzialki_list[i][1]
            typ_min_dzialki = dzialki_list[i][2]

    return minimum, typ_min_dzialki


def converting_point(dzialki_list):
    for row in dzialki_list:
        row[1] = float(row[1].replace(",", "."))
    return dzialki_list


def biggest_area(dzialki_list):
    maximum = dzialki_list[0][1]
    typ_max_dzialki = " "
    for i in range(1, len(dzialki_list)):
        if maximum < dzialki_list[i][1]:
            maximum = dzialki_list[i][1]
            typ_max_dzialki = dzialki_list[i][2]
    return maximum, typ_max_dzialki


def statistics(dzialki_list):
    """ 0-R 1-B 2-S 3-L 4-X """

    stat_list = []
    stat_list.append(["R", 0, 0.0])
    stat_list.append(["B", 0, 0.0])
    stat_list.append(["S", 0, 0.0])
    stat_list.append(["L", 0, 0.0])
    stat_list.append(["X", 0, 0.0])
    for row in dzialki_list:
        if row[2] == "R":
            stat_list[0][1] += 1
            stat_list[0][2] += row[1]
        elif row[2] == "B":
            stat_list[1][1] += 1
            stat_list[1][2] += row[1]
        elif row[2] == "S":
            stat_list[2][1] += 1
            stat_list[2][2] += row[1]
        elif row[2] == "L":
            stat_list[3][1] += 1
            stat_list[3][2] += row[1]
        elif row[2] == "X":
            stat_list[4][1] += 1
            stat_list[4][2] += row[1]

    for ele in stat_list:
        (ele[2]) = round(ele[2] / ele[1], 2)

    print(stat_list)


def main():
    dzialki_list = import_file()
    dzialki_list = converting_point(dzialki_list)
    minimum, typ_min_dzialki = smallest_area(dzialki_list)
    maximum, typ_max_dzialki = biggest_area(dzialki_list)
    statistics(dzialki_list)
    print(dzialki_list)


if __name__ == "__main__":
    main()
