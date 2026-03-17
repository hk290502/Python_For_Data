some_file_path = r"C:\WiseOwl\files_and_folders\about_me.txt"

with open(some_file_path,'w') as some_file_name:
    some_file_name.write("My name is Hamza Khan\n")
    some_file_name.write("I live in the UK\n")
    some_file_name.write("I am a keen gym goer\n")

with open(some_file_path, "r") as f:
    print("\nFile Created!\n")
    for line in f:
        print(line)