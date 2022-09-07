
class wordGame:
    def __init__(self, inputCommandList):
        self.wordList = []
        self.inputCommandList = inputCommandList

    def game(self):
        wordTemp = ""
        inputCommandList = self.inputCommandList
        checkInputCommand = 0
        checkWord = 0
        countGame = 0
        wordList = self.wordList
        for i in range(0, len(inputCommandList)):
            checkCase = self.checkInputCommand(inputCommandList[i])
            if (checkCase == 1):
                wordTemp = inputCommandList[i].split(" ", 1)[1]
                if (len(wordList) >= 1):
                    if (self.checkWord(wordList[countGame], wordTemp) == 1):
                        wordList.append(wordTemp)
                        print("'"+wordTemp+"'"  + " -> ",end="")
                        print(wordList)
                        countGame += 1
                    else:
                        print("'"+wordTemp+"'" + " -> "+"game over")
                        break
                else:
                    wordList.append(wordTemp)
                    print("'"+wordTemp+"'" + " -> ",end="")
                    print(wordList)
            elif (checkCase == 2):
                wordList.clear()
                countGame = 0
                print("game restarted")
            elif (checkCase == 3):
                break
            elif (checkCase == 4):
                print("'"+self.inputCommandList[i]+"'" + " is Invalid Input !!!")
                break

    def checkInputCommand(self, inputCommand):
        if (inputCommand[0] == "P"):
            return 1
        elif (inputCommand[0] == "R"):
            return 2
        elif (inputCommand[0] == "X"):
            return 3
        else:
            return 4

    def checkWord(self, word1, word2):
        wordLength1 = len(word1)
        wc1A = word1[wordLength1 - 2]
        wc2A = word1[wordLength1 - 1]
        wc1B = word2[0]
        wc2B =word2[1]
        if (wc1A.lower() == wc1B.lower() and wc2A.lower() == wc2B.lower()):
            return 1
        else:
            return 0


print("*** TorKham HanSaa ***")
inputCommandList = list(input("Enter Input : ").split(","))
wordgame = wordGame(inputCommandList)
wordgame.game()
