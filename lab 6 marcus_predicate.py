import nltk
from nltk import logic
from nltk.inference import ResolutionProver

def main():
    lp = logic.LogicParser()
    print("Enter the number of premises:")
    num_premises = int(input())
    premises = []
    print("Enter each premise:")
    for i in range(num_premises):
        premise_input = input(f"Premise {i+1}: ")
        premises.append(lp.parse(premise_input))
    print("Enter the goal:")
    goal_input = input()
    goal = lp.parse(goal_input)
    print("\nPremises:")
    for p in premises:
        print(" ", p)
    print("\nGoal:")
    print(" ", goal)
    prover = ResolutionProver()
    if prover.prove(goal, premises):
        print("\nThe goal is proven.")
    else:
        print("\nThe goal could not be proven.")

if __name__ == "__main__":
    main()