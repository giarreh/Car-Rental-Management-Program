from tkinter import *
import requests


def main():
    def add_customer_window():
        customer_window = Toplevel(root)

        # Customers name
        cust_name = Label(customer_window, text="Customer's name:", font="none 12 bold")
        cust_name.pack(padx=20)
        text_entry_name = Entry(customer_window, width=20, bg="white")
        text_entry_name.pack(padx=20)

        # Customers email address
        cust_email = Label(customer_window, text="Customer's email:", font="none 12 bold")
        cust_email.pack(padx=20)
        text_entry_email = Entry(customer_window, width=20, bg="white")
        text_entry_email.pack(padx=20)

        # Customers phone number
        cust_phone_number = Label(customer_window, text="Customer's phone number:", font="none 12 bold")
        cust_phone_number.pack(padx=20)
        text_entry_phone = Entry(customer_window, width=20, bg="white")
        text_entry_phone.pack(padx=20)

        # Button for submitting entries to database
        def submitClick():
            comment = dict(id=len(requests.get('http://localhost:5000/customers/').json()) + 1,
                           name=text_entry_name.get(),
                           email=text_entry_email.get(), phone_number=text_entry_phone.get())
            new_customer = requests.post('http://localhost:5000/customers/', json=comment)

        btn_submit = Button(customer_window, text="SUBMIT\nCUSTOMER", width=9, command=submitClick)
        btn_submit.pack(padx=20)

    def destroy_customer_window():
        destroy_customer = Toplevel(root)
        # destroy customer label
        lbl = Label(destroy_customer, text="Enter the ID of customer you wish to remove from the database",
                    font="none 12 bold")
        lbl.pack(padx=20, pady=20)
        # Destroy customer entry
        destroy_customer_text = Entry(destroy_customer, width=20, bg="white")
        destroy_customer_text.pack(padx=20)

        def destroyClick():
            # Deletes customer with selected ID from entry
            requests.delete(f'http://localhost:5000/customers/{destroy_customer_text.get()}')

        # Destroy button
        btn_destroy = Button(destroy_customer, text="Delete", width=10, command=destroyClick)
        btn_destroy.pack(padx=20)

    def edit_customer_window():
        edit_customer = Toplevel(root)
        # Id of customer
        lbl = Label(edit_customer, text="ID of customer you wish to change:", font="none 12 bold")
        lbl.pack(padx=20)
        customer_id_text = Entry(edit_customer, width=20, bg="white")
        customer_id_text.pack(padx=20)

        # New customer's name
        lbl_name = Label(edit_customer, text="New name of customer:", font="none 12 bold")
        lbl_name.pack(padx=20)
        customer_new_name = Entry(edit_customer, width=20, bg="white")
        customer_new_name.pack(padx=20)

        # New customer's email
        lbl_email = Label(edit_customer, text="New email of customer:", font="none 12 bold")
        lbl_email.pack(padx=20)
        customer_new_email = Entry(edit_customer, width=20, bg="white")
        customer_new_email.pack(padx=20)

        # New customer's phone number
        lbl_phone_number = Label(edit_customer, text="New phone number of customer:", font="none 12 bold")
        lbl_phone_number.pack(padx=20)
        customer_new_phone_number = Entry(edit_customer, width=20, bg="white")
        customer_new_phone_number.pack(padx=20)

        # Apply changes with button
        def applyClick():
            comment = dict(id=customer_id_text.get(), name=customer_new_name.get(), email=customer_new_email.get(),
                           phone_number=customer_new_phone_number.get())
            edit_customers = requests.put(f'http://localhost:5000/customers/{customer_id_text.get()}', json=comment)

        # Apply changes with button
        btn_apply = Button(edit_customer, text="Apply\nChanges", command=applyClick)
        btn_apply.pack(padx=20)

    def add_car_window():
        # New window
        car_window = Toplevel(root)

        # Car's brand
        car_brand = Label(car_window, text="Car's brand:", font="none 12 bold")
        car_brand.pack(padx=20)
        car_brand_entry = Entry(car_window, width=20, bg="white")
        car_brand_entry.pack(padx=20)

        # Car's model
        car_model = Label(car_window, text="Car's model", font="none 12 bold")
        car_model.pack(padx=20)
        car_model_entry = Entry(car_window, width=20, bg="white")
        car_model_entry.pack(padx=20)

        # Car's year model
        car_year = Label(car_window, text="Car's year model", font="none 12 bold")
        car_year.pack(padx=20)
        car_year_entry = Entry(car_window, width=20, bg="white")
        car_year_entry.pack(padx=20)

        # Car's color
        car_color = Label(car_window, text="Car's color", font="none 12 bold")
        car_color.pack(padx=20)
        car_color_entry = Entry(car_window, width=20, bg="white")
        car_color_entry.pack(padx=20)

        def addCar():
            # Add cars with attributes from entry boxes
            comment = dict(id=len(requests.get('http://localhost:5000/cars/').json()) + 1,
                           brand=car_brand_entry.get(),
                           model=car_model_entry.get(), year_model=car_year_entry.get(), color=car_color_entry.get(),
                           customer_id=None)
            # post request
            new_car = requests.post('http://localhost:5000/cars/', json=comment)
        # Button to commit car
        btn_add_car = Button(car_window, text="ADD CAR", command=addCar)
        btn_add_car.pack(padx=20)

    def remove_car_window():
        # New window
        remove_car = Toplevel(root)

        # Enter car ID to remove
        lbl = Label(remove_car, text="Enter the ID of the car you wish to remove from the database", font="none 12 bold")
        lbl.pack(padx=20, pady=20)
        # Entry for car ID
        remove_car_entry = Entry(remove_car, width=20, bg="white")
        remove_car_entry.pack(padx=20)

        def removeClick():
            # Remove car from database
            requests.delete(f'http://localhost:5000/cars/{remove_car_entry.get()}')
        # Button to delete car from ID
        btn_remove_car = Button(remove_car, text="Delete", width=10, command=removeClick)
        btn_remove_car.pack(padx=20)

    def edit_car_window():
        edit_car = Toplevel(root)

        # Id of customer
        lbl = Label(edit_car, text="ID of car you wish to change:", font="none 12 bold")
        lbl.pack(padx=20)
        car_id_text = Entry(edit_car, width=20, bg="white")
        car_id_text.pack(padx=20)

        # Edit car brand
        lbl_brand = Label(edit_car, text="Edit brand of car:", font="none 12 bold")
        lbl_brand.pack(padx=20)
        car_new_brand = Entry(edit_car, width=20, bg="white")
        car_new_brand.pack(padx=20)

        # Edit car's model
        lbl_model = Label(edit_car, text="Edit model of car:", font="none 12 bold")
        lbl_model.pack(padx=20)
        car_new_model = Entry(edit_car, width=20, bg="white")
        car_new_model.pack(padx=20)

        # Edit car's year model
        lbl_year_model = Label(edit_car, text="Edit year model of car:", font="none 12 bold")
        lbl_year_model.pack(padx=20)
        car_new_year_model = Entry(edit_car, width=20, bg="white")
        car_new_year_model.pack(padx=20)

        lbl_color = Label(edit_car, text="Edit car color:", font="none 12 bold")
        lbl_color.pack(padx=20)
        car_color = Entry(edit_car, width=20, bg="white")
        car_color.pack(padx=20)

        # Apply changes with button
        def editCarClick():
            # Make changes with Entries
            # Get request to make changes without changing customer_id
            response = requests.get(f'http://localhost:5000/cars/{car_id_text.get()}')
            x = response.json()
            comment = dict(id=car_id_text.get(), brand=car_new_brand.get(), model=car_new_model.get(),
                           year_model=car_new_year_model.get(), color=car_color.get(), customer_id=x["customer_id"])
            # Submit changes
            car_edit = requests.put(f'http://localhost:5000/cars/{car_id_text.get()}', json=comment)

        # Apply changes with button
        btn_apply = Button(edit_car, text="Apply\nChanges", command=editCarClick)
        btn_apply.pack(padx=20)

    def assign_car():
        # New window
        assign_window = Toplevel(root)

        # Car ID
        assign_car_label = Label(assign_window, text="Enter car ID")
        assign_car_label.pack(padx=20)
        assign_car_entry = Entry(assign_window, width=20, bg="white")
        assign_car_entry.pack(padx=20)

        # Customer ID
        assign_customer_label = Label(assign_window, text="Enter customer ID")
        assign_customer_label.pack(padx=20)

        assign_customer_entry = Entry(assign_window, width=20, bg="white")
        assign_customer_entry.pack(padx=20)

        def assignClick():
            # Get request to fill attributes of given ID
            response = requests.get(f'http://localhost:5000/cars/{assign_car_entry.get()}')
            x = response.json()

            # Only make changes with customer ID and car ID
            dct = dict(brand=x["brand"], color=x["color"], customer_id=int(assign_customer_entry.get()),
                       id=int(assign_car_entry.get()), model=x["model"],
                       year_model=x["year_model"])

            # submit changes
            y = requests.put(f'http://localhost:5000/cars/{assign_car_entry.get()}', json=dct)

        submit_btn = Button(assign_window, text="ASSIGN CAR\nTO CUSTOMER", command=assignClick)
        submit_btn.pack(padx=20)

    def unassign_car():
        # New window
        unassign_window = Toplevel(root)

        # Enter car ID
        unassign_car_label = Label(unassign_window, text="Enter car ID you wish to unassign")
        unassign_car_label.pack(padx=20)
        # Car ID Entry
        unassign_car_entry = Entry(unassign_window, width=20, bg="white")
        unassign_car_entry.pack(padx=20)

        def unassign_car_func():
            # Get request to fill attributes of given ID
            response = requests.get(f'http://localhost:5000/cars/{unassign_car_entry.get()}')
            x = response.json()

            # Change customer_id to None (unassigning)
            dct = dict(brand=x["brand"], color=x["color"], customer_id=None,
                       id=int(unassign_car_entry.get()), model=x["model"],
                       year_model=x["year_model"])
            # Submit changes
            y = requests.put(f'http://localhost:5000/cars/{unassign_car_entry.get()}', json=dct)
        # Submit button
        unassign_btn = Button(unassign_window, text="UNASSIGN\nCAR", command=unassign_car_func)
        unassign_btn.pack(padx=20)

    # Root of GUI
    root = Tk()
    root.geometry("480x480")
    root.title("Car rental service")
    # Customers label
    customer_label = Label(root, text="Customers", font="none 20 bold")
    customer_label.pack()
    # Add customer window
    open_window_cu1 = Button(root, text="Add a customer", command=add_customer_window)
    open_window_cu1.pack(padx=20)
    # Remove customer window
    open_window_cu2 = Button(root, text="Remove a customer", command=destroy_customer_window)
    open_window_cu2.pack(padx=20)
    # Edit customer window
    open_window_cu3 = Button(root, text="Edit a customer", command=edit_customer_window)
    open_window_cu3.pack(padx=20)

    # Cars label
    cars_label = Label(root, text="Cars", font="none 20 bold")
    cars_label.pack(padx=20, pady=5)
    # Add car window
    open_window_car1 = Button(root, text="Add a car", command=add_car_window)
    open_window_car1.pack(padx=20)
    # Remove car window
    open_window_car2 = Button(root, text="Remove a car", command=remove_car_window)
    open_window_car2.pack(padx=20)
    # Edit car window
    open_window_car3 = Button(root, text="Edit a car", command=edit_car_window)
    open_window_car3.pack(padx=20)

    # Assign a car to customer
    # Assign a car to customer label
    open_assign_window = Button(root, text="Assign a car to customer", font="none 20 bold", command=assign_car)
    open_assign_window.pack(padx=20)

    # Unassign a car to customer
    # Unassign a car to customer label
    open_unassign_window = Button(root, text="Unassign a car from customer", font="none 20 bold", command=unassign_car)
    open_unassign_window.pack(padx=20)

    root.mainloop()


if __name__ == '__main__':
    main()
