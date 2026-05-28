import flet as ft

START = 'e'
END = 'x'
WALL = '1'

map_data = [
    ['e', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '0'],
    ['1', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '1', '0', '1', '0', 'x'], 
    ['1', '1', '0', '0', '0', '1']
]

maze_size = len(map_data)

for i in range(maze_size):
    for j in range(maze_size):
        if map_data[i][j] == START:
            start = (i, j)
        elif map_data[i][j] == END:
            end = (i, j)


def main(page: ft.Page):
    page.title = "미로 찾기"

    player_pos = list(start)  # 현재 플레이어 위치

    grid = []
    for i in range(maze_size):
        row = []
        for j in range(maze_size):
            cell = ft.Container(
                width=40,
                height=40,
                bgcolor="yellow" if (i, j) == start else "white",
                border=ft.Border.all(1, ft.Colors.BLACK),
                alignment=ft.Alignment(0, 0),
                content=ft.Text(map_data[i][j])
            )
            row.append(cell)
        grid.append(row)

    status_text = ft.Text("방향키로 이동하세요!", size=16)

    def update_display():
        for i in range(maze_size):
            for j in range(maze_size):
                val = map_data[i][j]
                if [i, j] == player_pos:
                    grid[i][j].bgcolor = "yellow"
                elif val == WALL:
                    grid[i][j].bgcolor = "grey"
                elif val == START:
                    grid[i][j].bgcolor = "lightblue"
                elif val == END:
                    grid[i][j].bgcolor = "green"
                else:
                    grid[i][j].bgcolor = "white"
        page.update()

    def on_keyboard(e: ft.KeyboardEvent):
        x, y = player_pos

        if e.key == "Arrow Up":
            nx, ny = x - 1, y
        elif e.key == "Arrow Down":
            nx, ny = x + 1, y
        elif e.key == "Arrow Left":
            nx, ny = x, y - 1
        elif e.key == "Arrow Right":
            nx, ny = x, y + 1
        else:
            return

        # 범위 및 벽 체크
        if 0 <= nx < maze_size and 0 <= ny < maze_size:
            if map_data[nx][ny] != WALL:
                player_pos[0], player_pos[1] = nx, ny

                if (nx, ny) == end:
                    status_text.value = "🎉 도착! 미로를 탈출했습니다!"
                else:
                    status_text.value = f"위치: ({nx}, {ny})"

                update_display()
            else:
                status_text.value = "❌ 벽입니다!"
                page.update()

    page.on_keyboard_event = on_keyboard

    layout = ft.Column(
        [status_text] + [ft.Row(row) for row in grid]
    )

    page.add(layout)
    update_display()

ft.run(main)