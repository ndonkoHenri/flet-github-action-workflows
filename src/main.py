import flet as ft


def main(page: ft.Page):
    # the title of the app
    page.title = "Flet Counter App"

    # a light/bright theme
    page.theme_mode = "light"

    # the page's alignment
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def increment_counter(e):
        """Increment the value of the counter_text object by 1, and update the UI to reflect these changes."""
        counter_text.value = str(int(counter_text.value) + 1)
        page.update()

    # the app's appbar
    page.appbar = ft.AppBar(
        title=ft.Text(
            "Flet Demo Home Page", color=ft.colors.WHITE
        ),  # a title of white color
        bgcolor=ft.colors.BLUE,  # a blue background color
        center_title=True,  # center the title || without this, the title will be on the left
    )

    # text that contains the counter number to be incremented
    counter_text = ft.Text("0", size=64)

    # the app's FAB
    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.icons.ADD, color=ft.colors.WHITE),
        shape=ft.CircleBorder(),  # gives the button a round/circle shape
        on_click=increment_counter,  # the callback to be executed when this button is clicked
        tooltip="Increment",  # the text to be shown when this button is hovered
        bgcolor=ft.colors.BLUE,  # a blue background color
    )

    # adding our widgets/controls to the page/UI
    page.add(ft.Text("You have pushed the button this many times:"), counter_text)


ft.app(target=main)
