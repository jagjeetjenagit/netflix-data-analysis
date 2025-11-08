# Netflix Dashboard - Streamlit App

A simple interactive dashboard I built to visualize Netflix content data using Streamlit.

## 🎯 What It Does

This dashboard lets you:
- View key stats (total titles, movies, shows, countries)
- Filter data by content type (Movies/TV Shows) and year range
- See interactive visualizations:
  - Movies vs TV Shows distribution (pie chart)
  - Top 10 genres (bar chart)
  - Content growth over time (line chart)
  - Top countries producing content (bar chart)
  - Content ratings distribution (bar chart)

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make sure you have the data file:**
   - Place `netflix_titles.csv` in the same folder as `app.py`
   - You can download it from Kaggle: [Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

3. **Run the dashboard:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, just copy that URL into your browser

## 📦 Requirements

- Python 3.7+
- streamlit
- pandas
- matplotlib
- seaborn
- numpy

## 🎨 Features

- **Interactive Filters** - Use the sidebar to filter by content type and year
- **Real-time Updates** - Charts update automatically when you change filters
- **Clean Design** - Simple, beginner-friendly layout
- **Netflix Colors** - Uses Netflix's red (#E50914) and black (#221F1F) theme

## 📝 What I Learned

Building this dashboard helped me practice:
- Creating interactive web apps with Streamlit
- Data visualization with Matplotlib
- Adding filters and user controls
- Structuring a dashboard layout
- Caching data for better performance

## 🎓 Perfect for Interviews

This project demonstrates:
- Python data visualization skills
- Building interactive dashboards
- Clean, readable code
- User-friendly interface design

---

*Built as a learning project to practice Streamlit and data visualization!*
