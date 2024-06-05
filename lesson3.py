# 1. შექმენი ფუნქცია, რომელიც მომხმარებლისგან მიღებულ ინფორმაციას გაასამმაგებს
# # და დაბეჭდავს შემდეგნაირად

def Triple():
    message=input('Enter: ')
    print(f'Tripled: {message*3}')

Triple()

# 2. შექმენი ფუნქცია, რომელიც მიიღებს მომხმარებლის წონას და დააბრუნებს მის წონას
# მთვარეზე. (მთვარის გრავიტაცია 6_ჯერ ნაკლებია დედამიწისაზე)

def Weight_on_moon():
    weight=int(input('Enter your weight: '))
    return weight//6

print(Weight_on_moon())

# 3. შექმენი კალკულატორის ფუნქცია, რომელიც მიიღებს გამოსახულებას
# მომხმარებლისგან input() ფუნქციის დახმარებით (სამ მონაცემს _ პირველ რიცხვს,
# მოქმედებას (+ - * / ^), მეორე რიცხვს)

def Calculator():
    try:
        num1 = int(input('Enter first number: '))
        operation = input('operation: ')
        num2 = int(input('Enter second number: '))

        if num2 == 0 and operation == '/':
            return 'You can not divide a number by zero '
        else:
            if operation == '+':
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            elif operation == '*':
                return num1 * num2
            elif operation == '/':
                return num1 / num2
            elif operation == '^':
                return num1 ^ num2
    except ValueError:
        return 'You can only enter a number '

print(Calculator())