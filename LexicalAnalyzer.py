# Here First we Create a Class of Lexical Analyzer.


class LexicalAnalyzer:

    # Overloaded Contructor.
    def __init__(self, Sigma, acceptingState, Tokens, TT, kw):  # Constructor
        self.Sigma = Sigma
        self.acceptingState = acceptingState
        self.Token = Tokens
        self.TT = TT
        self.kw = kw
        self.hashtable = {}

    def Tokenizer(self, input):
        state = 0
        charinput = input

        i = 0
        key = ''
        while i < len(charinput):
            ind = self.getIndex(charinput[i])
            state = self.TT[state][ind]

            acc = self.checkAccepting(state, self.acceptingState)
            key += charinput[i]
            if key[0] == "{" and charinput[1 + i] != "}":
                self.hashtable[charinput[i]] = "{"

                key = ''
                state = 0

            elif charinput[i] == "}":
                for val in key:
                    if val == "}":
                        self.hashtable[charinput[i]] = "}"

                        key = ''
                        state = 0
                        break
            elif key[0] == "(":
                if charinput[i + 1] != ")":
                    self.hashtable[charinput[i]] = "("
                elif charinput[i + 1] == ")":
                    self.hashtable[charinput[i]] = "("
                    self.hashtable[charinput[i + 1]] = ")"
                    i = i + 1
                key = ''
                state = 0

            elif charinput[i] == ")":
                if key[0] != ")":
                    self.hashtable[key[0]] = self.printToken(state, self.Token, self.kw, key[:-1])

                for val in key:
                    if val == ")":
                        self.hashtable[charinput[i]] = ")"

                        acc = ""
                        key = ''
                        state = 0
                        i = i + 1
                        break

            if acc == 'y':
                i = i - 1
                self.hashtable[key[:-1].strip()] = self.printToken(state, self.Token, self.kw, key[:-1])

                state = 0
                k = 0
                key = ''


            elif acc == 'n':
                self.hashtable[key.strip()] = self.printToken(state, self.Token, self.kw, key)

                state = 0
                key = ''

            i = i + 1

        return self.hashtable  # returning Tokens

    def getIndex(self, ch):
        i = 0
        if 'A' <= ch <= 'Z':
            return 0
        elif 'a' <= ch <= 'z':
            return 0
        elif '0' <= ch <= '9':
            return 1
        elif ch == '=':
            return 2
        elif ch == '+':
            return 3
        elif ch == '{':
            return 4
        elif ch == '}':
            return 5
        elif ch == '(':
            return 6
        elif ch == ')':
            return 7
        elif ch == ';':
            return 8
        elif ch == ',':
            return 9
        elif ch == '*':
            return 10
        elif ch == '<':
            return 11
        elif ch == '>':
            return 12
        elif ch == ' ' or ch == '\n' or ch == '\t':
            return 13

        return -1

    def key_or_id(self, keyword, k):
        if k[0] == " ":
            k = k[1:]
        g = ''
        for i in k:
            if i != ' ' and i != '\0':
                g += i
            else:
                break

        flag = False
        j = 0
        while j < len(keyword):
            if keyword[j] == g:
                flag = True
                break
            j = j + 1

        if flag:
            return "Keyword"
        elif not flag:
            return "id"

    def checkAccepting(self, state, acceptingState):
        return acceptingState[state]

    def printToken(self, state, Token, k, ky):
        if state == 2 and Token[state] == "id":
            return self.key_or_id(k, ky)
        else:
            return self.Token[state]
