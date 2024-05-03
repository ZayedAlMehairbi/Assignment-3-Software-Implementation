import tkinter as tk
from tkinter import ttk, messagebox
import pickle
from tkinter import simpledialog


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

    def load_data(self):
        # List of entities to manage
        self.entities = ["event", "guest", "supplier", "client", "venue", "employee"]
        self.data = {}
        for entity in self.entities:
            try:
                with open(f"{entity}.pkl", "rb") as f:
                    self.data[entity] = pickle.load(f)
            except FileNotFoundError:
                self.data[entity] = {}  # Ensure each entity type is initialized as an empty dictionary

    def save_data(self):
        # Save data to binary files
        for entity, items in self.data.items():
            with open(f"{entity}.pkl", "wb") as f:
                pickle.dump(items, f)

    def add_buttons(self):
        # List of entities to manage
        self.entities = ["event", "guest", "supplier", "client", "venue", "employee"]
        actions = ["Add", "Delete", "Modify", "Display", "Display by ID"]

        for row, entity in enumerate(self.entities):
            for col, action in enumerate(actions):
                button = ttk.Button(self.main_frame, text=f"{action.capitalize()} {entity.capitalize()}",
                                    command=lambda action=action, entity=entity: self.perform_action(action, entity))
                button.grid(row=row, column=col, padx=5, pady=5, sticky="ew")

    def perform_action(self, action, entity):
        if action in ["Add", "Delete", "Modify"]:
            self.modify_entity(entity, action)
        elif action == "Display":
            self.display_all_entities(entity)
        elif action == "Display by ID":
            self.display_entity_by_id(entity)

    def modify_entity(self, entity, action):
        # Create a new window for adding or modifying entity details
        modify_window = tk.Toplevel(self.master)
        modify_window.title(f"{action.capitalize()} {entity.capitalize()} Details")

        # Depending on the action, set up the window differently
        if action != "Delete":
            self.setup_modify_window(modify_window, entity, action)
        else:
            self.setup_delete_window(modify_window, entity)

    def setup_modify_window(self, modify_window, entity, action):
        # Add labels and entry fields for input, predefined fields depend on the entity type
        fields = ["ID", "Name", "Address", "Contact Details", "Budget"] if entity in ["client", "supplier"] else ["ID",
                                                                                                                  "Name",
                                                                                                                  "Date",
                                                                                                                  "Venue"]
        entry_widgets = {}
        for i, field in enumerate(fields):
            tk.Label(modify_window, text=f"{field}:").grid(row=i, column=0)
            entry = tk.Entry(modify_window)
            entry.grid(row=i, column=1)
            entry_widgets[field.lower()] = entry

        # Add button to confirm addition or modification
        confirm_button = ttk.Button(modify_window, text=action.capitalize(),
                                    command=lambda: self.confirm_modify(entity, entry_widgets, action, modify_window))
        confirm_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

    def setup_delete_window(self, modify_window, entity):
        tk.Label(modify_window, text="ID:").grid(row=0, column=0)
        id_entry = tk.Entry(modify_window)
        id_entry.grid(row=0, column=1)

        delete_button = ttk.Button(modify_window, text="Delete",
                                   command=lambda: self.confirm_delete(entity, id_entry.get(), modify_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def confirm_modify(self, entity, entry_widgets, action, window):
        id_value = entry_widgets["id"].get()
        if not id_value:
            messagebox.showerror("Error", "ID is required.")
            window.destroy()
            return

        details = {field: widget.get() for field, widget in entry_widgets.items() if widget.get()}

        try:
            if action == "Add":
                if id_value in self.data[entity]:
                    messagebox.showerror("Error", "ID already exists.")
                    window.destroy()
                    return
                self.data[entity][id_value] = details  # Add new entry

            elif action == "Modify":
                if id_value not in self.data[entity]:
                    messagebox.showerror("Error", "ID does not exist.")
                    window.destroy()
                    return
                self.data[entity][id_value].update(details)  # Update existing entry

            self.save_data()
            messagebox.showinfo("Success",
                                f"{entity.capitalize()} details {'added' if action == 'Add' else 'modified'} successfully.")
            window.destroy()

        except KeyError as e:
            messagebox.showerror("Error", f"Error modifying data: {str(e)}")
            window.destroy()

    def display_all_entities(self, entity):
        # Check if there are any entries for the given entity
        if not self.data[entity]:
            messagebox.showinfo("Display All", f"No {entity} data available.")
            return

        # Compile entity details into a readable string
        details_str = f"All {entity.capitalize()}s:\n\n"
        for id, details in self.data[entity].items():
            details_str += f"ID: {id}\n"
            for key, value in details.items():
                details_str += f"{key.capitalize()}: {value}\n"
            details_str += "\n"

        # Display the compiled details
        messagebox.showinfo(f"All {entity.capitalize()}s", details_str)

    def display_entity_by_id(self, entity):
        # Create a simple input dialog to get the entity ID from the user
        id = simpledialog.askstring("Input", f"Enter {entity} ID:", parent=self.master)
        if id is None or id.strip() == "":
            return  # User cancelled or entered an empty string

        # Check if the ID exists within the data
        if id in self.data[entity]:
            details = self.data[entity][id]
            details_str = f"Details for {entity.capitalize()} ID {id}:\n\n"
            for key, value in details.items():
                details_str += f"{key.capitalize()}: {value}\n"

            messagebox.showinfo(f"{entity.capitalize()} Details", details_str)
        else:
            messagebox.showerror("Error", f"{entity.capitalize()} with ID {id} not found.")


def main():
    root = tk.Tk()
    app = EventManagementSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
