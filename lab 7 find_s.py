def find_s(examples):
    hypothesis = ['0'] * len(examples[0][0])
    for example, label in examples:
        if label == 1:
            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = example[i]
                elif hypothesis[i] != example[i]:
                    hypothesis[i] = '?'
    return hypothesis

def main():
    print("🧠 Find-S Algorithm - Console Version\n")
    
    n = int(input("Enter number of attributes: "))
    attribute_names = []
    for i in range(n):
        name = input(f"Enter name of attribute {i+1}: ")
        attribute_names.append(name)
    
    examples = []
    while True:
        print("\nEnter attribute values for an example:")
        values = [input(f"{attribute_names[i]}: ") for i in range(n)]
        
        label = input("Label (1 for Positive, 0 for Negative): ")
        try:
            label = int(label)
            if label not in [0, 1]:
                raise ValueError
        except:
            print("Invalid label. Please enter 1 or 0.")
            continue
        
        examples.append((values, label))
        
        cont = input("Add another example? (y/n): ").lower()
        if cont != 'y':
            break

    hypothesis = find_s(examples)
    print("\n✅ Final Hypothesis:")
    for i in range(n):
        print(f"{attribute_names[i]}: {hypothesis[i]}")

if __name__ == "__main__":
    main()
