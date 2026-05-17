import customtkinter as ctk
import requests

# setup theme
ctk.set_appearance_mode("dark")


# tạo app window
app = ctk.CTk()

# title
app.title("Attendance System")

# width x height
app.geometry("500x400")

# title label form login
title_label = ctk.CTkLabel(
    app,
    text="Login",
    font=("Arial", 28)
)
title_label.pack(pady=10)
# username input
email_entry = ctk.CTkEntry(
    app,
    placeholder_text="Email",
    width=300
)

email_entry.pack(pady=10)
# password input
password_entry = ctk.CTkEntry(
    app,
    placeholder_text="Password",
    show="*",
    width=300
)

password_entry.pack(pady=10)

# RESULT LABEL
result_label = ctk.CTkLabel(
    app,
    text=""
)

result_label.pack(pady=10)


def handle_login():

    # username = username_entry.get()

    # password = password_entry.get()

    # print(username)
    # print(password)
    # lấy dữ liệu từ input hiển thị vào consolog
    email = email_entry.get()
    password = password_entry.get()
    login_data = {
        "email": email,
        "password": password
    }

    response = requests.post(
        "http://localhost:8000/login",
        json=login_data
    )

    data = response.json()

    result_label.configure(
        text=data["message"]
    )


login_button = ctk.CTkButton(
    app,
    text="Login",
    command=handle_login
)

login_button.pack(pady=20)
# chạy app
app.mainloop()
