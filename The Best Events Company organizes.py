import pickle  # Importing the pickle module for serialization
import tkinter as tk  # Importing the tkinter module for GUI development
from tkinter import simpledialog, messagebox  # Importing specific classes from tkinter for dialog boxes


# Define the Employee class
class Employee:
    def __init__(self, employee_id, name, department, job_title, basic_salary, manager_id=None):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.manager_id = manager_id

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Department: {self.department}, Job Title: {self.job_title}, Basic Salary: {self.basic_salary}, Manager ID: {self.manager_id}"


# Define the Client class
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def __str__(self):
        return f"Client ID: {self.client_id}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}, Budget: {self.budget}"


# Define the Event class
class Event:
    def __init__(self, event_id, type, theme, date, time, duration, venue_id, client_id, caterer_id=None,
                 cleaning_company_id=None, decorations_company_id=None, entertainment_company_id=None,
                 furniture_supply_company_id=None, invoice=None):
        self.event_id = event_id
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_id = venue_id
        self.client_id = client_id
        self.caterer_id = caterer_id
        self.cleaning_company_id = cleaning_company_id
        self.decorations_company_id = decorations_company_id
        self.entertainment_company_id = entertainment_company_id
        self.furniture_supply_company_id = furniture_supply_company_id
        self.invoice = invoice

    def __str__(self):
        return f"Event ID: {self.event_id}, Type: {self.type}, Theme: {self.theme}, Date: {self.date}, Time: {self.time}, Duration: {self.duration}, Venue ID: {self.venue_id}, Client ID: {self.client_id}, Caterer ID: {self.caterer_id}, Cleaning Company ID: {self.cleaning_company_id}, Decorations Company ID: {self.decorations_company_id}, Entertainment Company ID: {self.entertainment_company_id}, Furniture Supply Company ID: {self.furniture_supply_company_id}, Invoice: {self.invoice}"


# Define the Guest class
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def __str__(self):
        return f"Guest ID: {self.guest_id}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}"


# Define the Supplier class
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, specialization):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.specialization = specialization

    def __str__(self):
        return f"Supplier ID: {self.supplier_id}, Name: {self.name}, Address: {self.address}, Contact Details: {self.contact_details}, Specialization: {self.specialization}"


# Define the Venue class
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    def __str__(self):
        return f"Venue ID: {self.venue_id}, Name: {self.name}, Address: {self.address}, Contact: {self.contact}, Min Guests: {self.min_guests}, Max Guests: {self.max_guests}"


# Define the EventManagementSystemGUI class
class EventManagementSystemGUI:
    def __init__(self):
        # Initialize the GUI
        self.root = tk.Tk()
        self.root.title("Event Management System")
        # Create navigation menu
        self.create_navigation_menu()

    def create_navigation_menu(self):
        # Create a frame for navigation menu
        self.navigation_frame = tk.Frame(self.root)
        self.navigation_frame.pack(padx=10, pady=5)
        # Add buttons for different functionalities
        tk.Button(self.navigation_frame, text="Add Employee", command=self.show_add_employee).grid(row=0, column=0,
                                                                                                   padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Add Client", command=self.show_add_client).grid(row=0, column=1, padx=5,
                                                                                               pady=2)
        tk.Button(self.navigation_frame, text="Add Event", command=self.show_add_event).grid(row=0, column=2, padx=5,
                                                                                             pady=2)
        tk.Button(self.navigation_frame, text="Add Guest", command=self.show_add_guest).grid(row=0, column=3, padx=5,
                                                                                             pady=2)
        tk.Button(self.navigation_frame, text="Add Supplier", command=self.show_add_supplier).grid(row=0, column=4,
                                                                                                   padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Add Venue", command=self.show_add_venue).grid(row=0, column=5, padx=5,
                                                                                             pady=2)
        tk.Button(self.navigation_frame, text="Display Employee", command=self.show_display_employee).grid(row=1,
                                                                                                           column=0,
                                                                                                           padx=5,
                                                                                                           pady=2)
        tk.Button(self.navigation_frame, text="Display Client", command=self.show_display_client).grid(row=1, column=1,
                                                                                                       padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Display Event", command=self.show_display_event).grid(row=1, column=2,
                                                                                                     padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Display Guest", command=self.show_display_guest).grid(row=1, column=3,
                                                                                                     padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Display Supplier", command=self.show_display_supplier).grid(row=1,
                                                                                                           column=4,
                                                                                                           padx=5,
                                                                                                           pady=2)
        tk.Button(self.navigation_frame, text="Display Venue", command=self.show_display_venue).grid(row=1, column=5,
                                                                                                     padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Delete Employee", command=self.show_delete_employee).grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Delete Client", command=self.show_delete_client).grid(row=2, column=1,
                                                                                                     padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Delete Event", command=self.show_delete_event).grid(row=2, column=2,
                                                                                                   padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Delete Guest", command=self.show_delete_guest).grid(row=2, column=3,
                                                                                                   padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Delete Supplier", command=self.show_delete_supplier).grid(row=2,
                                                                                                         column=4,
                                                                                                         padx=5, pady=2)
        tk.Button(self.navigation_frame, text="Delete Venue", command=self.show_delete_venue).grid(row=2, column=5,
                                                                                                   padx=5, pady=2)

    # Functions to show forms for adding different entities
    def show_add_employee(self):
        self.clear_frame()
        self.create_entity_form(Employee)

    def show_add_client(self):
        self.clear_frame()
        self.create_entity_form(Client)

    def show_add_event(self):
        self.clear_frame()
        self.create_entity_form(Event)

    def show_add_guest(self):
        self.clear_frame()
        self.create_entity_form(Guest)

    def show_add_supplier(self):
        self.clear_frame()
        self.create_entity_form(Supplier)

    def show_add_venue(self):
        self.clear_frame()
        self.create_entity_form(Venue)

    # Functions to display entities
    def show_display_employee(self):
        self.clear_frame()
        self.display_entity("employees.pkl", "Employees")

    def show_display_client(self):
        self.clear_frame()
        self.display_entity("clients.pkl", "Clients")

    def show_display_event(self):
        self.clear_frame()
        self.display_entity("events.pkl", "Events")

    def show_display_guest(self):
        self.clear_frame()
        self.display_entity("guests.pkl", "Guests")

    def show_display_supplier(self):
        self.clear_frame()
        self.display_entity("suppliers.pkl", "Suppliers")

    def show_display_venue(self):
        self.clear_frame()
        self.display_entity("venues.pkl", "Venues")

    # Functions to delete entities
    def show_delete_employee(self):
        self.delete_entity("employees.pkl", "Employee")

    def show_delete_client(self):
        self.delete_entity("clients.pkl", "Client")

    def show_delete_event(self):
        self.delete_entity("events.pkl", "Event")

    def show_delete_guest(self):
        self.delete_entity("guests.pkl", "Guest")

    def show_delete_supplier(self):
        self.delete_entity("suppliers.pkl", "Supplier")

    def show_delete_venue(self):
        self.delete_entity("venues.pkl", "Venue")

    # Function to create a form for adding entities
    def create_entity_form(self, entity_class):
        self.entity_form_frame = tk.Frame(self.root)
        self.entity_form_frame.pack(padx=10, pady=5)
        entity = entity_class(None, None, None, None, None)  # Initialize with None values for all attributes
        attributes = [attr for attr in dir(entity) if not callable(getattr(entity, attr)) and not attr.startswith("__")]
        for i, attribute in enumerate(attributes):
            tk.Label(self.entity_form_frame, text=f"{attribute.replace('_', ' ').title()}:").grid(row=i, column=0,
                                                                                                  padx=5, pady=2)
            setattr(self, f"{attribute}_entry", tk.Entry(self.entity_form_frame))
            getattr(self, f"{attribute}_entry").grid(row=i, column=1, padx=5, pady=2)
        tk.Button(self.entity_form_frame, text=f"Add {entity_class.__name__}",
                  command=lambda: self.add_entity(entity_class)).grid(row=len(attributes), columnspan=2, padx=5, pady=2)

    # Function to add an entity
    def add_entity(self, entity_class):
        attributes = self.get_entity_attributes(entity_class)
        if None in attributes:  # Check if any required fields are missing
            messagebox.showerror("Error", "All required fields are needed.")
            return
        entity = entity_class(*attributes)
        entities = self.load_data(f"{entity_class.__name__.lower()}s.pkl")
        entities.append(entity)
        self.save_data(entities, f"{entity_class.__name__.lower()}s.pkl")
        messagebox.showinfo("Success", f"{entity_class.__name__} added successfully.")
        self.clear_frame()

    # Function to display entities
    def display_entity(self, filename, entity_name):
        entities = self.load_data(filename)
        if entities:
            for entity in entities:
                print(entity)
        else:
            messagebox.showinfo("Information", f"No {entity_name} available.")

    # Function to delete an entity
    def delete_entity(self, filename, entity_name):
        item_id = simpledialog.askstring(f"Delete {entity_name}", f"Enter {entity_name} ID to delete:")
        if item_id:
            entities = self.load_data(filename)
            index = self.get_index_by_id(entities, item_id)
            if index != -1:
                del entities[index]
                self.save_data(entities, filename)
                messagebox.showinfo("Information", f"{entity_name} deleted successfully.")
            else:
                messagebox.showerror("Error", f"{entity_name} with ID {item_id} not found.")

    # Function to clear the frame
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Function to save data to a file
    def save_data(self, data, filename):
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    # Function to load data from a file
    def load_data(self, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    # Function to get the index of an entity by its ID
    def get_index_by_id(self, data, item_id):
        for index, item in enumerate(data):
            if getattr(item, f"{item.__class__.__name__.lower()}_id") == item_id:
                return index
        return -1

    # Function to get attributes of an entity from the form
    def get_entity_attributes(self, entity_class):
        attributes = []
        for attr in dir(entity_class):
            if not callable(getattr(entity_class, attr)) and not attr.startswith("__"):
                attributes.append(getattr(self, f"{attr}_entry").get())
        return attributes

    # Function to run the GUI
    def run(self):
        self.root.mainloop()


# Entry point of the program
if __name__ == "__main__":
    app = EventManagementSystemGUI()
    app.run()

