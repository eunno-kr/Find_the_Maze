사용자가 직접 움직이면서 미로찾기 할수 있음

구성 
지도 (map_data)
플레이어 위치
키보드 입력
화면 업데이트

```inport flet as ft

START = 'e'   # 시작 지점 설정
END = 'x'   # 도착 지점 설정
WALL = '1'   # 벽 설정 그 외 길

map_data = [
    ['e', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '0'],
    ['1', '0', '1', '0', '1', '0'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '1', '0', '1', '0', 'x'], 
    ['1', '1', '0', '0', '0', '1']
]   # 지도 맵핑


for i in range(maze_size):   #이중 반복문 중 바깥
  for j in range(maze_size):   #이중 반복문 중 안쪽
      if map_data[i][j] == START:  # 시작점 찾기
        start = (i, j)   # 좌표 저장
        slif map_data[i][j] == END:  #끝점 찾기
          end = (i, j)  # 좌표 저장

def main(page: ft.Page):   #   전체 화면으로 실행 
  page.title = "미로찾기"  # 제목 설정

  grid = [] # 미로 전체 리스트 
  for i in range(maze_size): # 세로 열
    row = [] # 한줄 리스트
    for i in range(maze_size): # 가로 열
      cell = ft.Container(  # 한칸 박스 생성
        width=40 # 박스의 가로의 크기
        height=40 # 박스의 세로의 크기
        bgcolor="yellow" if (i, j) == start else "white", # 시작점 노랑색 표시 나머지는 흰색으로 표시
        alignment=ft.Alignment(0, 0), # 텍스트를 중앙으로 정렬
        content = ft. Text(map-data[i][j]) # 박스안 문자 표시
      )
      row.append(cell) # 한줄에 칸 추가
    grid.append(row) # 전체 미로에 한줄 추가

  status_text = ft. Text("방향키로 이동하세요!", size=16) # 화면에  시작하면 보여주는 텍스트

  def update_display(): # 위치가 바뀔때마다 화면 생성 
    for i in range(maze_size):  # 이중 반복문 
      for j in range(maze_size): # 전체 맵 하나씩 검사
        val = map_dara[i][j] # 현재 위치 값 가져오기 # '1' = 벽 등등..
        if [i, j] == player_pos:   #현위치
          grid[i[[j].bgcolor = "yellow"  # 현위치는 노랑색 표시
        elif val == WALL:  # 벽
          grid[i[[j].bgcolor = "grey"   # 벽은 그레이 지정
        elif val == START:  # 출발지점
          grid[i[[j].bgcolor = "lightblue" # 출발지점 라이트 블루 지정
        elif val == END:  # 종점 
          grid[i[[j].bgcolor = "green"  # 끝나는 지점 초록색 지정
        elso:
          grid[i[[j].bgcolor = "white"  # 그외 나머지는 흰색으로 지정
      page.update()  #지속적 업데이트 (이동할때마다 색 변경)

  def on_keyboard(E: ft.KeyboardEvent):
    x, t = player_pos

  if e,ket == "Arrow Up":
    nx, ny = X - 1, y
  elif e.key == "Arrow Down":
    nx, ny = X + 1, y
  elif e.key == "Arrow Left":
    nx, ny = X , y - 1
  elif e.key == "Arrow Right":
    nx, ny = X , y + 1  
  else:
    rturn # 방향키가 아닌 키는 무시

  if 0 <= nx <maze_size and 0 <= ny < maze_size:  # 맵 밖으로 나가지 않게 해주고 이동 가능 여부 체크
    if map_data[nx][ny] != WALL:  #벽 확인후 벽일시 이동 불가
      player_pos[0], player_pos[1] = nx, ny # 직접실제 이동 가능 
      if (nx, ny) == end:  #도착시
        status_text.value = "🎉 도착! 미로를 탈출했습니다!"  #  출구에 도착 했을때 나오는 문구
      else:  # 현위치 표시
        status_text.value = f"위치: ({nx}, {ny})"
      update_display() # 위치 이동해서 위치는 바뀌는데 화면은 그대로
    else:
      status_text.value = "❌ 벽입니다!" #벽에 부딪혔을때 나오는 문구 # 이동 실패? 이동 불가시 
      page.update()

  page.on_keyboard_event = on_keyboard # 키보드 연결 

  layout = ft. Column(
    [status_text] + [ft. Row(row) for row in grid]
    )
  page.add(layout)   #ui 생성 
  update_display()  # 초기 화면 그대로 세

ft.run(main)   # 전체 시작

터미널 실행
python Find_the_Maze.py

시작화면
<img width="367" height="406" alt="출력 값" src="https://github.com/user-attachments/assets/8fc36c15-fc90-418d-86b2-d8074e3a0d2c" />





도착시
<img width="418" height="469" alt="도착" src="https://github.com/user-attachments/assets/323db94a-f7d8-4a3e-946e-5e2caea30c46" />





벽에 부딪혔을떄
<img width="399" height="452" alt="벽" src="https://github.com/user-attachments/assets/7d17c738-d99b-4a9f-bb9e-7e0ed219f65e" />






🎮미로찾기 게임 전체 흐름 정리
        프로그램 시작
            ↓
        main 실행
            ↓
        UI 생성
            ↓
        사용자 키 입력
            ↓
        on_keyboard 실행
            ↓
        이동 계산
            ↓
        이동 가능 체크
            ↓
        player_pos 변경
            ↓
        update_display()
            ↓
        화면 변경
