#imports
import random

# define the main function
def main():
    kind = random.randint(1, 4)
    no1 = None
    no2 = None
    operation_types = ["+", "-"]
    operation_type = random.choice(operation_types)
    type_verification = 0

    # generating the operations
    match kind:
        case 1:
            no1 = random.randint(1, 10)
            no2 = random.randint(1, 10)
        case 2:
            no1 = random.randint(1, 10)
            no2 = random.randint(10, 100)
        case 3:
            no1 = random.randint(10, 100)
            no2 = random.randint(1, 10)
        case 4:
            no1 = random.randint(10, 100)
            no2 = random.randint(10, 100)

    # If the result of the operation is negative, print its swapped version
    # Since my sister hasn't learned negatives yet.
    if eval(f"{no1} {operation_type} {no2}") < 0:
        print(f"{no2} {operation_type} {no1} =") # Display the swapped operation
        type_verification = 0 # Mark that the operation was swapped

    # if the operation doesn't have a negative result, print it as-is
    else:
        print(f"{no1} {operation_type} {no2} =") # Display the operation
        type_verification = 1 # Mark that the operation wasn't swapped

    # keep asking for answer until right answer is given
    while True:
        user_input = input("Answer: ") # get the answer of the user
        if user_input.isdigit(): # verification that the answer is a number
            answer = int(user_input) # make the answer into an integer (not just text)

            # if the operation was swapped, define that good answer as such
            if type_verification == 0:
                good_answer = eval(f"{no2} {operation_type} {no1}")

            # if the operation wasn't swapped, define the good answer a such
            else:
                good_answer = eval(f"{no1} {operation_type} {no2}")

            if answer == good_answer: # if the given answer is good, print that it's good and cut the program
                print("Good answer!😃")
                break
            else: # if the given answer is bad, print that it's bad and ask for it again
                print("Bad answer😰")
        else: # if the answer wasn't a number
            print("The answer is supposed to be a number")

# run the function
main()
