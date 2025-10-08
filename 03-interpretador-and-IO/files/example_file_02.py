import sys 
# this program is to demonstrate the stdin (input), stdout (output), stderr (except) and exi
def main():
    try: 
        print("Welcome to the program!")
        user_input = input("Do you want to exit the program? (y/n): ")
        if user_input.lower() == "yes" or "y":
            exit_program()
    

    except Exception as e:
        print(f"An error ocurred: {e}")
        exit_program()



def exit_program():
    print("Exiting the program ...")
    sys.exit(1)

if __name__ == "__main__":
    main()