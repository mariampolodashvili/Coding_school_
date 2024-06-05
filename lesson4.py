# 1. ციკლის მეშვეობით 3 მომხმარებელს შეაყვანინე
# ინფორმაცია საკუთარი სახელის, გვარის და ასაკის
# შესახებ. თითოეული მომხმარებლის ინფორმაცია
# შეინახე ინდივიდუალურ სიაში. შემდეგ კი სამივე სია
# დაამატე საერთო ცალრიელ სიას სახელად consumer_info.
# Input_ის მეშვეობით მომხმარებლის ინდექსის შეყვანის
# შემთხვევაში პროგრამამ უნდა დაბრუნოს არჩეულ
# მომხმარებელზე ინფორმაცია შემდეგნაირად:
#
consumer_info=[]
i=0
while i<3:
    List=[]
    name=input('Enter name: ')
    surname = input('Enter surname: ')
    age = input('Enter age: ')
    List.append(name)
    List.append(surname)
    List.append(age)
    consumer_info.append(List)
    i+=1

print(consumer_info)
index=int(input('Enter index: '))
print(f'Name: {consumer_info[index][0]}\nLastname: {consumer_info[index][1]}\nAge: {consumer_info[index][2]}\n')

# 2. შექმენი ჩაშენებული სია, რომელშიც იქნება შენახული
# ცნობილი მსახიობების შესახებ ინფორმაცია.
# მომხმარებელს შემოჰყავს მსახიობის სახელი ან გვარი.
# თუ სიაში მოიძებნა მსახიობი, დაბეჭდe მის შესახებ
# არსებული ინფორმაცია რეზუმის სახით.

famous_actors = [
    {
        "name": "Leonardo DiCaprio",
        "birthdate": "1974-11-11",
        "nationality": "American",
        "notable_works": ["Titanic", "Inception", "The Revenant"]
    },
    {
        "name": "Meryl Streep",
        "birthdate": "1949-06-22",
        "nationality": "American",
        "notable_works": ["The Devil Wears Prada", "Sophie's Choice", "Mamma Mia!"]
    },
    {
        "name": "Denzel Washington",
        "birthdate": "1954-12-28",
        "nationality": "American",
        "notable_works": ["Training Day", "Glory", "Fences"]
    },
    {
        "name": "Cate Blanchett",
        "birthdate": "1969-05-14",
        "nationality": "Australian",
        "notable_works": ["The Lord of the Rings", "Blue Jasmine", "Carol"]
    },
    {
        "name": "Tom Hanks",
        "birthdate": "1956-07-09",
        "nationality": "American",
        "notable_works": ["Forrest Gump", "Saving Private Ryan", "Cast Away"]
    },
    {
        "name": "Natalie Portman",
        "birthdate": "1981-06-09",
        "nationality": "Israeli-American",
        "notable_works": ["Black Swan", "V for Vendetta", "Jackie"]
    },
    {
        "name": "Morgan Freeman",
        "birthdate": "1937-06-01",
        "nationality": "American",
        "notable_works": ["The Shawshank Redemption", "Driving Miss Daisy", "Se7en"]
    },
    {
        "name": "Scarlett Johansson",
        "birthdate": "1984-11-22",
        "nationality": "American",
        "notable_works": ["Lost in Translation", "The Avengers", "Marriage Story"]
    },
    {
        "name": "Robert De Niro",
        "birthdate": "1943-08-17",
        "nationality": "American",
        "notable_works": ["Taxi Driver", "Raging Bull", "Goodfellas"]
    },
    {
        "name": "Jennifer Lawrence",
        "birthdate": "1990-08-15",
        "nationality": "American",
        "notable_works": ["The Hunger Games", "Silver Linings Playbook", "American Hustle"]
    }
]

name=input('Enter name: ')
for resume in famous_actors:
    if name==resume['name']:
        print(resume)


# 3. შექმენი ფუნქცია რომელიც მიიღებს სიას და
# დააბრუნებს ასევე სიას, თუმცა უნიკალური
# ელემენტებით (გამოიყენე set მონაცემთა ტიპი).

def unique_list(list):
    unique_set=set()
    for char in list:
        unique_set.add(f'{char}')
    return unique_set

List=[1,2,2,3,3,3]
print(list(unique_list(List)))


# 4. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის
# მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.

def set_to_tuple(set1, set2):
    set3=set1.union(set2)
    return tuple(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set_to_tuple(set1, set2))

# 5. დაწერე პროგრამა, რომელიც შეამოწმებს გადაცემული
# ლექსიკონი არის თუ არა ცარიელი.

def empty_dict(dict):
    if not dict:
        return 'Dictionary is empty'
    else:
        return 'Dictionary is not empty'

dict={}
print(empty_dict(dict))

# 6. დაწერე პროგრამა რომელიც სტრიქონისგან ქმნის
# ლექსიკონს.
# დათვალე სტრიქონში კონკრეტული სიმბოლოს
# ოდენობა.

def str_to_dict(string):
    dict={}
    for i in string:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict

print(str_to_dict('w3schools'))


# 7. შექმენი while ციკლი, რომელიც მომხმარებელს ხუთჯერ
# შემოატანინებს ინფორმაციას და ჩაამატებს ცარიელ
# სიაში. შედეგი დაბეჭდე. (append მეთოდი)

i=0
list=[]
while i<5:
    info=input('enter information: ')
    list.append(info)
    i+=1

print(list)

# 8. მიღებული სიის პირველ და ბოლო ელემენტებს ადგილი
# შეუცვალე და დაბეჭდე შედეგი.
# წაშალე სიაში მომხმარებლის მიერ მოთხოვნილი
# ელემენტი. (remove მეთოდი)

first=list[0]
last=list[len(list)-1]

list[0]=last
last=list[len(list)-1]=first

print(list)

element=input('which element you want to delete? ')
list.remove(element)
print(list)

#იპოვე სიის სიგრძე მინიმუმ ორი მეთოდით.

print(len(list))
count=0
for i in list:
    count+=1
print(count)

# 10. ამობეჭდე სიის ყოველი ელემენტი მის ინდექსთან
# ერთად მინიმუმ ორი მეთოდით.

for i in list:
    print(f'{i}: {list.index(i)}')

for i in range(len(list)):
    print(f'{list[i]}: {i}')

# 11. შეკრიბე ორი სია და დაბეჭდე შედეგი.

list1=['1', '2', '3']
list2=['4', '5']

print(list1+list2)

# 12. შეასრულე იგივე ოპერაცია extend მეთოდის
# დახმარებით.

list1.extend(list2)
print(list1)

# 13. გაამრავლე სია რიცხვზე და დაბეჭდე შედეგი.

list=['1', '2', '3']
print(list*2)

# 14. Slicing _ ის გამოყენებით შეაბრუნე სია და დაბეჭდე
# შედეგი.

list=['1', '2', '3']
print(list[::-1])

# 15. გააკეთე იგივე reverse მეთოდის გამოყენებით.

list=['1', '2', '3']
list.reverse()
print(list)

