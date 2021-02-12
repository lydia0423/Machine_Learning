
#?38. Write a Python program to solve (x + y) * (x + y).
#?Test Data : x = 4, y = 3
#?Expected Output : (4 + 3) ^ 2) = 49

x = 4
y = 3

ans = x * x + 2 * x * y + y * y
print("Expected Output : ({} + {} ^ 2) = {}".format(x, y, ans))

#* x * x = x^2
#* 2 * x * y = xy + xy
#* y * y = y^2