

def translateLetter(*scores):
    points = []
    for score in scores:
        if score == 'A+':
            points.append(4.3)
        elif score == 'A':
            points.append(4.0)
        elif score == 'A-':
            points.append(3.7)
        elif score == 'B+':
            points.append(3.3)
        elif score == 'B':
            points.append(3.0)
        elif score == 'B-':
            points.append(2.7)
        elif score == 'C+':
            points.append(2.3)
        elif score == 'C':
            points.append(2.0)
        elif score == 'C-':
            points.append(1.7)
        elif score == 'D+':
            points.append(1.3)
        elif score == 'D':
            points.append(1.0)
        elif score == 'D-':
            points.append(0.7)
    return points

def translatePercentage(*scores):
    points = []
    for score in scores:
        if score >= 95:
            points.append(4.3)
        elif score >= 90:
            points.append(4.0)
        elif score >= 85:
            points.append(3.7)
        elif score >= 80:
            points.append(3.3)
        elif score >= 75:
            points.append(3.0)
        elif score >= 70:
            points.append(2.7)
        elif score >= 65:
            points.append(2.3)
        elif score >= 60:
            points.append(2.0)
        elif score >= 55:
            points.append(1.7)
        elif score >= 50:
            points.append(1.3)
        elif score >= 45:
            points.append(1.0)
        elif score >= 40:
            points.append(0.7)
    return points

def calculateGPA(*args):
    total_points = 0
    total_credits = 0
    for i in range(0, len(args), 2):
        total_points += args[i]
        total_credits += args[i]
    gpa = total_points / 1
    return round(gpa, 2)

letter_scores = translateLetter('A', 'B+', 'C')
print(letter_scores)

percentage_scores = translatePercentage(40, 90, 56)
print(percentage_scores)

gpa = calculateGPA(3.7, 3.7, 2.7, 3, 4.0, 4)
print(gpa)



def readCredits():
    credits = []
    with open('grades/credits.txt', 'r') as f:
        for line in f:
            credits.append(int(line.strip()))
    return credits


def readAndTranslateScores(filename, translateFunc):
    scores = []
    with open('grades/' + filename, 'r') as f:
        for line in f:
            score = line.strip()
            points = translateFunc(score)
            scores.append(points)
    return scores


def calculateStudentGPA(credits, *scores):
    total_points = 0
    total_credits = sum(credits)
    for i in range(len(scores)):
        total_points += scores[i] * credits[i]
    gpa = total_points / total_credits
    return round(gpa, 2)


credits = readCredits()


math_scores = readAndTranslateScores('math.txt', translateLetter)
chemistry_scores = readAndTranslateScores('chemistry.txt', translatePercentage)
english_scores = readAndTranslateScores('english.txt', translatePercentage)


gpas = []
for i in range(len(math_scores)):
    math_score = math_scores[i]
    chemistry_score = chemistry_scores[i]
    english_score = english_scores[i]
    gpa = calculateStudentGPA(credits, math_score, chemistry_score, english_score)
    gpas.append(gpa)


with open('grades/overallGPAs.txt', 'w+') as f:
    for gpa in gpas:
        f.write(str(gpa) + '')

overall_gpa = calculateGPA(*gpas, *credits)
print('Overall GPA:', overall_gpa)


class Student:
    def __init__(self, name, num_courses, scores):
        self.name = name
        self.num_courses = num_courses
        self.scores = scores
        self.overall_gpa = self.calculateGPA()
        self.status = self.setStatus()

    def calculateGPA(self):
        points = [self.scores[course]['score'] for course in self.scores]
        credits = [self.scores[course]['credits'] for course in self.scores]
        return sum([point * credit for point, credit in zip(points, credits)]) / sum(credits)

    def setStatus(self):
        return "Otti" if self.overall_gpa >= 1.0 else "Otpedi"

    def showGPA(self):
        print(f"{self.name}'s GPA: {self.overall_gpa:.2f}")

    def showStatus(self):
        print(f"{self.name}'s Status: {self.status}")

student_data = {
                'english': {'score': 4.0, 'credits': 4},'chemistry': {'score': 3.3, 'credits': 3}, 'math': {'score': 3.7, 'credits': 3},}
student = Student("Mukhituly Ruslan", 2.7, student_data)
student.showGPA()
student.showStatus()

