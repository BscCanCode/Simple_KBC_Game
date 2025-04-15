import sys
def fun():
    try:
        print("Welcome to KBC(KAUN BANEGA CROREPATI)!!!")
        print("You will be Answering 5 questions,be ready and All the best from Team KBC!")
        question=("Largest country in the world?")
        print(question)
        option=("1.Russia\n2.China\n3.USA\n4.CANADA")
        print(option)
        answer=int(input("Enter your answer between 1-4:"))
        if 0<answer<=4:
            if answer==1:
                print("Russia is the correct answer!")
                print("You won Rs.10000")
                print("------------------------------------")
            else:
                print("Unfortunately! Answer is incorrect")
                print("You won Rs.0")
                sys.exit()
        #Another question!
            question=("2.Who is the Prime Minister of India?")
            print(question)
            option=("1.Narendra_Modi\n2.Rahul_Gandhi\n3.Amit_Shah\n4.Eknath_Shinde")
            print(option)
            answer=int(input("Enter your answer between 1-4:"))
            if answer==1:
                print("Narendra Modi is the correct answer!")
                print("You won Rs.20000")
                print("-----------------------------------------------")
            else:
                print("Unfortunately! Answer is incorrect")
                print("The total amount you won is Rs.10000")
                sys.exit()
                #3rd Question
            question=("3.Which city is known as capital of India?")
            print(question)
            option=("1.Chennai\n2.New_Delhi\n3.Kolkata\n4.Hyderabad")
            print(option)
            answer=int(input("Enter your answer between 1-4:"))
            if answer==2:
                print("New_Delhi is the correct answer!")
                print("You won Rs.30000")
                print("-------------------------------------------------")
            else:
                print("Unfortunately! Answer is incorrect\nThe correct answer is New_Delhi")
                print("You will get money prize for the correct answers given before!")
                print("The total amount you won is:Rs.30000")
                sys.exit()
                  #4th Question
            question=("4.Largest Continent in the world?")
            print(question)
            option=("1.Australia\n2.Africa\n3.Europe\n4.Asia")
            print(option)
            answer=int(input("Enter your answer between 1-4:"))
            if answer==4:
                print("Asia is the correct answer!")
                print("You won Rs.40000")
                print("-------------------------------------------------------")
            else:
                print("Unfortunately! Answer is incorrect\nThe correct answer is Asia")
                print("You will get money prize for the correct answers given before!")
                print("The total amount you won is:Rs.60000")
                sys.exit()
            #5th Question
            question=("5.How many wheels do Auto-Rickshaw a Public Transport vehicle in MUMBAI has?")
            print(question)
            option=("1.Five_Wheels\n2.Four_Wheels\n3.Three_Wheels\n4.One_wheels")
            print(option)
            answer=int(input("Enter your answer between 1-4:"))
            if answer==3:
                print("Three_Wheels is the correct answer!")
                print("You won Rs.50000")
                print("---------------------------------------------------")
            else:
                print("Unfortunately! Answer is incorrect\nThe correct answer is Three_Wheels")
                print("You will get money prize for the correct answers given before!")
                print("The total amount you won is:Rs.100000")
                sys.exit()
            print("As you have answered all the questions correctly\nThe prize money you won for answering all the question correct is Rs.150000!!")
            print("Congratulations from Team KBC on winning such a Huge Amount!")
        else:
            print(f"{answer} is not valid and not listed,enter between 1-4!")
            print("You won Rs.0, to win you should enter  your answer between 1-4!")
        
    except ValueError:
        print("Only int values are accepted")
        print("You won Rs.0, to win you should enter your answer between 1-4!")
        sys.exit()
        
fun()
