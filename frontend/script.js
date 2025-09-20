/* crash course on the JS topics that are used:
- DOM: the Document Object Model (DOM) is how JS interacts with the HTML you have!
- Event Listeners: JS lets you "listen" for things like clicks or form submissions. 
                  super important when making an interactable webpage like a planner/calender
- Fetch: This is how we talk to the FastAPI backend. fetch() sets an HTTP request, await waits for the response!
- async/await: Asynchronous basically means that u don't want to block the browser while waiting for something 
              like a network request
- Loops: Similar to any coding language, we made use of loops to streamline tasks. you'll notice that we used a foreach loop to write code
       that can display a to-do list/tasks for a team.
*/
// get references to the main HTML elements we're gonna interact with
const loginForm = document.getElementById("login-form");  // form for logging in
const signupForm = document.getElementById("signup-form"); // form for signing up
const taskForm = document.getElementById("task-form");    // form for adding new tasks
const taskInput = document.getElementById("task-input");  // input box where user types the task
const taskList = document.getElementById("task-list");    //  <ul> where tasks will be displayed
const API_BASE = "/api/v1";
let token = null;

// Show or hide forms
function showTaskForm() {
  loginForm.style.display = "none";
  signupForm.style.display = "none";
  taskForm.style.display = "flex";
}

// Login
loginForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("login-email").value;
  const password = document.getElementById("login-password").value;

  const res = await fetch(`${API_BASE}/auth/login`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({email, password})
  });

  if (res.ok) {
    const data = await res.json();
    token = data.access_token;
    showTaskForm();
    loadTasks();
  } else {
    alert("Login failed");
  }
});

// Signup
signupForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("signup-email").value;
  const password = document.getElementById("signup-password").value;

  const res = await fetch(`${API_BASE}/auth/signup`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({email, password})
  });

  if (res.ok) {
    alert("Signup successful! Please login.");
  } else {
    alert("Signup failed");
  }
});

// This function loads tasks from the backend and displays them on the page
async function loadTasks() {
  // Fetch tasks from the backend API
  const res = await fetch(`${API_BASE}/tasks/`, {
    headers: { "Authorization": "Bearer ${token}"}
  });
  const tasks = await res.json(); // Parse the JSON response

  // Clear any previously rendered tasks
  taskList.innerHTML = "";

  // Loop through each task and create elements in the DOM
  tasks.forEach((task) => {
    // Create a new <li> element to hold this task
    const li = document.createElement("li");

    // 1. Create a checkbox for marking task as complete
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed; // Set the checkbox based on the task's current state

    // When checkbox changes (user marks/unmarks task), update it on the backend
    checkbox.addEventListener("change", async () => {
      await fetch(`${API_BASE}/tasks/${task.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json",
                    "Authorization": "Bearer ${token}"
        },
        body: JSON.stringify({ completed: checkbox.checked }),
      });
      loadTasks(); // Reload the tasks to reflect the updated state
    });

    // 2. Create a <span> to display the task text
    const textSpan = document.createElement("span");
    textSpan.textContent = task.title;

    // If the task is completed, add a visual style (like strikethrough)
    if (task.completed) {
      textSpan.style.textDecoration = "line-through";
      textSpan.style.color = "gray";
    }

    // 3. Create a delete button to remove the task
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";

    // When the button is clicked, send a DELETE request to the backend
    deleteBtn.addEventListener("click", async () => {
      await fetch(`${API_BASE}/tasks/${task.id}`, {
        method: "DELETE",
        headers: { "Authorization": "Bearer ${token}"}
      });
      loadTasks(); // Refresh the list to remove the deleted task
    });

    // Append all parts (checkbox, text, delete button) into the <li>
    li.appendChild(checkbox);
    li.appendChild(textSpan);
    li.appendChild(deleteBtn);
    taskList.appendChild(li);

    // Add this <li> to the overall task list
    taskList.appendChild(li);
  });
}

// This handles the form submission when a new task is added
taskForm.addEventListener("submit", async (e) => {
  e.preventDefault(); // Prevent the form from reloading the page
  const task = taskInput.value; // Get the task the user typed

  // Send a POST request to add the new task to the backend
  await fetch(`${API_BASE}/tasks/`, {
    method: "POST",
    headers: { "Content-Type": "application/json",
                "Auhorization": "Bearer ${token}"
    },
    body: JSON.stringify({ title: task }),
  });

  // Clear the input box
  taskInput.value = "";

  // Reload the task list to show the new task
  loadTasks();
});

// When the page first loads, fetch and display all existing tasks
loadTasks();
