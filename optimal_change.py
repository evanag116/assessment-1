def optimal_change(item_cost, amount_paid):
    if item_cost > amount_paid:
        return "Error: please provide sufficient payment."
    elif item_cost == amount_paid:
        return f"For an item that costs ${item_cost} with an amount paid of ${amount_paid}, there is no change required."
    else:
        change_owed = int((amount_paid * 100) - (item_cost * 100))
        
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
            
        


        number_of_each_coin = {i: change_to_be_returned.count(i) for i in register}
        return number_of_each_coin

        # {'hundred': 0, 'fifty': 0, 'twenty': 0, 'ten': 1, 'five': 1, 'one': 3, 'quarter': 1, 'dime': 2, 'nickel': 0, 'penny': 4}
        


        answer_prefix = f"The optimal change for an item that costs ${item_cost} with amount paid of ${amount_paid} is"
        # answer = f"{}"
        # return f"{answer_prefix}{num_of_100s if num_of_100s > 0 else ''} $100 bill{'s' if num_of_100s > 1 else ''}{num_of_50s if num_of_50s > 0 else ''}"
        # return answer_prefix + answer

print(optimal_change(31.51,50))

# "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
# ['ten', 'five', 'one', 'one', 'one', 'quarter', 'dime', 'dime', 'penny', 'penny', 'penny', 'penny']



# bill vs bills
# quarter vs quarters
# dime vs dimes
# penny vs pennies



