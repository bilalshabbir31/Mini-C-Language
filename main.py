## Main Code.
from AcceptingState import AcceptingStates
from Keyword import Keywords
from LexicalAnalyzer import LexicalAnalyzer
from Parser import LL1Parser
from Sigma import Sigma
from Tokens import Token
from TransitionTable import TransitionTable




S=Sigma()
Sigma=S.getSigma()
T=Token()
Tokens=T.getTokens()
Transition_table=TransitionTable()
TT=Transition_table.getTransitionTable()
AS=AcceptingStates()
AcceptingState=AS.getAcceptingStates()
Kw=Keywords()
keyword=Kw.getKeyword()

Lex=LexicalAnalyzer(Sigma,AcceptingState,Tokens,TT,keyword)
print(f'                                   Lexical Analyzer. ')
print('*******************************************************************************************')


# sample input for Tokenizer

#Tn=Lex.Tokenizer("void main(){a=6;}")
#Tn=Lex.Tokenizer("void main(){int a;}")
#Tn=Lex.Tokenizer("void main(){a=b+c;}")
Tn=Lex.Tokenizer("void main(){a=b*c;}")
#Tn=Lex.Tokenizer("abc")     #invalid input String is not Valid
print(f'Tokens: {Tn}')
print(f'*******************************************************************************************')
l=[]

for key,val in Tn.items():
    if val=="Keyword":
        l.append(key)
    elif val=="intliteral":
        l.append(val)
    else:
        l.append(val)

l.append("$")


### LL1 Parsing
print(f'                                   LL(1) Parser. ')
print('*******************************************************************************************')

LL=LL1Parser()
LL.Parsing(l)

