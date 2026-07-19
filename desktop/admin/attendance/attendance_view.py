import customtkinter as ctk
from tkinter import messagebox
import requests


def attendance_view_show(app):
    app.clear_content()
    title = ctk.CTkLabel(
        app.content,
        text="Attendance History",
        font=("Arial", 32, "bold")
    )
    title.pack(
        pady=20
    )
    refresh_btn = ctk.CTkButton(
        app.content,
        text="Refresh",
        command=app.attendance_view
    )
    refresh_btn.pack(
        pady=10
    )
    table_frame = ctk.CTkFrame(
        app.content
    )
    table_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )
    try:
        response = requests.get("http://127.0.0.1:8000/attendance", timeout=10)
        records = response.json()
    except Exception as e:
        messagebox.showerror(
            "Error", f"Failed to fetch attendance records: {e}")
        records = []  # Tránh crash vòng lặp phía dưới nếu API lỗi

    header_frame = ctk.CTkFrame(table_frame)
    header_frame.pack(fill="x", pady=5)

    headers = ["ID", "User ID", "Check In", "Check Out", "Action"]
    widths = [80, 80, 220, 220, 400]

    for index, header in enumerate(headers):
        label = ctk.CTkLabel(
            header_frame,
            text=header,
            width=widths[index],
            font=("Arial", 18, "bold")
        )
        label.pack(side="left", padx=5, pady=10)

    for record in records:
        row_frame = ctk.CTkFrame(table_frame)
        row_frame.pack(fill="x", pady=3)

        ctk.CTkLabel(row_frame, text=record.get("id", ""),
                     width=80).pack(side="left", padx=5, pady=8)
        ctk.CTkLabel(row_frame, text=record.get("user_id", ""),
                     width=120).pack(side="left", padx=5, pady=8)
        ctk.CTkLabel(row_frame, text=str(record.get("check_in", "")),
                     width=280).pack(side="left", padx=5, pady=8)
        ctk.CTkLabel(row_frame, text=str(record.get("check_out", "")),
                     width=280).pack(side="left", padx=5, pady=8)
        action_frame = ctk.CTkFrame(
            row_frame, fg_color="transparent", width=180)
        action_frame.pack(side="left", padx=5)

        # Nút Sửa (Edit) - Sử dụng đúng biến r=record thay vì user
        edit_btn = ctk.CTkButton(
            action_frame,
            text="Edit",
            width=70,
            command=lambda r=record: app.open_edit_window(r)
        )
        edit_btn.pack(side="left", padx=5)

        # Nút Xóa (Delete) - Sử dụng đúng biến rid=record["id"]
        delete_btn = ctk.CTkButton(
            action_frame,
            text="Delete",
            width=70,
            fg_color="red",
            hover_color="darkred",
            command=lambda rid=record.get("id"): app.delete_user(rid)
        )
        delete_btn.pack(side="left", padx=5)
