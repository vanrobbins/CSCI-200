# Lab 2 Algorithm

## Van Robbins 9/8/2024

### Problem Description

Design and create a python program that outputs a paragraph using variables and expressions that finds a linear function in slope intercept form given two points it passes through. The program will also output the functions x and y intercepts. It will use at least three types of variables, and define at least five variables. It will also use at least one mathmatical operation.

All values must be stored in variables before they are used. The output must be a paragraph using at least four variables and computation result(s).

### Algorithm

1. Comment Block File Header that details the name of the file, purpose, special requirements, variables, and version of the file
2. Create Variables So That All Values Are Stored In Variables Before They Are Used
   1. pointAX: Point A's x-value
   2. pointAY: Point A's y-value
   3. pointBX: Point B's x-value
   4. pointBY: Point B's y-value
   5. differenceY: Difference between point A's y-value and point B's y-value
   6. differenceX: Difference between point A's x-value and point B's x-value
   7. slope: Finds the slope of the two points
   8. yInterceptY: Finds the y intercept of the line or b value in y=mx+b
   9. xInterceptX: Finds the x intercept of the line or when y is equal to 0 in y=mx+b
   10. yInterceptX: The x value of the functions y-intercept or 0
   11. xInterceptY: The y value of the functions x-intercept or 0
   12. slopeIntEquation: The found equation given the two points or y=mx+b
   13. message: Final message that outputs the results
3. Calculate slope, y-intercept, and x-intercept of equation
   1. To find the slope given two points we must find the rise over run or change in y divided by change in x
      1. Find the difference between the y values of the two points
      2. Find the difference between the x values of the two points
      3. Divide the difference of the y values by the difference of the x values giving you the slope between the two points
   2. To find the equation's y-intercept we must plug in one of the points and the slope into the equation y=mx+b to find b
      1. Solve for b by setting the equation to y-mx=b
      2. Insert pointAY for y
      3. Insert slope for m
      4. Insert pointAX for x
      5. We find that the y-intercept is equal to the difference between pointAY and the slope times pointAX or interceptY=pointAY-(slope*pointAX)
   3. To find the equation's x-intercept we must set y to 0 in y=mx+b and solve for x
      1. Change the equation to equal x, x=(y-b)/m
      2. Y is 0 since it is the x-intercept
      3. Equation is x=-b/m
      4. In the previous two calculations the values of m and b were found or slope and yInterceptY respectively so xInterceptX=-yInterceptY/slope
4. Print out results of the calculations
   1. Set slopeIntEquation to final found equation through cacatination "f(x)=(slope)x+(interceptY)"
   2. Set message to equal "A linear function passes through the points ({pointAX},{pointAY}) and ({pointBX},{pointBY}). The slope of the function is {slope}.  The Y-intercept of the function is ({yInterceptX},{yInterceptY}) and the X-intercept of the function is ({xInterceptX},{xInterceptY}). The slope intercept form of the function is"+{slopeIntEquation}
   3. Print with print(f) the message variable so that the variables are printed properly
