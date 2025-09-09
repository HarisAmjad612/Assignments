marks = int(input('Enter student marks: '))

if marks >= 85 and marks <=100:
    print('Grade: A')

elif marks >= 70 and marks <= 84:
    print('Grade: B')
    
elif marks >= 50 and marks <= 69:
    print('Grade: C')

elif marks < 50 and marks >= 0:
    print('Grade: F')

else: 
    print('Enter valid marks!')
