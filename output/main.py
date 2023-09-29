import raylib

raylib.InitWindow(800, 450, "raylib [core] example - basic window")

RAYWHITE = raylib.Color(245, 245, 245, 255)
LIGHTGRAY = raylib.Color(200, 200, 200, 255)

while not raylib.WindowShouldClose():
    raylib.BeginDrawing()
    raylib.ClearBackground(RAYWHITE)
    raylib.DrawText("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
    raylib.EndDrawing()

raylib.CloseWindow()