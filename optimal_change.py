def optimal_change(item_cost, amount_paid):
    if item_cost > amount_paid:
        return "Error: please provide sufficient payment." # to handle underpayment
    elif item_cost == amount_paid:
        return f"For an item that costs ${item_cost} with an amount paid of ${amount_paid}, there is no change required." # to handle exact payment
    else:
        change_owed = int((amount_paid * 100) - (item_cost * 100)) # to return the difference in pennies, and make sure it's an int
        answer_prefix = f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
        answer = ""
        final_answer = ""
        
        change_to_be_returned = []

        # dictionary of the bills and coins in the USD cash circulation
        # I went in the direction to use total pennies, so one dollar is 100 pennies
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

        # this while loop gives the bills/coins I'll need
        while change_owed > 0:
            for i in register:
                if change_owed // register[i] >= 1:
                    change_to_be_returned.append(i)
                    change_owed -= register[i]
                    break
            
        

        # this dictionary comprehension gives me a dictionary with the coins I'll need 
        # and the numbers of those coins 
        number_of_each_coin = {i: change_to_be_returned.count(i) for i in register if change_to_be_returned.count(i) > 0}

        # the frontend part. giving the appropriate string to handle plurality 
        # my least favorite part🤮

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

        # I wish I could have made that loop more concise. Unfortunately the question had too many 
        # different possibilities. Bill(s) vs quarter(s) vs dime(s) vs nickel(s) vs penny vs pennies
                
        

        # to take away the commas after each bill/coin if there's no pennies in 
        # the change
        if "penn" not in answer:
            answer = answer[:-2]

        final_answer = answer_prefix + answer + "."
            
        
        return final_answer

