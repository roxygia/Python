import csv

exam_results = []

with open("exam_results.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        exam_results.append(line)

#print(exam_results)

# for student_result in exam_results:
#     #print(student_result[0], student_result[1])
#     score = float(student_result[1])*100
#     print(f"{student_result[0]:<20} {score:.0f}%")

with open("exam_results_output.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")
    for student_result in exam_results:
        score = round(float(student_result[1])*100)
        csv_writer.writerow([student_result[0], f"{score}%"])
