import requests
import flet as ft
import datetime
from flet_core import TextAlign

def main(page: ft.Page):
    page.title = "Magister.py"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    token = ft.TextField(label="Authentication Token", icon="key")

    fromDate = ft.ElevatedButton(
        "Pick date - From",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2023, month=10, day=1),
                last_date=datetime.datetime(year=2024, month=10, day=1),
                on_change=handle_change,
            )
        )
    )
    toDate = ft.ElevatedButton(
        "Pick date - To",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda e: page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2023, month=10, day=1),
                last_date=datetime.datetime(year=2024, month=10, day=1),
                on_change = handle_change2,
            )
        )
    )

    fromDateValue = ""
    toDateValue = ""

    def handle_change(e):
        fromDateValue = e.control.value.strftime('%Y-%m-%d')

    def handle_change2(e):
        toDateValue = e.control.value.strftime('%Y-%m-%d')

    def login(e):
        if token.value == "":
            token.value
        else:
            headers = {"Authorization": f"Bearer " + token.value}
            response = requests.get("https://citadel.magister.net/api/account?noCache=0", headers=headers)
            personjson = response.json()["Persoon"]
            accessid = personjson["Id"]
            agenda = requests.get("https://citadel.magister.net/api/personen/" + str(
                accessid) + "/afspraken?status=1&tot=" + toDateValue + "&van=" + fromDateValue, headers=headers)
            items = agenda.json()["Items"]

            try:
                h1ci = items[0]
                h1c = ft.Text(value=str(h1ci["LesuurVan"]) + " - " + h1ci["Omschrijving"])
            except IndexError:
                h1c = 'null'

            try:
                h2ci = items[1]
                h2c = ft.Text(value=str(h2ci["LesuurVan"]) + " - " + h2ci["Omschrijving"])
            except IndexError:
                h2c = ft.Text(value="Does not exist")

            try:
                h3ci = items[2]
                h3c = ft.Text(value=str(h3ci["LesuurVan"]) + " - " + h3ci["Omschrijving"])
            except IndexError:
                h3c = ft.Text(value="Does not exist")

            try:
                h4ci = items[3]
                h4c = ft.Text(value=str(h4ci["LesuurVan"]) + " - " + h4ci["Omschrijving"])
            except IndexError:
                h4c = ft.Text(value="Does not exist")
            try:
                h5ci = items[4]
                h5c = ft.Text(value=str(h5ci["LesuurVan"]) + " - " + h5ci["Omschrijving"])

            except IndexError:
                h5c = ft.Text(value="Does not exist")
                
            try:
                h6ci = items[5]
                h6c = ft.Text(value=str(h6ci["LesuurVan"]) + " - " + h6ci["Omschrijving"])

            except IndexError:
                h6c = ft.Text(value="Does not exist")
            
            try:
                h7ci = items[6]
                h7c = ft.Text(value=str(h7ci["LesuurVan"]) + " - " + h7ci["Omschrijving"])

            except IndexError:
                h7c = ft.Text(value="Does not exist")
                
            try:
                h8ci = items[7]
                h8c = ft.Text(value=str(h8ci["LesuurVan"]) + " - " + h8ci["Omschrijving"])

            except IndexError:
                h8c = ft.Text(value="Does not exist")
                
            try:
                h9ci = items[8]
                h9c = ft.Text(value=str(h9ci["LesuurVan"]) + " - " + h9ci["Omschrijving"])

            except IndexError:
                h9c = ft.Text(value="Does not exist")
                
            try:
                h10ci = items[9]
                h10c = ft.Text(value=str(h10ci["LesuurVan"]) + " - " + h10ci["Omschrijving"])

            except IndexError:
                h10c = ft.Text(value="Does not exist")

            h1 = ft.Container(
                content=h1c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h2 = ft.Container(
                content=h2c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h3 = ft.Container(
                content=h3c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h4 = ft.Container(
                content=h4c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h5 = ft.Container(
                content=h5c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h6 = ft.Container(
                content=h6c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h7 = ft.Container(
                content=h7c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h8 = ft.Container(
                content=h8c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h9 = ft.Container(
                content=h9c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            h10 = ft.Container(
                content=h10c,
                alignment=ft.alignment.center,
                width=200,
                height=50,
                bgcolor=ft.colors.BLUE,
                border_radius=ft.border_radius.all(5),
            )
            page.add(
                ft.Row(
                    [
                        h1,
                        h2,
                        h3,
                        h4,
                        h5

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
            page.add(
                ft.Row(
                    [
                        h6,
                        h7,
                        h8,
                        h9,
                        h10

                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

    c1 = ft.Container(
        content=token,
        padding=5,
    )

    c2 = ft.Container(
        content=ft.FilledButton(
            "Log-In and Fetch", icon="login", on_click=login
        ),
        padding=5,
    )


    column = ft.Column(spacing=5, controls=(c1, c2))

    page.add(
        ft.Row(
            [
                column,
                fromDate,
                toDate



            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )


def agenda(page: ft.Page):
    ft.TextField(label="Authentication Token", icon="key")


ft.app(main)
