import tkinter as tk

# 1. Global counter variable
count = 0


# 2. Functions to handle button clicks
def increment():
    global count
    count += 1
    counter_label.config(text=str(count))  # Updates the label text


def decrement():
    global count
    count -= 1
    counter_label.config(text=str(count))


def reset():
    global count
    count = 0
    counter_label.config(text=str(count))


# 3. Initialize the main window
root = tk.Tk()
root.title("Counter App")
root.geometry("200x200")

# 4. Create the widgets (Notice we separate creation from packing!)
counter_label = tk.Label(root, text="0", font=("Arial", 24))
counter_label.pack(pady=10)

# Connect the buttons to their respective functions using 'command'
btn_increment = tk.Button(root, text="Increment", command=increment)
btn_increment.pack(pady=2)

btn_decrement = tk.Button(root, text="Decrement", command=decrement)
btn_decrement.pack(pady=2)

btn_reset = tk.Button(root, text="Reset", command=reset)
btn_reset.pack(pady=2)

# 5. Keep the window open and responsive
root.mainloop()