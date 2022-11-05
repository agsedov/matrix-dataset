import random
import math
import json

class Matrix:
    def __init__(self, seed, page):
        self.page = page
        random.seed(seed)
        r1 = random.random()
        if(r1<=0.35):
            self.matrixType = 'regular'
        elif(r1<=0.7):
            self.matrixType = 'sle'
        else:
            self.matrixType = 'determinant'

        r2 = random.random()

        self.chooseSize()

        self.data = [[0]*self.n for i in range(self.m)]
        for i in range(0,self.m):
            for j in range(0,self.n):
                if(r2<=0.1):
                    self.data[i][j] = math.floor(random.random()*1999 - 999)
                elif(r2<=0.5):
                    self.data[i][j] = math.floor(random.random()*199 - 99)
                else:
                    self.data[i][j] = math.floor(random.random()*19 - 9)

    def regularMatrixMN(self):
        r = random.random()
        if(r<=0.4):
            return 2
        if(r<=0.7):
            return 3
        if(r<=0.9):
            return 4
        return 5

    def chooseSize(self):
        r = random.random()
        if(self.matrixType == 'regular'):
            self.m = self.regularMatrixMN()
            self.n = self.regularMatrixMN()
            return
        if(self.matrixType == 'sle'):
            self.n = math.floor(random.random()*4)+3
            self.m = math.floor(random.random()*(self.n-2))+2
        if(self.matrixType == 'determinant'):
            self.m = math.floor(random.random()*3)+2
            self.n = self.m

    def texFormat(self):
        resultString = ""
        braceL = "\\left(\n"
        braceR = "\\right)\n"
        if(self.matrixType == "determinant"):
            braceL = "\\left|\n"
            braceR = "\\right|\n"

        resultString = braceL

        if(self.matrixType == "sle"):
            resultString += "\\begin{array}{"+"c"*(self.n-1)+"|c}\n"
        else:
            resultString += "\\begin{array}{"+"c"*self.n+"}\n"

        for i in range(0,self.m):
            resultString += " & ".join([str(num) for num in self.data[i]])
            resultString += "\\\\\n"
        resultString += "\\end{array}\n"
        resultString += braceR
        return resultString

matrices = []
matricesData = []
matricesTex = ""
for p in range(1,300):
    for e in range(0,10):
        m = Matrix(p*10+e, p)
        matrices.append(m)
        matricesData.append(m.__dict__)
        matricesTex += " $" + m.texFormat()+ "$ \n"
        if(e==1 or e==3 or e==5 or e==7):
            matricesTex += "\\vfill\n"
        else:
            matricesTex += "\\hspace{\\fill}\n"
    matricesTex+="\\newpage\n"
with open('./generator/matrices.tex', 'w') as f:
    f.write(matricesTex)

with open("./generator/matrices.json", "w") as f:
    json.dump(matricesData, f, indent = 6)

