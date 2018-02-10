"""Points in a rectangle
Max. Marks: 100
Given a rectangle with sides parallel to X and Y axis and N points in X-Y co-ordinates, print the total number of points that lie strictly inside the rectangle.

Input ::
The first line consist of a single integer T - the number of test cases.
For every test case the input is as follows -
First Line consists of x1 y1 x2 y2 - (x1, y1) and (x2, y2) are opposite corner points of the rectangle.
Next line consists of N
N lines follows - each line containing - X Y coordinate of the point.

Output :: Output in T lines, the answer to each test case.
"""

t = int(input())                                #test cases
while t > 0:
     x1,y1,x2,y2 = map(int,input().split())     #input coordinates
     maxx=max(x1,x2)                           
     minx=min(x1,x2)
     maxy=max(y1,y2)
     miny=min(y1,y2)
     count=0
     cases = int(input())
     while cases > 0:
         a,b = map(int,input().split())
         if ((a>minx) and (a<maxx) and (b<maxy) and (b>miny)):
             count += 1
         cases -= 1
     print(count)
     t -= 1