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
    print("Module not found")
class Student(User):
    def setClasses(self, classArray):
        """
        Set the classes for the student.
        """
        self.classes = classArray

    def getClasses(self):
        """
        Get the list of classes the student is enrolled in.
        """
        return self.classes