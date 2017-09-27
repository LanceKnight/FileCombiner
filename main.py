
for i in range(1,4):
    lesson_no = str(i)
    lesson_dir = "data/" +lesson_no + ".txt"
    with open("data/total.txt","a") as output:

        with open(lesson_dir, "r") as input:
            text = input.read()
            output.write("======Lesson: " + lesson_no + "======\n" )
            output.write(text)
            output.write("\n")