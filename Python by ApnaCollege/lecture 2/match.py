color = input("enetr color :")

match color:
    case "green":
        print("go")
    case "yellow":
        print("get ready")
    case "red":
        print("stop")
    case _:
        print("wrong color !")