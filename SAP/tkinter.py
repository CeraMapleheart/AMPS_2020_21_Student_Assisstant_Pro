import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Student Productivity Platform")

# Create GUI elements
label = tk.Label(window, text="Student Productivity Platform")
label.pack()

# Create input field for text
text_entry = tk.Entry(window, width=50)
text_entry.pack()

# Create buttons for each functionality
speech_to_text_button = tk.Button(window, text="Speech to Text", command=speech_to_text)
speech_to_text_button.pack()

text_to_speech_button = tk.Button(window, text="Text to Speech", command=text_to_speech)
text_to_speech_button.pack()

create_notes_button = tk.Button(window, text="Create Notes", command=create_notes)
create_notes_button.pack()

syllabus_button = tk.Button(window, text="Set Syllabus", command=syllabus)
syllabus_button.pack()

topics_button = tk.Button(window, text="Add Topic", command=topics)
topics_button.pack()

subtopics_button = tk.Button(window, text="Add Subtopic", command=subtopics)
subtopics_button.pack()

access_notes_button = tk.Button(window, text="Access Notes", command=notes)
access_notes_button.pack()

planner_button = tk.Button(window, text="Set Planner", command=planner)
planner_button.pack()

agenda_button = tk.Button(window, text="Set Agenda", command=agenda)
agenda_button.pack()

statistics_button = tk.Button(window, text="Set Statistics", command=statistics)
statistics_button.pack()

goals_button = tk.Button(window, text="Add Goal", command=goals)
goals_button.pack()

timetable_button = tk.Button(window, text="Update Timetable", command=timetable)
timetable_button.pack()

journal_button = tk.Button(window, text="Add Journal Entry", command=journal)
journal_button.pack()

calendar_button = tk.Button(window, text="Add Event to Calendar", command=calendar)
calendar_button.pack()

window.mainloop()