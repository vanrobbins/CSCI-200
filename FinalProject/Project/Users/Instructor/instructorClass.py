import os;
import sys;
# Get the absolute path of the Project directory (parent of User and Utility)
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../"))
# Add the Project directory to sys.path
if project_dir not in sys.path:
    sys.path.insert(0, project_dir);
try:
    from Users.userClass import User;
except:
    print("Module not found");


class Instructor(User):
    def setTitle(self, titleName):
        """
        Set the title of the Instructor.
        """
        self.title = titleName

    def setClasses(self, classArray):
        """
        Set the classes the Instructor is teaching.
        """
        self.classes = classArray

    def getTitle(self):
        """
        Get the title of the Instructor.
        """
        return self.title

    def getClasses(self):
        """
        Get the list of classes the Instructor is teaching.
        """
        return self.classes

    def getTitleName(self):
        """
        Get the full title (e.g., "Dr. John Doe").
        """
        return f"{self.title} {self.first} {self.last}"
    
    