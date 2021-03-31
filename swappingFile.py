def changeData():
    file_a_path = input("Please the Give the Path fof File A")
    file_b_path = input("Please the Give the Path fof File B")

    file_a = open(file_a_path, "r")
    data_a = file_a.read()

    file_b = open(file_b_path, "r")
    data_b = file_b.read()

    file_a = open(file_a_path, "w")
    file_b = open(file_b_path, "w")

    file_a.write(data_b)
    file_b.write(data_a)

changeData()