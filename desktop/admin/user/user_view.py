import customtkinter as ctk
from tkinter import messagebox
import requests


def users_view_show(app):
    app.clear_content()

    title = ctk.CTkLabel(
        app.content,
        text="Users Management",
        font=("Arial", 32, "bold")
    )
    title.pack(pady=20)

    form_frame = ctk.CTkFrame(app.content)
    form_frame.pack(fill="x", padx=20, pady=10)

    # name input
    name_entry = ctk.CTkEntry(form_frame, placeholder_text="Name", width=200)
    name_entry.pack(side="left", padx=10, pady=20)

    # email input
    email_entry = ctk.CTkEntry(form_frame, placeholder_text="Email", width=200)
    email_entry.pack(side="left", padx=10, pady=20)

    # password input
    password_entry = ctk.CTkEntry(
        form_frame, placeholder_text="Password", show="*", width=200)
    password_entry.pack(side="left", padx=10, pady=20)

    # result label
    result_label = ctk.CTkLabel(app.content, text="")
    result_label.pack()

    # --- ĐỊNH NGHĨA HÀM XỬ LÝ (Chỉ chứa logic thêm user) ---
    def handle_add_user():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        if name == "" or email == "" or password == "":
            result_label.configure(text="Please fill all fields")
            return

        user_data = {
            "name": name,
            "email": email,
            "password": password
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/users", json=user_data)
            data = response.json()
            result_label.configure(text=data.get("message", "Success"))

            # clear input
            name_entry.delete(0, "end")
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")

            # refresh users
            app.show_users()
        except Exception as e:
            result_label.configure(text=f"Connection Error: {e}")
    add_btn = ctk.CTkButton(
        form_frame,
        text="Add User",
        command=handle_add_user
    )
    add_btn.pack(side="left", padx=10)

    refresh_btn = ctk.CTkButton(
        app.content,
        text="Refresh",
        command=app.show_users
    )
    refresh_btn.pack(pady=10)

    table_frame = ctk.CTkFrame(app.content)
    table_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # GET USERS API
    try:
        response = requests.get("http://127.0.0.1:8000/users")
        users = response.json()
    except Exception as e:
        error_label = ctk.CTkLabel(
            table_frame, text=f"Failed to fetch users: {e}")
        error_label.pack(pady=20)
        return

    header_frame = ctk.CTkFrame(table_frame)
    header_frame.pack(fill="x", pady=5)

    headers = ["ID", "Name", "Email", "Action"]
    for header in headers:
        label = ctk.CTkLabel(
            header_frame,
            text=header,
            width=200,
            font=("Arial", 18, "bold")
        )
        label.pack(side="left", padx=10, pady=10)

    for user in users:
        row_frame = ctk.CTkFrame(table_frame)
        row_frame.pack(fill="x", pady=5)

        id_label = ctk.CTkLabel(row_frame, text=user["id"], width=200)
        id_label.pack(side="left", padx=10, pady=10)

        name_label = ctk.CTkLabel(row_frame, text=user["name"], width=200)
        name_label.pack(side="left", padx=10, pady=10)

        email_label = ctk.CTkLabel(row_frame, text=user["email"], width=200)
        email_label.pack(side="left", padx=10, pady=10)

        edit_btn = ctk.CTkButton(
            row_frame,
            text="Edit",
            width=80,
            command=lambda u=user: app.open_edit_window(u)
        )
        edit_btn.pack(side="left", padx=5)

        delete_btn = ctk.CTkButton(
            row_frame,
            text="Delete",
            width=80,
            fg_color="red",
            command=lambda uid=user["id"]: app.delete_user(uid)
        )
        delete_btn.pack(side="left", padx=5)
