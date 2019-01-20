This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

* Right, then down
* Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

Analysis:

```
*

```

For a 1 by 1 matrix, the answer is 1. Also for any X by 1 matrix and 1 by X matrix, the answer is 1.

```
* *
* *
```
    
For a 2 by 2 matrix, at top left
    * when moving right, the remain matrix is 2 by 1.
    * when moving down, the remain matrix is 1 by 2.
So the answer for the 2 by 2 matrix is the sum of the answers for 2 by 1 matrix and 1 by 2 matrix. It is 2. 

```
* * *
* * *
```

For a 2 by 3 matrix, at top left
    * when moving right, the remain matrix is 2 by 2.
    * when moving down, the remain matrix is 1 by 3.
So the answer for the 2 by 3 matrix is the sum of the answers for the 2 by 2 matrix and 1 by 3 matrix.

It is obvious that the rule is:
    * when moving right, the problem becomes another smaller problem with a smaller number of columns and the same number of rows.
    * when moving down, the problem becomes another smaller problem with a smaller number of rows and the same number of columns.

Now it is time to write the code:

```

def WaysToGo(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return WaysToGo(rows - 1, columns) + WaysToGo(rows, columns - 1)

def main():
    a = (1, 1)
    b = (2, 2)
    c = (3, 3)
    d = (4, 4)
    e = (5, 5)

    x = (a, b, c, d, e)

    for i in x:
        print i, WaysToGo(i[0], i[1])


if __name__ == "__main__":
    main()

```


