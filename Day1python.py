q1=[123,354,324,2340,324,234,756,955]
print("Question 1: ")
print(max(q1))

q2=[432,435,"588","464",234]
new_numbers = [];
for n in q2:
    new_numbers.append(int(n));
q2 = new_numbers;
print("Question 2: ")
print(q2)

new_numbers2 = [];
for n in q2:
    new_numbers2.append(str(n));
q2 = new_numbers2;
print(q2)

q3={"k1": "v1", "k2": "v2", "k3": "v3"}
q3update = {y:x for x,y in q3.items()}
print ("Question 3: ")
print(q3update)

q4=(1,2,3,4)

q5=[50,96,45,67,88]
count=0
for number in q5:
    if number < 70:
        count=count+1
print("Question 5: ")
print("Number of Exams failed:")
print(count)

q6=[33,15,76,78,34,56]
print("Question 6: ")
for number in q6:
    if ((number % 3 == 0) and (number % 5 == 0)):
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
print(q6)