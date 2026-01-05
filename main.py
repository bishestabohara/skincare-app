print("Skincare Checklist App")
choose =" "
while choose !="morning" and choose !="night":
    choose = input("Pick Morning or Night: ").lower()

    if choose == "morning":
        print("Step 1: Serum")
        answer =" "
        while answer !="y":
            answer = input("Did you do serum?(y/n):").lower()
            if answer == "n":
                print("Apply serum")
            else:
                print("answer not applicable")
        print("Step 1 complete")
        print("step 2: moisturizer")

        answer= " "
        while answer !="y":
            answer = input("Did you apply moisturizer?(y/n):").lower()
            if answer == "n":
                print ("apply moisturizer")
            else:
                print("answer not applicable")
        print("step 2 complete")
        print("step 3: Sunscreen")

        answer=" " 
        while answer !="y":
            answer = input("Did you apply sunscren?(y/n):").lower()
            if answer =="n":
                print("go back and apply sunscreen")
            else:
                print("answer not applicable")
        print("Morning Skincare routine completed")

            

        


    elif choose == "night":
        print("Step 1: Serum")
        answer = input("Did you do serum?(y/n):").lower()
        if answer == "y":
            print("Step 1 complete")
            print("step 2: moisturizer")

            answer = input("Did you apply moisturizer?(y/n):").lower()
            if answer == "y":
                print("Nighttime Skincare routine complete")
            elif answer == "n":
                print ("apply moisturizer")
            else:
                print("answer not applicable")

        elif answer == "n":
            print("Apply serum")
        else:
            print("answer not applicable")

    else:
        print("Pick Morning or Night")



    
    


