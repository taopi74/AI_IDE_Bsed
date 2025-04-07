# AI_IDE_Based.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os
from datetime import datetime

# Main window
root = tk.Tk()
root.title("AI IDE Based - Project Manager")
root.geometry("900x600")
root.configure(bg="#f0f0f0")

# Project data
projects = []

# AI-like suggestion database (simple example)
ai_suggestions = {
    "print": "print('Hello, World!') - Basic output command",
    "loop": "for i in range(5):\n    print(i) - Simple loop example",
    "function": "def my_function():\n    return 'Hello' - Define a function"
}

# Load projects from file
def load_projects():
    global projects
    try:
        with open("projects.json", "r") as file:
            projects = json.load(file)
        update_project_list()
    except FileNotFoundError:
        projects = []

# Save projects to file
def save_projects():
    with open("projects.json", "w") as file:
        json.dump(projects, file)
    messagebox.showinfo("Success", "Projects saved successfully!")

# Add new project
def add_project():
    name = project_name_entry.get().strip()
    if name:
        new_project = {
            "name": name,
            "progress": 0,
            "status": "Not Started",
            "code": f"# Project: {name}\n# Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        projects.append(new_project)
        update_project_list()
        project_name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Error", "Please enter a project name!")

# Update project list in Treeview
def update_project_list():
    project_tree.delete(*project_tree.get_children())
    for i, project in enumerate(projects):
        project_tree.insert("", "end", iid=i, values=(project["name"], f"{project['progress']}%", project["status"]))

# Show project details when selected
def show_project_details(event):
    selected = project_tree.selection()
    if selected:
        index = int(selected[0])
        code_text.delete("1.0", tk.END)
        code_text.insert("1.0", projects[index]["code"])
        progress_entry.delete(0, tk.END)
        progress_entry.insert(0, projects[index]["progress"])
        status_label.config(text=f"Status: {projects[index]['status']}\nLast Updated: {projects[index]['last_updated']}")

# Update project progress and code
def update_progress():
    selected = project_tree.selection()
    if selected:
        index = int(selected[0])
        progress = progress_entry.get()
        if progress.isdigit() and 0 <= int(progress) <= 100:
            projects[index]["progress"] = int(progress)
            projects[index]["code"] = code_text.get("1.0", tk.END).strip()
            projects[index]["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            projects[index]["status"] = "Completed" if int(progress) == 100 else "In Progress" if int(progress) > 0 else "Not Started"
            update_project_list()
            show_project_details(None)
        else:
            messagebox.showwarning("Error", "Progress must be between 0 and 100!")
    else:
        messagebox.showwarning("Error", "Select a project first!")

# AI suggestion feature
def suggest_code():
    selected = project_tree.selection()
    if selected:
        index = int(selected[0])
        keyword = suggestion_entry.get().lower().strip()
        suggestion = ai_suggestions.get(keyword, "No suggestion available. Try 'print', 'loop', or 'function'.")
        code_text.insert(tk.END, f"\n# AI Suggestion: {suggestion}\n")
    else:
        messagebox.showwarning("Error", "Select a project first!")

# UI Setup
# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save Projects", command=save_projects)
file_menu.add_command(label="Exit", command=root.quit)

# Left frame (Project list)
left_frame = ttk.Frame(root, width=300)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

project_tree = ttk.Treeview(left_frame, columns=("Name", "Progress", "Status"), show="headings", height=20)
project_tree.heading("Name", text="Project Name")
project_tree.heading("Progress", text="Progress")
project_tree.heading("Status", text="Status")
project_tree.column("Name", width=150)
project_tree.column("Progress", width=70)
project_tree.column("Status", width=100)
project_tree.pack(fill=tk.BOTH, expand=True)
project_tree.bind("<<TreeviewSelect>>", show_project_details)

tk.Label(left_frame, text="New Project Name:", bg="#f0f0f0").pack(pady=5)
project_name_entry = tk.Entry(left_frame)
project_name_entry.pack()
tk.Button(left_frame, text="Add Project", command=add_project).pack(pady=5)

# Right frame (Code editor and controls)
right_frame = ttk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

editor_frame = ttk.LabelFrame(right_frame, text="Code Editor")
editor_frame.pack(fill=tk.BOTH, expand=True, pady=5)
code_text = tk.Text(editor_frame, height=20, width=60)
code_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

control_frame = ttk.LabelFrame(right_frame, text="Controls")
control_frame.pack(fill=tk.X, pady=5)
tk.Label(control_frame, text="Progress (%):").pack(side=tk.LEFT, padx=5)
progress_entry = tk.Entry(control_frame, width=10)
progress_entry.pack(side=tk.LEFT)
tk.Button(control_frame, text="Update", command=update_progress).pack(side=tk.LEFT, padx=5)

tk.Label(control_frame, text="AI Suggestion:").pack(side=tk.LEFT, padx=5)
suggestion_entry = tk.Entry(control_frame, width=15)
suggestion_entry.pack(side=tk.LEFT)
tk.Button(control_frame, text="Suggest", command=suggest_code).pack(side=tk.LEFT, padx=5)

status_label = tk.Label(control_frame, text="Status: No project selected", wraplength=400, justify="left")
status_label.pack(side=tk.LEFT, padx=5)

# Load initial data
load_projects()

# Run the app
root.mainloop()