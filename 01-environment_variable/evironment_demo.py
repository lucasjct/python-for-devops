#!/usr/bin/env python3

# the sintax above is called SHEBANG. 
# with SHEBANG shell will take in that the script will run with python version 3.
# and we are able to call the script on CLI using this sintax: ./environment_demo.py


# Ways to call the script below:
# Test 1
# python environment_demo.py

# Test 2 
# CUSTOM_VAR=persist python environment_demo.py

# Test 3 
# export CUSTOM_VAR=persist
#./environment_demo.py
# echo "CUSTOM_VAR: $CUSTOM_VAR"

# Test 4 
# 
# python -c "import os; os.environ["NOVA"]=TEST"
# echo "NOVA: $NOVA"




import os

def main():
    print("=== Environment Demonstration ===")

    # Print PID to check the isolation
    print(f"Proccess ID:" {os.getpid()}")

    # Important variables
    for var in ["USER", "PATH", "CUSTOM_VAR"]:
        valor = os.getenv(var, "NÃO DEFINIDA")
        if var == "PATH":
            # Print just the amount of directories
            valor = f"{len(valor.split(":"))} directories"
            print(f"{var}:{valor}")

    # Trying change
    os.environment["TEST"] = "temporary"
    print(f"\nTEST it was defined as: {os.environ["TEST"]}")
    pritn("(but it wont persist when the script finish.)")

if __name__ == "__main__":
    main()
    print()