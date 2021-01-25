first_x, first_y = map(int, input().split())
second_x, second_y = map(int, input().split())
third_x, third_y = map(int, input().split())

if first_x == second_x:
    fourth_x = third_x
elif first_x == third_x:
    fourth_x = second_x
else:
    fourth_x = first_x

if first_y == second_y:
    fourth_y = third_y
elif first_y == third_y:
    fourth_y = second_y
else:
    fourth_y = first_y

print(fourth_x, fourth_y)
