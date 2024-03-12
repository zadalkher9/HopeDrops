def permissionSlip():
    permissionSlip = input("Did you bring back a signed permission slip?")

    if permissionSlip == "yes":
        historyQuestion = input("Which number amendment allowed women to vote in the US?")

        if historyQuestion == "19":
            print("You're going to the hsitory museum")
        elif historyQuestion != "19":
            print("You're going to the art museum ")
        else:
            print("You can't go on the field trip")
