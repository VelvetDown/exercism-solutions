"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores."""
    rounded_scores = []
    for score in student_scores:
        rounded_scores.append(round(score))
    return rounded_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided."""
    failed_students = 0
    for score in student_scores:
        if score <= 40:
            failed_students += 1
    return failed_students
    
def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold."""
    best_scores = []
    for score in student_scores:
        if score >= threshold:
            best_scores.append(score)
    return best_scores

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade."""
    gap = (highest - 40) / 4
    result = []
    for n in range(0, 4):
        result.append(int(41 + (n * gap)))
    return result


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order."""
    ranking = []
    for score in student_scores:
        name = student_names[student_scores.index(score)]
        ranking.append(f'{student_scores.index(score) + 1}. {name}: {score}')
    return ranking

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam."""
    perfect = []
    for info in student_info:
        if 100 in info:
            for element in info:
                perfect.append(element)
            break
    return perfect