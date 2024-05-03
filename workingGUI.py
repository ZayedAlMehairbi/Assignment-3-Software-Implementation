import tkinter as tk
from tkinter import ttk, messagebox
import pickle

class EventManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Event Management System")
        
        # Create a frame for better organization
        self.main_frame = ttk.Frame(self.master)
        self.main_frame.grid(row=0, column=0)

        # Load existing data or create empty data
        self.load_data()

        # Create buttons for each action for each entity
        self.add_buttons()

        # Create a button to display all events
        self.display_all_events_button = ttk.Button(self.main_frame, text="Display All Events", command=self.display_all_events)
        self.display_all_events_button.grid(row=len(self.entities) + 1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    def load_data(self):
        # Try loading data from binary files, if they exist
        try:
            with open("events.pkl", "rb") as f:
                self.events = pickle.load(f)
        except FileNotFoundError:
            self.events = {}
        
        try:
            with open("guests.pkl", "rb") as f:
                self.guests = pickle.load(f)
        except FileNotFoundError:
            self.guests = {}
        
        # Add loading for other entities similarly

    def save_data(self):
        # Save data to binary files
        with open("events.pkl", "wb") as f:
            pickle.dump(self.events, f)
        
        with open("guests.pkl", "wb") as f:
            pickle.dump(self.guests, f)

        # Add saving for other entities similarly

    def add_buttons(self):
        self.entities = ["Event", "Guest", "Supplier", "Client", "Venue", "Employee"]
        actions = ["Add", "Delete", "Modify"]

        for row, entity in enumerate(self.entities):
            for col, action in enumerate(actions):
                button = ttk.Button(self.main_frame, text=f"{action} {entity}", command=lambda action=action, entity=entity: self.perform_action(action, entity))
                button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

    def perform_action(self, action, entity):
        if action == "Add":
            self.add_entity(entity)
        elif action == "Delete":
            self.delete_entity(entity)
        elif action == "Modify":
            self.modify_entity(entity)

    def add_entity(self, entity):
        # Create a new window for adding details
        add_window = tk.Toplevel(self.master)
        add_window.title(f"Add {entity} Details")

        # Add labels and entry fields for input
        labels = ["Name", "Address", "Contact details", "Budget"] if entity == "Client" else ["Name", "Address", "Contact details", "Menu"]
        entry_widgets = {}
        for i, label_text in enumerate(labels):
            tk.Label(add_window, text=label_text + ":").grid(row=i, column=0)
            entry = tk.Entry(add_window)
            entry.grid(row=i, column=1)
            entry_widgets[label_text.lower()] = entry

        # Add an "Add" button to confirm adding details
        add_button = ttk.Button(add_window, text="Add", command=lambda: self.add_confirm(add_window, entry_widgets, entity))
        add_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def add_confirm(self, add_window, entry_widgets, entity):
        # Implement functionality to confirm adding details
        details = {}
        for label_text, entry in entry_widgets.items():
            details[label_text] = entry.get()

        # Update data dictionary with new details
        if entity == "Event":
            self.events[len(self.events) + 1] = details
        elif entity == "Guest":
            self.guests[len(self.guests) + 1] = details
        # Add other entities similarly

        self.save_data()  # Save data to binary files
        messagebox.showinfo("Add Details", f"Added details: {details}")
        add_window.destroy()

    def delete_entity(self, entity):
        # Display a message when the user clicks "Delete"
        messagebox.showinfo("Delete", f"Deleted {entity}")
        # Placeholder for deleting details using UML classes

    def modify_entity(self, entity):
        # Create a new window for modifying details
        modify_window = tk.Toplevel(self.master)
        modify_window.title(f"Modify {entity} Details")

        # Add labels and entry fields with previous values for input
        previous_values = self.get_previous_values(entity)
        entry_widgets = {}
        for i, (attribute, value) in enumerate(previous_values.items()):
            tk.Label(modify_window, text=f"{attribute}:").grid(row=i, column=0)
            entry = tk.Entry(modify_window)
            entry.insert(tk.END, value)
            entry.grid(row=i, column=1)
            entry_widgets[attribute.lower()] = entry

        # Add a button to confirm modifying details
        modify_button = ttk.Button(modify_window, text="Modify", command=lambda: self.modify_confirm(previous_values, modify_window))
        modify_button.grid(row=len(previous_values), column=0, columnspan=2)

    def get_previous_values(self, entity):
        # Placeholder function to get previous values for the specified entity
        # Replace this with actual functionality to retrieve previous values
        return {
            "Name": "Previous Name",
            "Address": "Previous Address",
            "Contact details": "Previous Contact",
            "Budget": "Previous Budget"
            # Add other attributes as needed
        }

    def modify_confirm(self, previous_values, modify_window):
        # Implement functionality to confirm modifying details
        messagebox.showinfo("Modify Details", "Details modified successfully")
        # Placeholder for saving modified details using UML classes
        modify_window.destroy()

    def display_all_events(self):
        # Display all event details
        details_str = ""
        for key, value in self.events.items():
            details_str += f"Event {key} Details:\n"
            for attribute, val in value.items():
                details_str += f"{attribute}: {val}\n"
            details_str += "\n"

        # Show the details in a message box
        messagebox.showinfo("All Events Details", details_str)

def main():
    root = tk.Tk()
    app = EventManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()