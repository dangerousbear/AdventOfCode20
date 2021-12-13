lines = [line[:-1] for line in open("4.txt", "r").readlines()]

def between(x,y,z):
    return x <= y and y <= z

tokensToFind = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

count = 0
tokens = tokensToFind.copy()
dataOK = True
for line in lines:
    if (line == ''): #New passport
        if len(tokens.intersection(tokensToFind)) == 7 and dataOK:
            count += 1
        tokens = set()
        dataOK = True
    else:
        for tag in line.split():
            tagParts = tag.split(":")
            tagName = tagParts[0]
            tagVal = tagParts[1]
            if tagName == "byr":
                dataOK = dataOK and between( 1920, int(tagVal), 2002 )
                print(tagName + " " + str(dataOK))
            elif tagName == "iyr":
                dataOK = dataOK and between( 2010, int(tagVal), 2020 )
                print(tagName + " " + str(dataOK))
            elif tagName == "eyr":
                dataOK = dataOK and between( 2020, int(tagVal), 2030 )
                print(tagName + " " + str(dataOK))
            elif tagName == "hgt":
                isCM = tagVal[-2:] == "cm"
                unitOK = isCM or tagVal[-2:] == "in" 
                dataOK = dataOK and unitOK and ( between( 150, int(tagVal[:-2]), 193 ) if isCM else between( 59, int(tagVal[:-2]), 76 ) )
                print(tagName + " " + str(dataOK))
            elif tagName == "hcl":
                dataOK = dataOK and tagVal[0] == "#" and all(x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a','b','c','d','e','f'] for x in tagVal[1:])
                print(tagName + " " + str(dataOK))
            elif tagName == "ecl":
                dataOK = dataOK and tagVal in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                print(tagName + " " + str(dataOK))
            elif tagName == "pid":
                dataOK = dataOK and len(tagVal) == 9
                print(tagName + " " + str(dataOK))
            else:
                assert(tagName == "cid")
            tokens.add(tagName)

print(count)