#Tool by Ghast with some changes

with open("path/file.csv", 'r') as file:
    txt = "".join(file.readlines())
    print("([ " + "\n   ".join(["[{}],".format(t) for t in txt.split("\n") if t])[:-1] + " ])")
