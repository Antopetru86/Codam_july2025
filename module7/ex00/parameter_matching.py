#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("None")
        return

    parameter = sys.argv[1]
    user_input = input("What was the parameter? ").strip()

    if user_input == parameter:
        print("Good job!")
    else:  
        print("No, sorry...")

if __name__ == "__main__":
    main()







#else: 
    #text= parameter[1] #define text in which keyword is looked for
    #matchword = re.findall(key,text)  #key = pattern #text
    #if len(matchword)==0:
        #print("none")
    #else:
        #print(len(matchword)) 
#!/usr/bin/env python3



