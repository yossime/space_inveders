# 🚀 Space Invaders Game

משחק Space Invaders קלאסי שנכתב ב-Python עם pygame.

## 📁 מבנה הפרויקט

```
space_invaders/
├── main.py              # נקודת כניסה ראשית למשחק
├── requirements.txt     # תלויות הפרויקט
├── README.md           # תיעוד הפרויקט
├── game/               # קבצי המשחק
│   ├── __init__.py
│   ├── run_game.py     # לולאת המשחק הראשית
│   ├── baise.py        # לוגיקת המשחק הבסיסית
│   ├── spaceship.py    # מחלקת החללית
│   ├── inveders.py     # מחלקת הפולשים
│   ├── shooting_spaceship.py  # קליעי החללית
│   ├── shooting_inveders.py   # קליעי הפולשים
│   ├── sound.py        # ניהול צלילים
│   ├── display.py      # הגדרות תצוגה
│   └── test.py         # בדיקות
└── assets/             # קבצי מדיה (תמונות, צלילים)
```

## 🎮 איך להריץ את המשחק

### דרישות מוקדמות

- Python 3.7 או גרסה חדשה יותר
- pygame

### התקנה

1. שכפל את הפרויקט:

   ```bash
   git clone <repository-url>
   cd space_invaders
   ```

2. התקן את התלויות:

   ```bash
   pip install -r requirements.txt
   ```

3. הרץ את המשחק:
   ```bash
   python main.py
   ```

## 🎯 איך לשחק

- **חצים שמאלה/ימינה**: הזז את החללית
- **רווח**: ירה
- **ESC**: יציאה מהמשחק

## ⚙️ הגדרות המשחק

המשחק כולל:

- חללית ירוקה (משולש)
- פולשים אדומים
- קליעים תכלת לחללית
- קליעים כתומים לפולשים
- רקע כחול כהה

## 🔧 התאמה אישית

### הוספת תמונות וצלילים

1. הוסף קבצי מדיה לתיקיית `assets/`
2. עדכן את הנתיבים בקבצים:
   - `display.py` - תמונת רקע
   - `spaceship.py` - תמונת חללית
   - `inveders.py` - תמונת פולשים
   - `sound.py` - קבצי שמע

### מבנה קבצי Assets מומלץ:

```
assets/
├── images/
│   ├── background.jpg
│   ├── spaceship.png
│   ├── invader.png
│   ├── spaceship_bullet.png
│   └── invader_bullet.png
└── sounds/
    ├── shoot.mp3
    ├── explosion.wav
    ├── game_over.mp3
    ├── victory.mp3
    └── background_music.mp3
```

## 🐛 פתרון בעיות

### המשחק לא נפתח

- ודא ש-pygame מותקן: `pip install pygame`
- בדוק שPython מותקן ונמצא ב-PATH

### שגיאות בקבצי מדיה

- המשחק יעבוד גם ללא קבצי מדיה (עם גרפיקה בסיסית)
- הוסף קבצי מדיה לתיקיית `assets/` לחוויה מלאה

## 📝 רישיון

פרויקט זה נוצר למטרות לימוד.
