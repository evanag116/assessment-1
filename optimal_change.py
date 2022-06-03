def optimal_change(item_cost, amount_paid):
    if item_cost > amount_paid:
        return "Error: please provide sufficient payment."
    elif item_cost == amount_paid:
        return f"For an item that costs ${item_cost} with an amount paid of ${amount_paid}, there is no change required."
    else:
        change_owed = int((amount_paid * 100) - (item_cost * 100))
        answer_prefix = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
        answer = ""
        
        change_to_be_returned = []
        register = {
            "hundred": 10000,
            "fifty": 5000,
            "twenty": 2000,
            "ten": 1000,
            "five": 500,
            "one": 100,
            "quarter": 25,
            "dime": 10,
            "nickel": 5,
            "penny": 1,
        }

        while change_owed > 0:
            for i in register:
                if change_owed // register[i] >= 1:
                    change_to_be_returned.append(i)
                    change_owed -= register[i]
                    break
            
        


        number_of_each_coin = {i: change_to_be_returned.count(i) for i in register if change_to_be_returned.count(i) > 0}

            
        for i in number_of_each_coin:
            if register[i] >= 100:
                if number_of_each_coin[i] > 1:
                    answer += f"{number_of_each_coin[i]} ${register[i] // 100} bills, "
                else:
                    answer += f"1 ${register[i] // 100} bill, "
            elif register[i] > 1:
                if number_of_each_coin[i] > 1:
                    answer += f"{number_of_each_coin[i]} {i}s, "
                else:
                    answer += f"1 {i}, "
            else:
                if number_of_each_coin[i] > 1:
                    answer += f"and {number_of_each_coin[i]} pennies"
                else:
                    answer += f"and 1 penny"
                
            
        
        return answer_prefix + answer + "."

        



print(optimal_change(9, 10))




# comment your code
# fix last test case

# if register[i] == 25:
                #     if number_of_each_coin[i] > 1:
                #         answer += f"{number_of_each_coin[i]} quarters, "
                #     else:
                #         answer += "1 quarter, "
                # elif register[i] == 10:
                #     if number_of_each_coin[i] > 1:
                #         answer += f"{number_of_each_coin[i]} dimes, "
                #     else:
                #         answer += "1 dime, "
                # elif register[i] == 5:
                #     if number_of_each_coin[i] > 1:
                #         answer += f"{number_of_each_coin[i]} nickels, "
                #     else:
                #         answer += "1 nickel, "
                # elif register[i] == 1:
                #     if number_of_each_coin[i] > 1:
                #         answer += f"and {number_of_each_coin[i]} pennies."
                #     else:
                #         answer += "and 1 penny."
