"""
File Name: lab2LinearFunction2Points
Purpose: 
    This file finds and illustrates the slope intercept form of a function given two points. 
    It also finds and illustrates the X and Y-intercepts of the function.
Special Requirements: 
    It must use at least three types of variables, and define at least five variables. It must also use at least one mathmatical operation.
    All values must be stored in variables before they are used. The output must be a paragraph using at least four variables and computation result(s).
Variables Used In the Order of Creation:
    pointAX: Point A's x-value
    pointAY: Point A's y-value
    pointBX: Point B's x-value
    pointBY: Point B's y-value
    differenceY: Difference between point A's y-value and point B's y-value
    differenceX: Difference between point A's x-value and point B's x-value
    slope: Finds the slope of the two points
    yInterceptY: Finds the y intercept of the line or b value in y=mx+b
    xInterceptX: Finds the x intercept of the line or when y is equal to 0 in y=mx+b
    yInterceptX: The x value of the functions y-intercept or 0
    xInterceptY: The y value of the functions x-intercept or 0
    slopeIntEquation: The found equation given the two points or y=mx+b
    message: Final message that outputs the results
First Created Date: 9/5/2024
Last Updated: 9/8/2024
Author: Van Robbins
Version 1.0
"""

#Creating Variables and Initiating there values
pointAX=1; #X Value of Point A:(1,2)
pointAY=2; #Y Value of Point A:(1,2)
pointBX=3; #X Value of Point B:(3,7)
pointBY=7; #Y Value of PointB:(3,7)
differenceY=0; #Difference of Point A and B Y values, initiated at 0 calculated later
differenceX=0; #Difference of Point A and B X values, initiated at 0 calculated later
slope=0.0; #Slope of the linear function, initiated at 0.0 calculated later
yInterceptY=0; #Y intercepts Y value, initiated at 0 calculated later
xInterceptX=0; #X intercepts X value, initiated at 0 calculated later
yInterceptX=0; #Y intercepts X value or 0
xInterceptY=0; #X intercepts Y value or 0
slopeIntEquation="y=mx+b" #Slope Intercept Equation base, initiated at y=mx+b m and b values will be found later
message=""; #Final message to print results, initiated as empty string

#Find Slope
differenceY=pointAY-pointBY;
differenceX=pointAX-pointBX;
slope= differenceY/differenceX;

#Find Y Intercept's Y value or b
yInterceptY= pointAY-(slope*pointAX);

#Find X Intercept's X value
xInterceptX= -yInterceptY/slope

#Insert Values into equation
slopeIntEquation=f"y={slope}x{yInterceptY}"

#Insert message statement
message=f"""A linear function passes through the points ({pointAX},{pointAY}) and ({pointBX},{pointBY})
The slope of the function is {slope}
The Y-intercept of the function is ({yInterceptX},{yInterceptY}) and the X-intercept of the function is ({xInterceptX},{xInterceptY})
The slope intercept form of the function is """+slopeIntEquation

print(message);