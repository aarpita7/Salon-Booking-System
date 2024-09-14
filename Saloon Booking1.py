import tkinter as tk
from tkinter import messagebox

# Queue data structure
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, customer_name):
        self.queue.append(customer_name)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def get_queue(self):
        return self.queue

# GUI Application
class SalonBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salon Booking System")
        
        # Styling
        self.root.config(bg="#d2b48c")  # Light brown background (Tan)
        self.root.geometry("350x350")

        # Initialize the queue
        self.queue = Queue()

        # Title label
        self.title_label = tk.Label(root, text="Salon Booking System", font=("Helvetica", 16, "bold"), bg="#d2b48c", fg="#3e2723")  # Dark brown text
        self.title_label.pack(pady=10)

        # Customer name input
        self.customer_name_label = tk.Label(root, text="Customer Name:", bg="#d2b48c", fg="#3e2723")  # Dark brown text
        self.customer_name_label.pack(pady=5)
        self.customer_name_entry = tk.Entry(root, width=30)
        self.customer_name_entry.pack(pady=5)

        # Book appointment button
        self.book_button = tk.Button(root, text="Book Appointment", command=self.book_appointment, bg="#8d6e63", fg="white", width=20)  # Medium brown button
        self.book_button.pack(pady=10)

        # Display queue button
        self.show_queue_button = tk.Button(root, text="Show Queue", command=self.show_queue, bg="#795548", fg="white", width=20)  # Medium brown
        self.show_queue_button.pack(pady=5)

        # Serve customer button
        self.serve_button = tk.Button(root, text="Serve Customer", command=self.serve_customer, bg="#5d4037", fg="white", width=20)  # Dark brown button
        self.serve_button.pack(pady=5)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#3e2723", fg="white", width=20)  # Dark brown button
        self.exit_button.pack(pady=5)

        # Queue display
        self.queue_label = tk.Label(root, text="Queue: []", bg="#d2b48c", fg="#8b4513")  # Saddle brown for the queue display
        self.queue_label.pack(pady=10)

    def book_appointment(self):
        customer_name = self.customer_name_entry.get()
        if customer_name:
            self.queue.enqueue(customer_name)
            self.customer_name_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Appointment booked for {customer_name}!")
        else:
            messagebox.showwarning("Input Error", "Please enter a customer name.")
        self.update_queue_display()

    def show_queue(self):
        queue = self.queue.get_queue()
        if queue:
            self.queue_label.config(text=f"Queue: {queue}")
        else:
            self.queue_label.config(text="Queue: []")
            messagebox.showinfo("Queue Status", "The queue is empty.")

    def serve_customer(self):
        served_customer = self.queue.dequeue()
        if served_customer:
            messagebox.showinfo("Serve Customer", f"Now serving: {served_customer}")
        else:
            messagebox.showinfo("Serve Customer", "No customers in the queue.")
        self.update_queue_display()

    def update_queue_display(self):
        queue = self.queue.get_queue()
        if queue:
            self.queue_label.config(text=f"Queue: {queue}")
        else:
            self.queue_label.config(text="Queue: []")

# Main Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = SalonBookingApp(root)
    root.mainloop()
