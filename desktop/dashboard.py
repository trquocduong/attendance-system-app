import customtkinter as ctk

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
        title.pack(
            pady=30
        )

        # Fake users
        users = [
            "Duong",
            "Admin",
            "Nhan Vien 01",
            "Nhan Vien 02"
        ]

        for user in users:
            user_item = ctk.CTkFrame(
                self.content,
                height=60
            )
            user_item.pack(
                fill="x",
                padx=40,
                pady=10
            )

            user_label = ctk.CTkLabel(
                user_item,
                text=user,
                font=("Arial", 20)
            )
            user_label.pack(
                side="left",
                padx=20,
                pady=15
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
