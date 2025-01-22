class Course:
    def __init__(self, courseNum, courseNm, instructorUNm):
        """
        Initializes the Course object with course number, course name, and instructor username.
        """
        self.courseNumber = courseNum
        self.courseName = courseNm
        self.instructorUsername = instructorUNm

    def __str__(self):
        """
        Returns a string representation of the course with course number and name.
        """
        return f"{self.courseNumber}: {self.courseName} (Instructor: {self.instructorUsername})"

    def setCourseNumber(self, newNumber):
        """
        Sets a new course number for the course.
        """
        self.courseNumber = newNumber

    def setCourseName(self, newName):
        """
        Sets a new course name for the course.
        """
        self.courseName = newName

    def setInstructorUsername(self, newInst):
        """
        Sets a new instructor username for the course.
        """
        self.instructorUsername = newInst

    def getCourseNumber(self):
        """
        Returns the course number.
        """
        return self.courseNumber

    def getCourseName(self):
        """
        Returns the course name.
        """
        return self.courseName

    def getInstructor(self):
        """
        Returns the instructor's username.
        """

