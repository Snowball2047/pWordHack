import random

def openFiles():
    questionsIn = open('TestQuestions2.txt', 'r')
    return questionsIn

def closeFiles(questionsIn):
    questionsIn.close()

def checkNumberInput(lowest, highest, inpMessage):
    userInput = input(inpMessage)
    while not userInput.isdigit():
        print('Should be a number')
        userInput = input(inpMessage)
    inpNumber = int(userInput)
    while not inpNumber in range(lowest, highest+1):
        print('Invalid (should be ', lowest, ' to ', highest,')')
        userInput = input(inpMessage)
        if userInput.isdigit():
            inpNumber = int(userInput)
    return(inpNumber)

def createQuestionList(questionsIn):
    thisQuestion = []
    allQuestions = []
    lineNum = 0
    questionNum = 0
    answers = []
    for line in questionsIn:
        currField=str(line[:-1])                             
        if lineNum % 5 == 0:
            if len(thisQuestion) > 0:
                allQuestions.append([thisQuestion, answers])      
            questionNum = questionNum + 1
            thisQuestion=[questionNum, currField]
            answers = []
        else:
            if len(currField) > 0:
                answers.append([lineNum % 5, currField])
        lineNum = lineNum + 1
    
    allQuestions.append([thisQuestion, answers])
    return(allQuestions)

def runQuiz(shuffledQuestions, numQuestions):
    correct = 0
    for i in range(numQuestions):
        overall = shuffledQuestions[i]
        question = overall[0]
        answers = overall[1]
        answer = answers[0]
        answers = random.sample(answers, len(answers))
        print(question[1])
        for i in range(len(answers)):
            posAnswer = answers[i]
            print(str(i+1) + ', ' + posAnswer[1])
        userA = checkNumberInput(1,len(answers), '\nAnswer?\n')
        userAnswer = answers[int(userA)-1]
        if userAnswer == answer:
            print('Correct!\n')
            correct += 1
        else:
            print('\nIncorrect! The answer was...', answer[1],'\n')
    return(correct)


runAQuiz = 'Y'
while runAQuiz.upper() == 'Y':            
    questionsIn = openFiles()
    allQuestions = createQuestionList(questionsIn)
    closeFiles(questionsIn)
    shuffledQuestions = random.sample(allQuestions, len(allQuestions))
    runAQuiz = 'n'
    numQuestions = checkNumberInput(1, allQuestions[-1][0][0],'How many questions?\n')
    print('')
    numCorrect = runQuiz(shuffledQuestions, numQuestions)
    percent = int(100*numCorrect/numQuestions)
    print('\nPercentage correct = ', percent, '%')
    closeFiles(questionsIn)
    runAQuiz = input('\nRun again? (y/n)\n')
