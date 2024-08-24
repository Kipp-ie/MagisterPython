import requests
import flet as ft
from flet_core import TextAlign

bearer_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJCMkZCREM4QkFDNjgzRkNDQTE3MjI3RURGRUU2ODZCIiwidHlwIjoiYXQrand0In0.eyJpc3MiOiJodHRwczovL2FjY291bnRzLm1hZ2lzdGVyLm5ldCIsIm5iZiI6MTcyNDUyNzEwMSwiaWF0IjoxNzI0NTI3MTAxLCJleHAiOjE3MjQ1MzA3MDEsImF1ZCI6WyJvcHAiLCJhdHRlbmRhbmNlIiwiY2FsZW5kYXIud2ViIiwiY2FsZW5kYXIuaWNhbCIsImNhbGVuZGFyLnRvLWRvIiwiZ3JhZGVzIiwib3NvLndlYiIsInJlZ2lzdHJhdGlvbiIsInJlZ2lzdHJhdGlvbi53ZWIiLCJodHRwczovL2FjY291bnRzLm1hZ2lzdGVyLm5ldC9yZXNvdXJjZXMiXSwic2NvcGUiOlsib3BlbmlkIiwicHJvZmlsZSIsIm9wcC5yZWFkIiwib3BwLm1hbmFnZSIsImF0dGVuZGFuY2Uub3ZlcnZpZXciLCJhdHRlbmRhbmNlLmFkbWluaXN0cmF0aW9uIiwiY2FsZW5kYXIudXNlciIsImNhbGVuZGFyLmljYWwudXNlciIsImNhbGVuZGFyLnRvLWRvLnVzZXIiLCJncmFkZXMucmVhZCIsImdyYWRlcy5tYW5hZ2UiLCJvc28uYWRtaW5pc3RyYXRpb24iLCJyZWdpc3RyYXRpb24uYWRtaW4iXSwiYW1yIjpbInB3ZCJdLCJjbGllbnRfaWQiOiJNNi1jaXRhZGVsLm1hZ2lzdGVyLm5ldCIsInN1YiI6ImZkZGYwMGNhOTcyNDQxOWVhOTFmMjEyYmVlZDZhZDBiIiwiYXV0aF90aW1lIjoxNzI0NTIzNTU0LCJpZHAiOiJDaXRhZGVsIENvbGxlZ2UiLCJ0aWQiOiI1Yzk5YjRlNzU4NzE0MThmOTdiZjIzZGU3MmVlMmQ1ZiIsInNpZCI6IjJDMDJFOUNEQkE0MTJBODNENTVGMTRDNkI2MURCMUUzIiwianRpIjoiMTQ1NDMwOEI0NDc2NjE0RTg4RkVGNDUxNzRFQTVBOUUifQ.vdQkfISwGBm3y-22zwUKDgKHodaowXTGZVht6qkGYSV1Q7W-o4bdOTkuf3G65SEoSFpv6aXZ0_5NsFcq0fVfmOFuJkUHlkTuwzZwACSahLxjk4ohReuusAGpv-Xx7P6ha9ffXutSd2lltAR2OSqNG1JLLOErtWiRtPtKaxiyV192l33b7PsuUhazytfb8eBbnz2WhUtpwC9DTc_223Ap2KBkQ5Wqoy2j3aNRdKY4NrGOFWhhQSlyf6CGhRbtmQ9R7Q50yCEtsWjP4UEwBaBKLSz83JNiODv-1Xnhd-ZzEy15YIXqK33tE1QGw5DMx_kzLoqnxN8cQG3c9lIXcjxyLA"
agenda_data_from = "2024-08-26"
agenda_data_to = "2024-08-26"

headers = {"Authorization": f"Bearer {bearer_token}"}


response = requests.get("https://citadel.magister.net/api/account?noCache=0", headers=headers)

personjson = response.json()["Persoon"]

print("Welcome to Python Magister - Log-In successful.")



print("Welcome: " + personjson["Roepnaam"])




def main(page: ft.Page):
    page.title = "Magister.py"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    token = ft.TextField(label="Authentication Token", icon="key")
    def login(e):
        if token.value == "":
            token.value
        else:
            headers = {"Authorization": f"Bearer " + token.value}
            response = requests.get("https://citadel.magister.net/api/account?noCache=0", headers=headers)
            personjson = response.json()["Persoon"]
            accessid = personjson["Id"]
            agenda = requests.get("https://citadel.magister.net/api/personen/" + str(
                accessid) + "/afspraken?status=1&tot=" + agenda_data_to + "&van=" + agenda_data_from, headers=headers)
            items = agenda.json()["Items"]

            try:
                h1ci = items[1]
                h

            except IndexError:
                h1c = 'null'

            h1 = ft.Container(
                content=ft.Text(value=str(1)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
            h2 = ft.Container(
                content=ft.Text(value=str(1)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
            h3 = ft.Container(
                content=ft.Text(value=str(1)),
                alignment=ft.alignment.center,
                width=50,
                height=50,
                bgcolor=ft.colors.AMBER,
                border_radius=ft.border_radius.all(5),
            )
            page.add(
                ft.Row(
                    [
                        h1,
                        h2,
                        h3

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
                column

            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
def agenda(page: ft.Page):
    ft.TextField(label="Authentication Token", icon="key")





ft.app(main)