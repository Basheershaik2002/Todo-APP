# Todo-APP

## About This Task

This project is a simple and functional **To-Do List Web Application** built using **Streamlit** and **Python**. It allows users to easily **add**, **view**, and **remove** tasks in a clean interface with persistent storage using a local text file.

The goal of this project was to get hands-on experience with:
- Building interactive web apps using Streamlit
- Managing dynamic user input
- Implementing stateful logic (task updates and deletions)
- Saving data locally using Python file operations
- Deploying a Python-based web app to the cloud

---

### How It Works

- When the app loads, it reads tasks from a `tasks.txt` file (if available).
- The user can add a task using a simple text input.
- The app immediately saves the task and displays it in a live list.
- The user can remove any task by selecting it from a dropdown and clicking remove.
- The task list persists across sessions using file-based storage.
- The UI automatically refreshes after every add or delete using `st.rerun()`.

---

### Why I Built It

I chose this project as a hands-on way to explore how **Streamlit** can be used beyond data science dashboards. A to-do list is something familiar and practical, which made it a great use case for learning about:

- Form inputs and widgets in Streamlit
- Updating and displaying dynamic lists
- Lightweight deployment of Python web apps
- User-centered design and UX basics

It also helped me understand how to separate **logic**, **UI**, and **state management** — all critical for building web applications.

---

### Live App
**
**[Click below to use the app] 

#### (https://commitsapporbasheershaik2002-mgs4ehphd4xbm5zguofgny.streamlit.app/)####

This app is deployed using **Streamlit Cloud** and is publicly accessible. Try adding and removing your own tasks to see it in action.

---

### Technologies Used

- **Python 3**
- **Streamlit**
- File handling (`tasks.txt`)
- Git & GitHub for version control
- Streamlit Cloud for deployment

---

### What I Learned

- Creating responsive UI with Streamlit
- Managing app state using file storage
- Real-time refresh using `st.rerun()`
- Debugging and testing user flows
- End-to-end deployment of a Streamlit project

---

### Future Enhancements

- Add checkboxes to mark tasks as completed
- Store tasks in a database (SQLite/Supabase)
- Add due dates and sorting/filtering options
- Multi-user task lists with login system

---

## Summary

This project demonstrates how a small, focused app can still involve **frontend**, **backend**, **file management**, and **deployment** — all using just Python. It’s a great starting point for anyone learning full-stack development with Streamlit.
