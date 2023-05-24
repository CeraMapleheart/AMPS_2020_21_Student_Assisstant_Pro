import tkinter as tk
import speech_recognition as sr
import pyttsx3
import os

# Variables to store data
syllabus_data = ""
topics_data = []
subtopics_data = []
notes_data = []
planner_data = ""
agenda_data = ""
statistics_data = ""
goals_data = []
timetable_data = {}
journal_data = {}
calendar_data = {}

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        # Code to display the converted text in the GUI or perform any desired action
        text_entry.delete(0, tk.END)
        text_entry.insert(tk.END, text)
    except sr.UnknownValueError:
        # Handle speech recognition errors
        print("Error: Unable to recognize speech.")

def text_to_speech():
    engine = pyttsx3.init()
    text = text_entry.get()
    engine.say(text)
    engine.runAndWait()

def create_notes():
    note = text_entry.get()
    notes_data.append(note)
    # Code to save the note or perform any desired action
    print("Note created:", note)
    text_entry.delete(0, tk.END)

def syllabus():
    global syllabus_data
    syllabus_data = text_entry.get()
    # Code to save the syllabus or perform any desired action
    print("Syllabus set:", syllabus_data)
    text_entry.delete(0, tk.END)

def topics():
    topic = text_entry.get()
    topics_data.append(topic)
    # Code to add the topic or perform any desired action
    print("Topic added:", topic)
    text_entry.delete(0, tk.END)

def subtopics():
    subtopic = text_entry.get()
    subtopics_data.append(subtopic)
    # Code to add the subtopic or perform any desired action
    print("Subtopic added:", subtopic)
    text_entry.delete(0, tk.END)

def notes():
    # Code to access and display notes or perform any desired action
    print("Accessing notes...")
    for note in notes_data:
        print("- ", note)
        

def save_note():
    note = "Sample note"  
    file_name = "note.txt"  
    with open(file_name, 'w') as file:
        file.write(note)

def share_note(note):
    api_url = "https://example.com/api/post_note"
    data = {
        'note': note
    }
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Note shared successfully")
    else:
        print("Error sharing note")

def create_journal(journal_type):
    journal_file = f"{journal_type}_journal.txt"
    with open(journal_file, 'w') as file:
        file.write("Start of the journal\n")
        file.write(f"Journal type: {journal_type}\n")
        file.write("Add your journal entries here\n")
    print(f"Journal '{journal_type}' created successfully")

def open_file(file_path):
    os.startfile(file_path)

def planner():
    global planner_data
    planner_data = text_entry.get()
    # Code to set the planner or perform any desired action
    print("Planner set:", planner_data)
    text_entry.delete(0, tk.END)

def agenda():
    global agenda_data
    agenda_data = text_entry.get()
    # Code to set the agenda or perform any desired action
    print("Agenda set:", agenda_data)
    text_entry.delete(0, tk.END)

def statistics():
    global statistics_data
    statistics_data = text_entry.get()
    # Code to set the statistics or perform any desired action
    print("Statistics set:", statistics_data)
    text_entry.delete(0, tk.END)

def goals():
    goal = text_entry.get()
    goals_data.append(goal)
    # Code to add the goal or perform any desired action
    print("Goal added:", goal)
    text_entry.delete(0, tk.END)

def timetable():
    day = text_entry.get()
    schedule = input("Enter the schedule for {}: ".format(day))
    timetable_data[day] = schedule
    # Code to add the timetable or perform any desired action
    print("Timetable updated for", day)
    text_entry.delete(0, tk.END)

def journal():
    journal_type = text_entry.get()
    entry = input("Enter your {} journal entry: ".format(journal_type))
    journal_data[journal_type] = entry
    # Code to add the journal entry or perform any desired action
    print("{} journal entry added.".format(journal_type))
    text_entry.delete(0, tk.END)

def calendar():
    event = text_entry.get()
    date = input("Enter the date for {}: ".format(event))
    calendar_data[event] = date
    # Code to add the event to the calendar or perform any desired action
    print("Event added to the calendar:", event)
    text_entry.delete(0, tk.END)