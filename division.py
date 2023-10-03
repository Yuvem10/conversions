def divHexa(nbResponse):
    hexaDiv = 16
    global res, resVirgule
    if nbResponse.__contains__("."):

        tabSplit = nbResponse.split(".")
        virgules = []

        for i in range(2):
            dividendStr = tabSplit[i]
            dividend = int(dividendStr)
            if i == 1:
                dividend = float("0." + dividendStr)
                while dividend != 0:
                    dividend = dividend * hexaDiv
                    split = str(dividend).split(".")
                    virgules.append(split[0])
                    splitInt = int(split[0])
                    dividend = dividend - splitInt

                for k in range(len(virgules)):
                    if virgules[k] == '10':
                        virgules[k] = "A"
                    elif virgules[k] == '11':
                        virgules[k] = "B"
                    elif virgules[k] == '12':
                        virgules[k] = "C"
                    elif virgules[k] == '13':
                        virgules[k] = "D"
                    elif virgules[k] == '14':
                        virgules[k] = "E"
                    elif virgules[k] == '15':
                        virgules[k] = "F"

                resVirgule = space.join(virgules)


            else:
                restes = []

                while dividend > hexaDiv:
                    quotient = dividend / hexaDiv
                    quotient = int(quotient)
                    r = int(dividend - (quotient * hexaDiv))
                    restes.append(str(r))
                    dividend = quotient

                for k in range(len(restes)):
                    if restes[k] == '10':
                        restes[k] = "A"
                    elif restes[k] == '11':
                        restes[k] = "B"
                    elif restes[k] == '12':
                        restes[k] = "C"
                    elif restes[k] == '13':
                        restes[k] = "D"
                    elif restes[k] == '14':
                        restes[k] = "E"
                    elif restes[k] == '15':
                        restes[k] = "F"

                dividend = str(dividend)

                longeur = len(restes)
                result = []
                while longeur > 0:
                    longeur = longeur - 1
                    result.append(restes[longeur])

                jsp = space.join(result)
                res = dividend + jsp
        print(res + "," + resVirgule)

    else:
        dividend = float(nbResponse)
        if dividend < hexaDiv:
            print("Tu es bete")

        else:
            restes = []

            while dividend > hexaDiv:
                quotient = dividend / hexaDiv
                quotient = int(quotient)
                r = int(dividend - (quotient * hexaDiv))
                restes.append(str(r))
                dividend = quotient

            for i in range(len(restes)):
                if restes[i] == '10':
                    restes[i] = "A"
                elif restes[i] == '11':
                    restes[i] = "B"
                elif restes[i] == '12':
                    restes[i] = "C"
                elif restes[i] == '13':
                    restes[i] = "D"
                elif restes[i] == '14':
                    restes[i] = "E"
                elif restes[i] == '15':
                    restes[i] = "F"

            dividend = str(dividend)

            longeur = len(restes)
            result = []
            while longeur > 0:
                longeur = longeur - 1
                result.append(restes[longeur])

            test = space.join(result)
            res = dividend + test
            print(res)


print("Pour une conversion en Hexadécimal écrivez 1")
print("Pour une conversion en Binaire écrivez 2")
response = input("Ta réponse:")
responseInt = int(response)
space = ""
if responseInt == 1:
    response = input("Le  nombre décimal à convertir:")
    divHexa(response)
