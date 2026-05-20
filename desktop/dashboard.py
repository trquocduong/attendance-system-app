import customtkinter as ctk
import requests

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

        # User button
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

    # CLEAR CONTENT (Đã đưa ra ngoài hàm build_ui)
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # DASHBOARD PAGE (Đã sửa lại thụt lề chuẩn)
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

    # USERS PAGE (Đã đưa ra ngoài hàm build_ui)
    def show_users(self):

        self.clear_content()
        title = ctk.CTkLabel(
            self.content,
            text="Users Management",
            font=("Arial", 32, "bold")
        )

        title.pack(pady=20)
        form_frame = ctk.CTkFrame(
            self.content
        )

        form_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # name input
        name_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Name",
            width=200
        )

        name_entry.pack(
            side="left",
            padx=10,
            pady=20
        )

        # email input
        email_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Email",
            width=200
        )

        email_entry.pack(
            side="left",
            padx=10,
            pady=20
        )

        # password input
        password_entry = ctk.CTkEntry(
            form_frame,
            placeholder_text="Password",
            show="*",
            width=200
        )

        password_entry.pack(
            side="left",
            padx=10,
            pady=20
        )

        # result label
        result_label = ctk.CTkLabel(
            self.content,
            text=""
        )

        result_label.pack()

        def handle_add_user():

            name = name_entry.get()

            email = email_entry.get()

            password = password_entry.get()
            if (
                name == ""
                or email == ""
                or password == ""
            ):

                result_label.configure(
                    text="Please fill all fields"
                )

                return

            user_data = {
                "name": name,
                "email": email,
                "password": password
            }

            response = requests.post(
                "http://127.0.0.1:8000/users",
                json=user_data
            )

            data = response.json()
            result_label.configure(
                text=data["message"]
            )

            # clear input
            name_entry.delete(0, "end")

            email_entry.delete(0, "end")

            password_entry.delete(0, "end")

            # refresh users
            self.show_users()
        add_btn = ctk.CTkButton(
            form_frame,
            text="Add User",
            command=handle_add_user
        )

        add_btn.pack(
            side="left",
            padx=10
        )
        refresh_btn = ctk.CTkButton(
            self.content,
            text="Refresh",
            command=self.show_users
        )

        refresh_btn.pack(
            pady=10
        )
        table_frame = ctk.CTkFrame(
            self.content
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )
        # GET USERS API

        response = requests.get(
            "http://127.0.0.1:8000/users"
        )

        users = response.json()
        header_frame = ctk.CTkFrame(
            table_frame
        )

        header_frame.pack(
            fill="x",
            pady=5
        )

        headers = [
            "ID",
            "Name",
            "Email"
        ]

        for header in headers:

            label = ctk.CTkLabel(
                header_frame,
                text=header,
                width=200,
                font=("Arial", 18, "bold")
            )

            label.pack(
                side="left",
                padx=10,
                pady=10
            )
        for user in users:

            row_frame = ctk.CTkFrame(
                table_frame
            )

            row_frame.pack(
                fill="x",
                pady=5
            )

            id_label = ctk.CTkLabel(
                row_frame,
                text=user["id"],
                width=200
            )

            id_label.pack(
                side="left",
                padx=10,
                pady=10
            )

            name_label = ctk.CTkLabel(
                row_frame,
                text=user["name"],
                width=200
            )

            name_label.pack(
                side="left",
                padx=10,
                pady=10
            )

            email_label = ctk.CTkLabel(
                row_frame,
                text=user["email"],
                width=200
            )

            email_label.pack(
                side="left",
                padx=10,
                pady=10
            )
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

        attendance_text = ctk.CTkLabel(
            self.content,
            text="Camera Attendance Coming Soon...",
            font=("Arial", 22)
        )
        attendance_text.pack(
            pady=50
        )

    # LOGOUT
    def logout(self):
        self.destroy()


app = DashboardApp()
app.mainloop()
