import pandas as pd
import xlrd
import openpyxl


class LL1Parser:
    top = 0

    def __init__(self):
        self.table = pd.read_excel('Parse Table.xlsx')
        self.stack = []

    def getNonterminals(self):
        return self.table["NT"].values.tolist()

    def getTerminals(self):
        return self.table.columns[1:].tolist()

    def reverse(self, str):
        return str[::-1]

    def isValid(self):
        print(f'String is Valid. ')

    def isNotValid(self):
        print(f'String is Not Valid')

    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        self.top = self.top - 1
        return self.stack.pop()

    def getProduction(self, row, column):
        return self.table.iloc[row, column + 1]

    def Parsing(self, Token):
        print(f'Input String:{Token}')
        if Token[0] != "void":
            self.isNotValid()
            exit(1)
        self.push('$')  # Pushing $ sign into the Stack.
        self.push(self.getNonterminals()[0])  # Pushing Starting Symbol'
        print(self.stack)
        print("***********************************************************")
        i = 0
        length = len(Token)
        while i < length:
            pop = self.stack.pop()
            print(f'Poped Value: {pop} ')
            print(f'Comparsion b/w Stack Pop Value: {pop}, with Token: {Token[i]}')

            if pop == "$" and Token[i] == "$":
                self.isValid()
                break

            if pop == "^":
                print("Discard Null Production")

            elif pop == Token[i]:
                print(f'Match: {pop} == {Token[i]}')
                i = i + 1
            elif pop != Token[i]:
                row = self.getNonterminals().index(pop)
                column = self.getTerminals().index(Token[i])
                z = []
                z.append(self.getProduction(row, column))
                production = z[0].split(" ")
                re = self.reverse(production)
                for j in re:
                    self.push(j)
                print(f'Production Pushed: {self.stack}')
