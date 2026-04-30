# 7. Tworzenie struktury folderów: Użyj modułu pathlib , aby napisać skrypt, który tworzy
# strukturę folderów: Projekt/src , Projekt/data , Projekt/docs .

from pathlib import Path

folder = Path("Project")

(folder / "src").mkdir(parents=True, exist_ok=True)
(folder / "data").mkdir(parents=True, exist_ok=True)
(folder / "docs").mkdir(parents=True, exist_ok=True)
