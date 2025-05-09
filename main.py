import tkinter as tk
from tkinter import messagebox
import webbrowser
import difflib
from mosque import Mosque

db = Mosque()



# === Functions ===
def display_all():
    listbox.delete(0, tk.END)
    records = db.Display()
    for rec in records:
        listbox.insert(tk.END, rec)

def search_by_name():
    name = entries['Name'].get()
    rec = db.Search(name)
    listbox.delete(0, tk.END)
    if rec:
        listbox.insert(tk.END, rec)
    else:
        all_names = [r[1] for r in db.Display()]
        close = difflib.get_close_matches(name, all_names, n=1, cutoff=0.6)
        if close:
            messagebox.showinfo("Did you mean?", f"Did you mean: {close[0]}?")
        else:
            messagebox.showinfo("Not Found", "No similar mosque name found.")

def add_entry():
    ID_str = entries['ID'].get()
    if not ID_str.isdigit():
        messagebox.showerror("Error", "Invalid ID")
        return
    ID = int(ID_str)

    name = entries['Name'].get()
    type_ = entries['Type'].get()
    address = entries['Address'].get()
    coordinates = entries['Coordinates'].get()
    imam_name = entries['Imam_name'].get()

    # Check duplicate ID
    existing_ids = [r[0] for r in db.Display()]
    if ID in existing_ids:
        messagebox.showerror("Error", f"Mosque with ID {ID} already exists.")
        return

    # Validate coordinates
    if "," not in coordinates:
        messagebox.showerror("Invalid Coordinates",
                             "Please enter coordinates in this format:\n25.276987, 55.296249")
        return

    lat_lon = coordinates.split(",")
    if len(lat_lon) != 2:
        messagebox.showerror("Invalid Coordinates",
                             "Coordinates should be in the format: Latitude, Longitude")
        return

    lat_str, lon_str = lat_lon[0].strip(), lat_lon[1].strip()
    if not (lat_str.replace('.', '', 1).replace('-', '', 1).isdigit() and
            lon_str.replace('.', '', 1).replace('-', '', 1).isdigit()):
        messagebox.showerror("Invalid Coordinates",
                             "Latitude and Longitude should be numeric.")
        return

    lat = float(lat_str)
    lon = float(lon_str)
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        messagebox.showerror("Invalid Coordinates",
                             "Latitude must be between -90 and 90, Longitude between -180 and 180.")
        return

    db.Insert(ID, name, type_, address, coordinates, imam_name)
    display_all()

def delete_entry():
    ID_str = entries['ID'].get()
    if not ID_str.isdigit():
        messagebox.showerror("Error", "Invalid ID")
        return
    ID = int(ID_str)
    db.Delete(ID)
    display_all()

def update_entry():
    ID_str = entries['ID'].get()
    if not ID_str.isdigit():
        messagebox.showerror("Error", "Invalid ID")
        return
    ID = int(ID_str)
    imam_name = entries['Imam_name'].get()
    db.Update(ID, imam_name)
    display_all()

def display_on_map():
    name = entries['Name'].get()
    rec = db.Search(name)
    if rec:
        coordinates = rec[4]
        webbrowser.open(f"https://www.google.com/maps/search/?api=1&query={coordinates}")
    else:
        messagebox.showinfo("Not Found", "No mosque with that name found.")



#making the GUI
root = tk.Tk()
root.title("Mosques Management System")


#making the frames 
part1 = tk.Frame(root, bd=2)
part1.grid(row=0, column=0, padx=5, pady=5, sticky='nw')

part2 = tk.Frame(root, bd=2)
part2.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

part3 = tk.Frame(root, bd=2)
part3.grid(row=1, column=0, padx=5, pady=5, sticky='w')

part4 = tk.Frame(part3)
part4.grid(row=1, column=2, padx=5, pady=5, sticky='e')

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

#making part 1
labels = ['ID', 'Name', 'Type', 'Address', 'Coordinates', 'Imam_name']
entries = {}
type_options = ["Jami", "Musalla", "Masjid", "Other"]

for i, label in enumerate(labels):
    tk.Label(part1, text=label).grid(row=i, column=0, padx=5, pady=2, sticky='w')
    if label == 'Type':
        var = tk.StringVar(root)
        var.set(type_options[0])
        dropdown = tk.OptionMenu(part1, var, *type_options)
        dropdown.grid(row=i, column=1, padx=5, pady=2, sticky='we')
        entries[label] = var
    else:
        entry = tk.Entry(part1)
        entry.grid(row=i, column=1, padx=5, pady=2)
        entries[label] = entry

#making Part 2 
listbox = tk.Listbox(part2, width=80)
listbox.pack(fill='both', expand=True)



#making Part 3
tk.Button(part3, text="Display All", width=15, command=display_all).grid(row=0, column=0, padx=5, pady=2)
tk.Button(part3, text="Search By Name", width=15, command=search_by_name).grid(row=0, column=1, padx=5, pady=2)
tk.Button(part3, text="Update Entry", width=15, command=update_entry).grid(row=0, column=2, padx=5, pady=2)

tk.Button(part3, text="Add Entry", width=15, command=add_entry).grid(row=1, column=0, padx=5, pady=2)
tk.Button(part3, text="Delete entry", width=15, command=delete_entry).grid(row=1, column=1, padx=5, pady=2)

#making Part 4
tk.Button(part4, text="Display on Map", width=15, command=display_on_map).pack()

root.mainloop()
