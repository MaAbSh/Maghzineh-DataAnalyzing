import Coding

class HighwayDecoding(Coding.CodingFactory):
    ## according to the coding algorithm, the required lists are defined:
    
    listHds1 = [] # the list for the first character of HDS
    listHds1.append(Coding.CodingVariable(4)) # for the difficulty

    listHds2 = [] # the list for the second character of HDS
    listHds2.append(Coding.CodingVariable(4)) # for the gate line
    listHds2.append(Coding.CodingVariable(2)) # for is the car selected
    listHds2.append(Coding.CodingVariable(8)) # for the number of the unselected cars

    listChd1 = [] # the list for the first part of CHD (due to the lines) (the line number is defined according to the level of the trail)
    listChd1.append(Coding.CodingVariable(4)) # for the line number
    listChd1.append(Coding.CodingVariable(4)) # for the line color

    listChd2 = [] # the list for the other part of CHD (due to the cars)
    listChd2.append(Coding.CodingVariable(4)) # for the car name
    listChd2.append(Coding.CodingVariable(4)) # for the car color
    listChd2.append(Coding.CodingVariable(4)) # for the car line

    def getIsBlack (Level):
        match Level:
            case 2:
                return 1
            
            case 3:
                return 1
            
            case 4:
                return 1
            
            case 9:
                return 1
            
            case 10:
                return 1
            
            case 11:
                return 1
            
            case 12:
                return 1
            
            case 13:
                return 1
            
            case 14:
                return 1
        return 0

            

    def getEntraceNumber (Level):
        match Level:
            case 1:
                return 3
            
            case 2:
                return 3
            
            case 3:
                return 3
            
            case 4:
                return 4
            
            case 5:
                return 3
            
            case 6:
                return 3
            
            case 7:
                return 3
            
            case 8:
                return 4
                
            case 9:
                return 3
            
            case 10:
                return 3
            
            case 11:
                return 3
            
            case 12:
                return 4
            
            case 13:
                return 4
            
            case 14:
                return 4
            
            case 15:
                return 3
            
            case 16:
                return 3
            
            case 17:
                return 3
            
            case 18:
                return 4
            
            case 19:
                return 3
            
            case 20:
                return 3
            
            case 21:
                return 3
            
            case 22:
                return 4
            
            case 23:
                return 4
            
            case 24:
                return 4

    def Decoding (tempStr1,Level):
        print(tempStr1)
        
        position = tempStr1.find("TFS:[")
        tempStr1 = tempStr1[(position+5):]
        position = tempStr1.find("]")
        tfsStr = tempStr1[:(position)]
        tempStr1 = tempStr1[(position+1):]

        position = tempStr1.find("RTS:[")
        tempStr1 = tempStr1[(position+5):]
        position = tempStr1.find("]")
        rtsStr = tempStr1[:(position)]
        tempStr1 = tempStr1[(position+1):]

        position = tempStr1.find("HDS:[")
        tempStr1 = tempStr1[(position+5):]
        position = tempStr1.find("]")
        hdsStr = tempStr1[:(position)]
        tempStr1 = tempStr1[(position+1):]

        position = tempStr1.find("CHD:[")
        tempStr1 = tempStr1[(position+5):]
        chdStr = tempStr1[0:(len(tempStr1)-1)]

        EntraceNumber =  HighwayDecoding.getEntraceNumber(Level)

        TFSeq = []
        RTSeq = []
        difficultySeq = []
        gateLineSeq = []
        selectedCarSeq = []
        unselectedNumberSeq = []
        lineNameList = []
        lineColorList = []
        carNameList = []
        carColorList = []
        carLineList = []

        if (len(tfsStr)>0):
            for c in tfsStr:
                if (c == 'T'):
                    TFSeq.append(1)
                else:
                    TFSeq.append(0)

        if (len(rtsStr)>0):
            rtsArray = rtsStr.split(",")
            for c in rtsArray:
                RTSeq.append(int(c))

        if (len(hdsStr)>0):
            hdrArray = hdsStr.split(",")
            for c in hdrArray:
                Coding.CodingFactory.breakingVariables(c[0],HighwayDecoding.listHds1)
                difficultySeq.append(HighwayDecoding.listHds1[0].x)
                Coding.CodingFactory.breakingVariables(c[1],HighwayDecoding.listHds2)
                gateLineSeq.append(HighwayDecoding.listHds2[0].x)
                selectedCarSeq.append(HighwayDecoding.listHds2[1].x)
                unselectedNumberSeq.append(HighwayDecoding.listHds2[2].x)

        if (len(chdStr)>0):
            for i in range(0,len(chdStr)):
                c = chdStr[i]
                if (i < EntraceNumber):
                    Coding.CodingFactory.breakingVariables(c,HighwayDecoding.listChd1)
                    lineNameList.append(HighwayDecoding.listChd1[0].x)
                    lineColorList.append(HighwayDecoding.listChd1[1].x)
                else:
                    Coding.CodingFactory.breakingVariables(c,HighwayDecoding.listChd2)
                    carNameList.append(HighwayDecoding.listChd2[0].x)
                    carColorList.append(HighwayDecoding.listChd2[1].x)
                    carLineList.append(HighwayDecoding.listChd2[2].x)

        if ( (len(TFSeq) > 0) and (len(TFSeq) == len(difficultySeq)) and (len(TFSeq) == len(RTSeq)) ):

            TN = TFSeq.count(1)
            TF = TFSeq.count(0)

            print( "In this trial we have:" )
            print( "# Level = " + str(Level) )
            print( "# The number of true/false responses = " + str(TN) + "/" + str(TF) + " (True/False, Difficulty, ExitLine, isCarSelected, NumberOfUnselectedCars)" )
            for i in range(0,len(difficultySeq)):
                tmpDifficulty = str(difficultySeq[i])
                tmpResponseLine = str(gateLineSeq[i])
                tmpIsSelected = str(selectedCarSeq[i])
                tmpUnselectedNumber = str(unselectedNumberSeq[i])
                print("# ResponseIndex = " + str(i) + " ("+tfsStr[i]+","+tmpDifficulty+","+tmpResponseLine+","+tmpIsSelected+","+tmpUnselectedNumber+")")            
            print( "# The number of lines = " + str(len(lineNameList)) + " (Text,Color)" )

            for i in range(0,len(lineNameList)):
                tmpLineName = ""
                match lineNameList[i]:
                    case 0:
                        tmpLineName = "B" #Blue

                    case 1:
                        tmpLineName = "R" #Red

                    case 2:
                        tmpLineName = "Y" #Yellow

                    case 3:
                        tmpLineName = "G" #Green

                tmpLineColor = ""
                match lineColorList[i]:
                    case 0:
                        tmpLineColor = "B" #Blue

                    case 1:
                        tmpLineColor = "R" #Red

                    case 2:
                        tmpLineColor = "Y" #Yellow

                    case 3:
                        tmpLineColor = "G" #Green

                if (HighwayDecoding.getIsBlack(Level) == 1 and tmpLineColor == "G"):
                    tmpLineColor = "D" #Dark

                print("# LineIndex = " + str(i) + " (" + tmpLineName + "," + tmpLineColor + ")")

            print( "# The number of cars = " + str(len(carNameList)) + " (Text,Color,Line)" )

            for i in range(0,len(carNameList)):
                tmpCarName = ""
                match carNameList[i]:
                    case 0:
                        tmpCarName = "B" #Blue

                    case 1:
                        tmpCarName = "R" #Red

                    case 2:
                        tmpCarName = "Y" #Yellow

                    case 3:
                        tmpCarName ="G" #Green

                tmpCarColor = ""   
                match carColorList[i]:
                    case 0:
                        tmpCarColor = "B" #Blue

                    case 1:
                        tmpCarColor = "R" #Red

                    case 2:
                        tmpCarColor = "Y" #Yellow

                    case 3:
                        tmpCarColor ="G" #Green   

                tmpCarLine = str(carLineList[i])

                print("# CarIndex = " + str(i) + " (" + tmpCarName + "," + tmpCarColor + "," + tmpCarLine + ")")

        else:
            print( "DATA has a problem!" )  

                          
