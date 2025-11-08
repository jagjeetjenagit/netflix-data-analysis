# Netflix Data Analysis Project

A beginner-friendly exploratory data analysis of Netflix's content catalog using Python, pandas, and matplotlib.

## 🎯 Project Overview

This project explores Netflix's movies and TV shows to understand:
- Content distribution (Movies vs TV Shows)
- Popular genres and trends
- Content growth over time  
- Geographic distribution of content
- Target audience analysis through ratings

## 📊 What I Discovered

- **Movies dominate** - About 70% of Netflix content are films
- **US leads production** - American content makes up the largest portion
- **Mature audience focus** - TV-MA and TV-14 ratings are most common
- **Steady growth** - Clear pattern of content expansion over the years

## 🛠️ Tools Used

- **Python** - Main programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Creating visualizations
- **Seaborn** - Enhanced statistical plots
- **Kaggle** - Data source (Netflix Movies and TV Shows dataset)

## 📁 Files

- `netflix_analysis.ipynb` - Main Jupyter notebook with complete analysis
- `app.py` - **Streamlit dashboard** for interactive visualization
- `requirements.txt` - Python dependencies
- `README.md` - This file
- `DASHBOARD_README.md` - Dashboard-specific documentation

## 🚀 How to Run

### Option 1: Jupyter Notebook Analysis
1. Clone this repository
2. Install required packages: `pip install pandas matplotlib seaborn kagglehub`
3. Open `netflix_analysis.ipynb` in Jupyter Notebook or VS Code
4. Run all cells to see the analysis

### Option 2: Interactive Streamlit Dashboard
1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `streamlit run app.py`
4. Open your browser at `http://localhost:8501`

**Note:** The Netflix dataset will be automatically downloaded when you run either the notebook or dashboard.

## 📈 Key Visualizations

1. **Pie Chart** - Movies vs TV Shows distribution
2. **Bar Chart** - Top 10 most popular genres
3. **Line Plot** - Content added per year (growth trends)
4. **Heatmap** - Top countries by content volume
5. **Bar Chart** - Content ratings distribution

## 🎓 Learning Goals

This project helped me practice:
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Creating meaningful visualizations
- Drawing insights from real-world data
- Storytelling with data
- **Building interactive dashboards with Streamlit**
- **Creating web applications for data visualization**

## 💡 Next Steps

- Analyze content duration patterns
- Explore director and cast data
- Compare Netflix with other streaming platforms
- Add interactive visualizations with Plotly

---

*This is a learning project created to practice data science fundamentals with real Netflix data.*