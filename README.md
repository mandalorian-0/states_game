# 🌍 State Guessing Game

A fun, interactive Python application where users guess U.S. state names. When a guess is correct, the state is **placed precisely at its pre-defined relative location on a U.S. map** using the `turtle` graphics module. The map serves as a dynamic canvas, with each correct guess appearing in its correct spot — just like on a real map!

🎯 **Perfect for:** Teaching geography, learning programming logic, or building interactive educational tools.

---

## 🚀 Features

- 🖼️ A **realistic U.S. map background** is drawn using `turtle`, providing a visual context.
- ✅ On correct guesses, the state is **placed at its exact relative coordinate** (x, y) on the map — not just drawn randomly.
- 📂 State locations are stored in a **CSV file** with columns: `state`, `x`, `y` (relative to map center).
- 📊 Uses **`pandas`** to efficiently load, filter, and process the state data.
- 📝 Users are prompted to guess a state name; correct guesses are added to a list for tracking.
- 🚨 Incorrect guesses trigger a clear, friendly alert message.
- 📏 All coordinates are **relative to the map** — not real-world geographic coordinates (e.g., latitude/longitude).

---

## 🔧 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mandalorian-0/states_game.git

   cd states_game
   ```

2. **Ensure Python is installed**  
   Download Python from [python.org](https://www.python.org/downloads/).

3. **Install required dependencies** (optional, but recommended):
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the script**:
   ```bash
   python main.py
   ```

> The app will start a loop where users enter state names. After each guess, it will either draw the state on the map or show an error.

---

## 📦 Dependencies

- ✅ **Python 3.6+** (required)
- 📚 **`pandas`** – to read and manage the CSV file containing state coordinates
- 🖼️ **`turtle`** – for drawing the map background and placing states at correct relative positions

> No external libraries beyond standard Python and `pandas` are needed.

---

## 🎮 Example Interaction

```
Guess a U.S. state: Texas
✅ Correct! Texas is now displayed at its relative location on the map.

Guess a U.S. state: Florida
✅ Correct! Florida is now displayed at its relative location on the map.

Guess a U.S. state: Antarctica
❌ Incorrect! Antarctica is not a U.S. state.

Correct guesses so far: ['Texas', 'Florida']
```

---

## 📝 How It Works (Concept)

1. A CSV file (`states.csv`) contains the list of U.S. states and their **relative x, y coordinates** on the map.
2. The `pandas` module loads this data and stores it in a DataFrame.
3. The `turtle` module draws a U.S. map background using lines and shapes.
4. When a user guesses a state:
   - The program checks if the guess exists in the list.
   - If correct → it finds the corresponding (x, y) pair and draws the state name at that point.
   - If incorrect → a message is shown.
5. All correct guesses are appended to a list for review.

> The coordinates are **not real-world GPS values** — they are **relative** and designed to match the visual layout of the map (e.g., centered, scaled, and normalized).

---

## 🚀 Future Improvements

- 🌐 Expand to include other countries with custom map backgrounds.
- 📈 Add a scoring system or timer to increase challenge.
- 📂 Save correct guesses to a JSON or CSV file for later review.
- 🎨 Improve map design with colors, borders, or state borders.
- 📊 Visualize the list of correct guesses with a bar chart or map overlay.

---

## 📚 License

This project is open-source and free to use.  
MIT License — see [LICENSE](LICENSE) for details.

---

## 🙌 Contributing

Feel free to open issues or submit pull requests for improvements!  
If you have ideas for new features, better visuals, or more states, let me know!

---

## 📞 Questions?

For any issues, suggestions, or bugs, reach out via GitHub Issues or contact [me](mailto:whoknows.camping830@passinbox.com).

---

> Built with ❤️ using Python, `pandas`, and `turtle` — simple, fun, and educational!
