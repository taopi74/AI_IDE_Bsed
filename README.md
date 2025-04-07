# AI_IDE_Bsed


### Features of AI_IDE_Based

#### Project Management:
- **Add New Project**: Allows users to create a new project by entering a project name.
- **Update Progress (0-100%)**: Users can update the progress of a project with a percentage value between 0 and 100.
- **Automatic Status Update**: The project status automatically updates based on progress:
  - "Not Started" (0%),
  - "In Progress" (1-99%),
  - "Completed" (100%).

#### Code Editor:
- **Write and Save Project Code**: Users can write code for each project and save it within the project data.
- **File Open and Save Functionality**: Supports opening external `.txt` or `.py` files into the editor and saving the current code to a file.

#### AI Suggestion:
- **Basic Code Suggestions**: Provides simple code snippets based on keywords entered by the user. Supported keywords include:
  - "print": Suggests `print('Hello, World!')`.
  - "loop": Suggests a `for` loop example.
  - "function": Suggests a function definition.
  - "if": Suggests a conditional statement.
  - If an unsupported keyword is entered, it displays a message suggesting valid options.

#### User Interface:
- **Layout**: 
  - **Left Side**: A project list displayed in a Treeview widget, showing project name, progress, and status.
  - **Right Side**: A code editor (Text widget) for writing code and a control panel for managing progress and AI suggestions.
- **Menu Bar**: Includes a "File" menu with options:
  - "Save Projects": Saves all project data to `projects.json`.
  - "Save Code As": Saves the current project's code to a separate file.
  - "Open File": Opens an external file into the code editor.
  - "Exit": Closes the application.

---
