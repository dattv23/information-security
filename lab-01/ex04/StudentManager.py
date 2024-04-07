from Student import Student


class StudentManager:
    studentList = []

    def generateID(self):
        maxId = 1
        if self.getStudentCount() > 0:
            maxId = self.studentList[0]._id
            for student in self.studentList:
                if maxId < student._id:
                    maxId = student._id
            maxId += 1
        return maxId

    def getStudentCount(self):
        return len(self.studentList)

    def addStudent(self):
        studentId = self.generateID()
        name = input("Enter student's name: ")
        gender = input("Enter student's gender: ")
        major = input("Enter student's major: ")
        average_score = float(input("Enter student's average score: "))
        student = Student(studentId, name, gender, major, average_score)
        self.classifyAcademicPerformance(student)
        self.studentList.append(student)

    def updateStudent(self, ID):
        student = self.findStudentByID(ID)
        if student is not None:
            name = input("Enter the new name of the student: ")
            gender = input("Enter the new gender of the student: ")
            major = input("Enter the new major of the student: ")
            average_score = float(input("Enter the new average score of the student: "))
            student._name = name
            student._gender = gender
            student._major = major
            student._average_score = average_score
            self.classifyAcademicPerformance(student)
        else:
            print(f"Student with ID = {ID} does not exist.")

    def sortStudentsByID(self):
        self.studentList.sort(key=lambda student: student._id)

    def sortStudentsByName(self):
        self.studentList.sort(key=lambda student: student._name)

    def sortStudentsByAverageScore(self):
        self.studentList.sort(key=lambda student: student._average_score)

    def findStudentByID(self, ID):
        for student in self.studentList:
            if student._id == ID:
                return student
        return None

    def findStudentsByName(self, name):
        return [
            student
            for student in self.studentList
            if name.upper() in student._name.upper()
        ]

    def deleteStudentByID(self, ID):
        student = self.findStudentByID(ID)
        if student is not None:
            self.studentList.remove(student)
            return True
        return False

    def classifyAcademicPerformance(self, student):
        if student._average_score >= 8:
            student._academicPerformance = "Good"
        elif student._average_score >= 6.5:
            student._academicPerformance = "Fair"
        elif student._average_score >= 5:
            student._academicPerformance = "Average"
        else:
            student._academicPerformance = "Poor"

    def displayStudents(self, students):
        print(
            "{:<8} {:<18} {:<8} {:<10} {:<15} {:<15}".format(
                "ID", "Name", "Gender", "Major", "Avg Score", "Performance"
            )
        )
        for student in students:
            print(
                "{:<8} {:<18} {:<8} {:<10} {:<15} {:<15}".format(
                    student._id,
                    student._name,
                    student._gender,
                    student._major,
                    student._average_score,
                    student._academicPerformance,
                )
            )
        print("\n")

    def getAllStudents(self):
        return self.studentList
