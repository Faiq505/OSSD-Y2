import tkinter as tk
from tkinter import messagebox

# Global variables to access input entry data safely across functions
username_entry = None
password_entry = None

def clear_window():
    """Destroys all active widgets on the screen to prepare for a new window view."""
    for widget in root.winfo_children():
        widget.destroy()

def save_credentials():
    """Validates inputs and saves new credentials into a local text file."""
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    if not username or not password:
        messagebox.showerror("Registration Error", "Both username and password are required!")
        return
        
    # Append the user credentials in a CSV format
    with open("credentials.txt", "a") as f:
        f.write(f"{username},{password}\n")
        
    messagebox.showinfo("Success", "Account created successfully! You can now sign in.")
    
    # Clear fields for convenience
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def check_credentials():
    """Verifies user login and forwards them to the customized main menu."""
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    
    try:
        with open("credentials.txt", "r") as f:
            lines = f.readlines()
            
        for line in lines:
            stored_user, stored_pass = line.strip().split(",")
            if username == stored_user and password == stored_pass:
                # Login matches successfully -> load main menu with the logged-in username
                main_menu_window(username)
                return
                
        messagebox.showerror("Access Denied", "Invalid username or password.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No registered users found. Create an account first!")

def main_menu_window(user_name):
    """Clears the authentication page and loads the main dashboard with personalized data."""
    clear_window()
    root.title("Dashboard")
    root.geometry("350x250")
    
    # Personalized Welcome Label using the logged-in username
    tk.Label(root, text=f"Hi {user_name}", font=("Arial", 16, "bold"), fg="#2c3e50").pack(pady=20)
    
    # Dummy Button 1
    tk.Button(root, text="Feature One", width=18, command=lambda: messagebox.showinfo("Dummy", "Feature 1 coming soon!")).pack(pady=5)
    
    # Dummy Button 2
    tk.Button(root, text="Feature Two", width=18, command=lambda: messagebox.showinfo("Dummy", "Feature 2 coming soon!")).pack(pady=5)
    
    # Sign Out Button - sends user directly back to the sign-in routine
    tk.Button(root, text="Sign Out", width=18, bg="#e74c3c", fg="white", command=signin_window).pack(pady=15)

def signin_window():
    """Builds the primary Portal Interface for registering/signing in."""
    global username_entry, password_entry
    clear_window()
    
    root.title("Authentication System")
    root.geometry("300x260")
    
    tk.Label(root, text="Login / Signup System", font=("Arial", 12, "bold")).pack(pady=10)
    
    # Username UI Elements
    tk.Label(root, text="Username:").pack(anchor="w", padx=40)
    username_entry = tk.Entry(root)
    username_entry.pack(fill="x", padx=40, pady=2)
    
    # Password UI Elements
    tk.Label(root, text="Password:").pack(anchor="w", padx=40)
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(fill="x", padx=40, pady=2)
    
    # Interface Submission Control Buttons
    tk.Button(root, text="Sign In", bg="#2ecc71", fg="white", command=check_credentials).pack(fill="x", padx=40, pady=8)
    tk.Button(root, text="Create Account", bg="#3498db", fg="white", command=save_credentials).pack(fill="x", padx=40, pady=2)

# Global initializations 
root = tk.Tk()
signin_window()
root.mainloop()