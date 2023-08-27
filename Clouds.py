import Coding

class CloudsDecoding(Coding.CodingFactory):
    ## according to the coding algorithm, the required lists are defined:
    listHds = [] # the list for each character of HDS
    listHds.append(Coding.CodingVariable(31)) # for the cloud index

    listChd1 = [] # the list for the first character of CHD
    listChd1.append(Coding.CodingVariable(4)) # for the difficulty
    listChd1.append(Coding.CodingVariable(4)) # for the distractor

    listChd2 = [] # the list for the other characters of CHD
    listChd2.append(Coding.CodingVariable(4)) # for the cloud area
    listChd2.append(Coding.CodingVariable(2)) # for the cloud type

    def Decoding (tempStr1):
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

        TFSeq = []
        RTSeq = []
        selectedCloudIndexSeq = []
        difficultyData = []
        distractorData = []
        cloudsAreaSeq = []
        cloudsTypeSeq = []

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
                Coding.CodingFactory.breakingVariables(c,CloudsDecoding.listHds)
                selectedCloudIndexSeq.append(CloudsDecoding.listHds[0].x)

        if (len(chdStr)>0):
            for i in range(0,len(chdStr)):
                c = chdStr[i]
                if (i == 0):
                    Coding.CodingFactory.breakingVariables(c,CloudsDecoding.listChd1)
                    difficultyData.append(CloudsDecoding.listChd1[0].x)
                    distractorData.append(CloudsDecoding.listChd1[1].x)
                else:
                    Coding.CodingFactory.breakingVariables(c,CloudsDecoding.listChd2)
                    cloudsAreaSeq.append(CloudsDecoding.listChd2[0].x)
                    cloudsTypeSeq.append(CloudsDecoding.listChd2[1].x)


        if ( (len(TFSeq) > 0) and (len(TFSeq) == len(selectedCloudIndexSeq)) and (len(TFSeq) == len(RTSeq)) ):

            TN = TFSeq.count(1)
            TF = TFSeq.count(0)
                
            TA0 = 0
            TA1 = 0
            TA2 = 0
            TA3 = 0
            FA0 = 0
            FA1 = 0
            FA2 = 0
            FA3 = 0
            for i in range(0,len(cloudsAreaSeq)):
                if (cloudsTypeSeq[i] == 1 and cloudsAreaSeq[i] == 0):
                    TA0 = TA0 + 1
                elif (cloudsTypeSeq[i] == 1 and cloudsAreaSeq[i] == 1):
                    TA1 = TA1 + 1
                elif (cloudsTypeSeq[i] == 1 and cloudsAreaSeq[i] == 2):
                    TA2 = TA2 + 1
                elif (cloudsTypeSeq[i] == 1 and cloudsAreaSeq[i] == 3):
                    TA3 = TA3 + 1
                elif (cloudsTypeSeq[i] == 0 and cloudsAreaSeq[i] == 0):
                    FA0 = FA0 + 1
                elif (cloudsTypeSeq[i] == 0 and cloudsAreaSeq[i] == 1):
                    FA1 = FA1 + 1
                elif (cloudsTypeSeq[i] == 0 and cloudsAreaSeq[i] == 2):
                    FA2 = FA2 + 1
                elif (cloudsTypeSeq[i] == 0 and cloudsAreaSeq[i] == 3):
                    FA3 = FA3 + 1

            STRCA = ""    
            TC0 = 0
            TC1 = 0
            TC2 = 0
            TC3 = 0
            FC0 = 0
            FC1 = 0
            FC2 = 0
            FC3 = 0
            for i in range(0,len(TFSeq)):
                iC = selectedCloudIndexSeq[i]
                CT = cloudsTypeSeq[iC]
                CA = cloudsAreaSeq[iC]
                if (TFSeq[i] != CT):
                    print("ERR: " + str(TFSeq[i]) + "," + str(CT))
                else:
                    if (CT == 1 and CA == 0):
                        TC0 = TC0 + 1
                        STRCA = STRCA + "A0(T),"
                    elif (CT == 1 and CA == 1):
                        TC1 = TC1 + 1
                        STRCA = STRCA + "A1(T),"
                    elif (CT == 1 and CA == 2):
                        TC2 = TC2 + 1
                        STRCA = STRCA + "A2(T),"
                    elif (CT == 1 and CA == 3):
                        TC3 = TC3 + 1
                        STRCA = STRCA + "A3(T),"
                    elif (CT == 0 and CA == 0):
                        FC0 = FC0 + 1
                        STRCA = STRCA + "A0(F),"
                    elif (CT == 0 and CA == 1):
                        FC1 = FC1 + 1
                        STRCA = STRCA + "A1(F),"
                    elif (CT == 0 and CA == 2):
                        FC2 = FC2 + 1
                        STRCA = STRCA + "A2(F),"
                    elif (CT == 0 and CA == 3):
                        FC3 = FC3 + 1
                        STRCA = STRCA + "A3(F),"
                        
            print( "In this trial, we have:" )
            print( "# The difficulty type = " + str(difficultyData) )
            print( "# The distractor type = " + str(distractorData) )
            print( "# The number of true/false responses = " + str(TN) + "/" + str(TF) )
            print( "# The number of clouds = " + str(len(cloudsTypeSeq)) )
            print( "# The number of rainy/non-rainy clouds in Area0 = " + str(TA0) + "/" + str(FA0) )
            print( "# The number of rainy/non-rainy clouds in Area1 = " + str(TA1) + "/" + str(FA1) )
            print( "# The number of rainy/non-rainy clouds in Area2 = " + str(TA2) + "/" + str(FA2) )
            print( "# The number of rainy/non-rainy clouds in Area3 = "+ str(TA3) + "/" + str(FA3) )
            print( "# The number of selected rainy/non-rainy clouds in Area0 = " + str(TC0) + "/" + str(FC0) )
            print( "# The number of selected rainy/non-rainy clouds in Area1 = " + str(TC1) + "/" + str(FC1) )
            print( "# The number of selected rainy/non-rainy clouds in Area2 = " + str(TC2) + "/" + str(FC2) )
            print( "# The number of selected rainy/non-rainy clouds in Area3 = " + str(TC3) + "/" + str(FC3) )
            print( '# Responses in the areas: ' + STRCA)
        else:
            print("DATA has a problem!")                    
