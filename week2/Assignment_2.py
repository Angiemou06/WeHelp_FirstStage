# Task 1
print("===Task 1===")
def find_and_print(messages):
    # write down your judgment rules in comments
    # 若年齡18 歲以上，則大於17歲
    # 若在臺灣達法定成年年齡，則大於17歲
    # 若能夠擁有投票權，則大於17歲
    # your code here, based on your own rules
    for key, value in messages.items():
        if "I'm 18 years old." in value:
            print(key)
        elif "I am of legal age in Taiwan." in value:
            print(key)
        elif "I will vote" in value:
            print(key)

find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a collegpye student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})

# Task 2
print("===Task 2===")
def calculate_sum_of_bonus(data):
    # write down your bonus rules in comments
    # bonus 基礎為 salary * 0.05 倍
    # 再根據performance 分為三個階級：
    # 1.above average 者 bonus + 500 2.average 者 bonus + 200 3.below average 者 bonus 不增減
    # 最後根據職稱分為三個階級：
    # 1.Engineer bonus + 500 2.CEO bonus 不增減 3. Sales bonus + 500
    # 若總 bonus 超過 10000 元，按照每人 bonus 比例，攤分 10000 元獎金

    # your code here, based on your own rules
    sumBonus = 0
    bonus = []
    for data in data.items():
        data = data[1]
        for i in range(0,len(data)):  
            salary = data[i].get("salary")
            salary = str(salary)
            if "USD" in salary:
                salary = salary[:-3]
                salary = int(salary)
                salary = salary*30
            elif "," in salary:
                salary = salary.translate({ord(','): None})
            
            salary = int(salary)
            base = salary * 0.05
            add = 0
            performance = data[i].get("performance")
            if performance=="above average":
                add = add + 500
            elif performance=="average":
                add = add + 200
            
            role = data[i].get("role")
            if role!="CEO":
                add = add + 500
            bonus.append(base + add)
            sumBonus = sumBonus + bonus[i]
    if sumBonus > 10000:
        sumBonus = 0
        Sum = sum(bonus)
        for i in range(0,len(bonus)):
            bonus[i] = 10000*(bonus[i]/Sum)
            sumBonus = sumBonus + bonus[i]

    print("sum of bonus: ",'{:.0f}'.format(sumBonus)," TWD")

calculate_sum_of_bonus({
    "employees":[
    {
        "name":"John",
        "salary":"1000USD",
        "performance":"above average",
        "role":"Engineer"
    },
    {
        "name":"Bob",
        "salary":60000,
        "performance":"average",
        "role":"CEO"
    },
    {
        "name":"Jenny",
        "salary":"50,000",
        "performance":"below average",
        "role":"Sales"
    }
    ]
}) # call calculate_sum_of_bonus function

# Task 3
print("===Task 3===")
def func(*data):
    name=[]
    key=[]
    lo = 0
    # your code here
    for data in data:
        name.append(data)
        key.append(name[lo][1])
        lo+=1

    for i in range(0,len(key)):
        ct = 0
        for j in range(0,len(key)):
            if key[i] == key[j]:
                ct+=1
        if ct < 2:
            print(name[i])

func("彭⼤牆", "王明雅", "吳明") # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

# Task 4
print("===Task 4===")

def get_number(index):
    # your code here
    if index%2 == 0:
        print('{:.0f}'.format(index/2*3))
    elif index == 0:
        print('{:.0f}'.format(index))
    else:
        print('{:.0f}'.format(4+int(index/2)*3))

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

# Task 5
print("===Task 5===")

def find_index_of_car(seats, status, number):
    # your code here
    gap=[]
    lo=[]
    for i in range(0,len(seats)):
        if status[i] == 0:
            seats[i] = 0
        if (seats[i]-number) >= 0:
            gap.append(seats[i]-number)
            lo.append(i)
    if len(gap) != 0:
        location = gap.index(min(gap))
        print(lo[location])
    else:
        print(-1)
           

find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2) # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2