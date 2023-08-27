class CodingVariable:
    def __init__(self, _xStates):
        self.xStates = max(min(_xStates, 64), 1)
        self._xBitNumber = 0
        while pow(2, self._xBitNumber) < self.xStates:
            self._xBitNumber += 1
        self._x = 0

    @property
    def xBitNumber(self):
        return self._xBitNumber

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = max(min(value, self.xStates - 1), 0)

    @property
    def xToBinary(self):
        return bin(self._x)[2:].zfill(self._xBitNumber)
    
class CodingFactory:
    def patchingVariables(_variables):
        _data = ""
        for i in range(len(_variables)):
            _data += _variables[i].xToBinary
        return CodingFactory.convertBinToChar(_data)
    
    def convertBinToChar(binData):
        if len(binData) > 6 or len(binData) < 1:
            print("convertBinToChar: Error1!")
            return chr(0)
        while len(binData) < 8:
            binData = "0" + binData
        data = 0
        for i in range(8):
            data |= (int(binData[i] == '1') << (7 - i))
        b1 = ord('0')
        b2 = ord('A')
        b3 = ord('a')
        b4 = ord('#')
        if data < 10:
            return chr(b1 + data)
        elif data < 36:
            return chr(b2 + (data - 10))
        elif data < 62:
            return chr(b3 + (data - 36))
        else:
            return chr(b4 + (data - 62))
    
    def breakingVariables(charData, _variables):
        BinData = CodingFactory.convertCharToBin(charData)
        headI = 8 - _variables[len(_variables)-1].xBitNumber
        for i in range(len(_variables) - 1, -1, -1):
            binData = BinData[headI:(headI + _variables[i].xBitNumber)]
            while len(binData) < 8:
                binData = "0" + binData
            data = 0
            for j in range(8):
                if (binData[j] == '1'):
                    tempV = 1
                else:
                    tempV = 0
                data |= tempV << (7 - j)
            _variables[i].x = data
            if i != 0:
                headI -= _variables[i - 1].xBitNumber 

    def convertCharToBin (charData):
        b1 = bytes('0', 'utf-8')[0]
        b2 = bytes('A', 'utf-8')[0]
        b3 = bytes('a', 'utf-8')[0]
        b4 = bytes('#', 'utf-8')[0]

        cchData = bytes(charData, 'utf-8')
        if (len(cchData)>0):
            _chData = cchData[0]
        else:
            print("convertCharToBin: Error1!")
            return "11111111"
        _data = 0

        if (_chData >= b1 and _chData <= b1+9):
            _data = _chData - b1
        elif (_chData >= b2 and _chData <= b2+25):
            _data = (10 + _chData - b2)
        elif (_chData >= b3 and _chData <= b3+25):
            _data = (36 + _chData - b3)
        elif (_chData >= b4 and _chData <= b4+1):    
            _data = (62 + _chData - b4)
        else:
            print("convertCharToBin: Error1!")
            return "11111111"
        
        binData = bin(_data)[2:]
        while (len(binData) < 8):
            binData = "0" + binData

        return binData  
    
##Sample1:
# listInput = []
# listInput.append(CodingVariable(8))
# listInput.append(CodingVariable(2))
# listInput.append(CodingVariable(2))
# listInput[0].x = 5
# listInput[1].x = 0
# listInput[2].x = 1
# tempCInput = CodingFactory.patchingVariables(listInput)
# listOutput = []
# listOutput.append(CodingVariable(8))
# listOutput.append(CodingVariable(2))
# listOutput.append(CodingVariable(2))
# CodingFactory.breakingVariables(tempCInput,listOutput)
# print(listOutput[0].x)
# print(listOutput[1].x)
# print(listOutput[2].x)

##Sample2:
# listHdr = []
# listHdr.append(CodingVariable(31))
# CodingFactory.breakingVariables("A",listHdr)
# print(listHdr[0].x)
# CodingFactory.breakingVariables("B",listHdr)
# print(listHdr[0].x)