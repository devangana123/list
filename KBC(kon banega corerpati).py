question_list = [
    "1) How many continents are there?",           
    "2) What is the capital of India?",
    "3) NG mei kaun se course padhaya jaata hai?",
    "4) What is the capital of maharashtra?",
    "5) What is the capital of MP?",
    "6) What is the national language  india?"
]
options_list = [
    ["1) Four", "2) Nine", "3) Seven", "4) Eight","5) Lifeline-5050\n"],
    ["1) Chandigarh", "2) Bhopal", "3) Chennai", "4) Delhi","5) Lifeline-5050\n"],
    ["1) Software Engineering", "2) Counseling", "3) Tourism", "4) Agriculture","5) Lifeline-5050\n"],
    ["1) Nagpur", "2) Mumbai", "3) Bhopal", "4) Amritsar", "5) Lifeline-5050\n"],
    ["1) Delhi", "2) Chennai", "3) Mumbai", "4) Bhopal","5) Lifeline-5050\n"],
    ["1) Hindi", "2) Telgu", "3) English", "4) Marathi", "5) Lifeline-5050"]
]
solution_list = [ 3, 4, 1, 2, 4, 1]
fifty50=["1) Four\n2) Sevan","1) Bhopal\n2) Delhi","1) Tourism\n2) Software Engineering","1) Amritsar\n2) Mumbai","1) Delhi\n2) Bhopal","1) English\n2) Hindi"]
name=input("Enter Your Name :- ")
print("\n       ✽✽✽✽✽✽✽✽--|| HeLLO MR",name,"||--✽✽✽✽✽","\n✽✽✽✽✽---|| WELCOME TO KON BANEGA KAROROATI GAME ||---✽✽✽✽✽\n             ✽✽✽✽✽✽✽✽✽✽-----KBC-----✽✽✽✽✽✽✽✽✽✽\n")
a=0
b=0
c=1
ll=2
cash=10000
while a < len(question_list):
    print("✽✽✽✽✽✽✽---|| Ye Raha Aapka Question No :-",c,"RS",cash,"Ke Liye ||---✽✽✽✽✽✽✽")
    print(question_list[a],"\n")
    ae=1
    for i in options_list[a]:
        print(i)
        ae+=1
    guess=int(input("Enter Yuor Choise :- "))
    if guess == solution_list[a]:
        print("✤✤✤|| SHAHI JAWAB ||✤✤✤\n")
        print("✽✽✽✽✽---AAPNE RS",cash,"JIT LIYA HAI---✽✽✽✽✽")
    elif guess == 5 and b < 1:
        b+=1
        print("Aap 5050 Lifeline Ka Use 1 Hi Bar Kar Sakte Ho")
        print(fifty50[a])
        fif50=int(input("ENTER YOUR ANSWER :- "))
        if fif50 == 2:
            print("✽✽✽✽✽---|| SAHI JAWAB ||---✽✽✽✽✽")
    elif guess == 5 and b < 2:
        print("✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽---|| SORRY ||---✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽")
        print("✽✽✽--|| AAPNE 50:50 LIFELINE PAHLE HI USE KI HAI ||--✽✽✽")
        print("✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽---|| GAME OVER ||---✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽✽")
        break
    else:
        print("✽✽✽✽✽---|| GALA JAWAB ||---✽✽✽✽✽")
        print("✽-|| AAP GAME SE BAHAR HO GYE HO ||-✽")
        print("✽✽✽✽✽---|| GAME OVER ||---✽✽✽✽✽")
        break
    a+=1
    ll+=1
    c+=1
    cash+=10000