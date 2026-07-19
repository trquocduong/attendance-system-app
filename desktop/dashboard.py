import customtkinter as ctk
from tkinter import messagebox
import requests
from admin.attendance.attendance_view import attendance_view_show
from admin.user.user_view import users_view_show

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Attendance System Dashboard")
        self.geometry("1200x700")

        # Build UI
        self.build_ui()

    def build_ui(self):
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )
        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Sidebar title
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="Attendance App",
            font=("Arial", 28, "bold")
        )
        self.logo_label.pack(
            pady=30
        )

        # Dashboard button
        self.dashboard_btn = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            height=45,
            command=self.show_dashboard
        )
        self.dashboard_btn.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        # User button (Đã sửa từ self.users_view_show thành self.show_users)
        self.user_btn = ctk.CTkButton(
            self.sidebar,
            text="User",
            height=45,
            command=self.show_users
        )
        self.user_btn.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        # Attendance button
        self.attendance_btn = ctk.CTkButton(
            self.sidebar,
            text="Attendance",
            height=45,
            command=self.show_attendance
        )
        self.attendance_btn.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        # History button (Đã chuyển từ hàm check_out lên đây và liên kết với attendance_view)
        self.history_btn = ctk.CTkButton(
            self.sidebar,
            text="History",
            height=45,
            command=self.attendance_view
        )
        self.history_btn.pack(
            pady=10,
            padx=20,
            fill="x"
        )

        # Logout button
        self.logout_btn = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            height=45,
            fg_color="red",
            hover_color="darkred",
            command=self.logout
        )
        self.logout_btn.pack(
            side="bottom",
            pady=20,
            padx=20,
            fill="x"
        )

        # CONTENT AREA
        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )
        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Default page
        self.show_dashboard()

    # CLEAR CONTENT
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # DASHBOARD PAGE
    def show_dashboard(self):
        self.clear_content()

        # Title
        title = ctk.CTkLabel(
            self.content,
            text="Dashboard",
            font=("Arial", 32, "bold")
        )
        title.pack(
            pady=30
        )

        # Cards container
        cards_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )
        cards_frame.pack(
            pady=20
        )

        # TOTAL USERS CARD
        user_card = ctk.CTkFrame(
            cards_frame,
            width=250,
            height=150
        )
        user_card.grid(
            row=0,
            column=0,
            padx=20
        )

        user_title = ctk.CTkLabel(
            user_card,
            text="Total Employees",
            font=("Arial", 20)
        )
        user_title.pack(
            pady=(25, 10)
        )

        user_count = ctk.CTkLabel(
            user_card,
            text="15",
            font=("Arial", 40, "bold")
        )
        user_count.pack()

        # ATTENDANCE CARD
        attendance_card = ctk.CTkFrame(
            cards_frame,
            width=250,
            height=150
        )
        attendance_card.grid(
            row=0,
            column=1,
            padx=20
        )

        attendance_title = ctk.CTkLabel(
            attendance_card,
            text="Today Attendance",
            font=("Arial", 20)
        )
        attendance_title.pack(
            pady=(25, 10)
        )

        attendance_count = ctk.CTkLabel(
            attendance_card,
            text="12",
            font=("Arial", 40, "bold")
        )
        attendance_count.pack()

        # STATUS
        status_label = ctk.CTkLabel(
            self.content,
            text="System Running Successfully",
            font=("Arial", 18)
        )
        status_label.pack(
            pady=40
        )
        footer = ctk.CTkLabel(
            self.content,
            text="Attendance System v1.0",
            text_color="gray"
        )

        footer.pack(
            side="bottom",
            pady=15
        )

    # Đã đổi tên từ users_view sang show_users để khớp với update_user/delete_user và bên view ngoài gọi vào
    def show_users(self):
        self.clear_content()
        users_view_show(self)

    # EDIT USER WINDOW
    def open_edit_window(self, user):
        window = ctk.CTkToplevel(self)
        window.title("Edit User")
        window.geometry("400x300")
        window.lift()  # Đưa cửa sổ lên phía trước
        window.focus_force()

        name_entry = ctk.CTkEntry(
            window,
            width=250
        )
        name_entry.insert(0, user["name"])
        name_entry.pack(pady=10)

        email_entry = ctk.CTkEntry(
            window,
            width=250
        )
        email_entry.insert(0, user["email"])
        email_entry.pack(pady=10)

        save_btn = ctk.CTkButton(
            window,
            text="Save",
            command=lambda: self.update_user(
                user["id"],
                name_entry.get(),
                email_entry.get(),
                window
            )
        )
        save_btn.pack(
            pady=20
        )

    def update_user(self, user_id, name, email, window):
        data = {
            "name": name,
            "email": email,
            "password": "123456"
        }
        try:
            response = requests.put(
                f"http://127.0.0.1:8000/users/{user_id}",
                json=data,
                timeout=10
            )
            print(response.json())
            window.destroy()
            self.show_users()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update user: {e}")

    # ATTENDANCE PAGE
    def show_attendance(self):
        self.clear_content()

        title = ctk.CTkLabel(
            self.content,
            text="Attendance Page",
            font=("Arial", 32, "bold")
        )
        title.pack(
            pady=30
        )

        checkin_btn = ctk.CTkButton(
            self.content,
            text="Check In",
            height=50,
            command=self.check_in
        )
        checkin_btn.pack(
            pady=20
        )
        checkout_btn = ctk.CTkButton(
            self.content,
            text="Check Out",
            height=50,
            fg_color="red",
            command=self.check_out
        )
        checkout_btn.pack(
            pady=20
        )

    def delete_user(self, user_id):
        confirm = messagebox.askyesno(
            "Confirm",
            "Are you sure want to delete this user?"
        )
        if not confirm:
            return

        try:
            response = requests.delete(
                f"http://127.0.0.1:8000/users/{user_id}"
            )
            print(response.json())
            self.show_users()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete user: {e}")

    # LOGOUT
    def logout(self):
        self.destroy()

    # Check in/out
    def check_in(self):
        user_id = 1
        try:
            response = requests.post(
                "http://127.0.0.1:8000/check-in",
                json={"user_id": user_id}
            )
            data = response.json()
            print("Dữ liệu thực tế từ server:", data)
            messagebox.showinfo("Success", data.get(
                "message", "Checked in successfully!"))
        except Exception as e:
            messagebox.showerror("Error", f"Connection failed: {e}")

    def check_out(self):
        user_id = 1
        try:
            response = requests.post(
                "http://127.0.0.1:8000/checkout",
                json={"user_id": user_id}
            )
            data = response.json()
            print("Dữ liệu thực tế từ server:", data)
            messagebox.showinfo("Success", data.get(
                "message", "Checked out successfully!"))
        except Exception as e:
            messagebox.showerror("Error", f"Connection failed: {e}")

    def attendance_view(self):
        self.clear_content()
        attendance_view_show(self)


app = DashboardApp()
app.mainloop()
