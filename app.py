# Netflix Dashboard - My First Streamlit App!
# I'm creating this to practice making interactive dashboards

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Set up the page - this makes it look nice
st.set_page_config(
    page_title="Netflix Dashboard",
    page_icon="🎬",
    layout="wide"
)

# Step 2: Add a title and description
st.title("🎬 Netflix Content Analysis Dashboard")
st.markdown("#### Exploring Netflix's Movies and TV Shows")
st.markdown("---")

# Step 3: Load the data (using cache so it doesn't reload every time)
@st.cache_data
def load_data():
    """Load and clean the Netflix data"""
    import os
    
    # Check if file exists locally, if not download it
    if not os.path.exists('netflix_titles.csv'):
        try:
            import kagglehub
            # Download the dataset from Kaggle
            path = kagglehub.dataset_download("shivamb/netflix-shows")
            # Copy to current directory
            import shutil
            shutil.copy(os.path.join(path, 'netflix_titles.csv'), 'netflix_titles.csv')
        except:
            st.error("Unable to download dataset. Please check your internet connection.")
            st.stop()
    
    # Read the CSV file
    df = pd.read_csv('netflix_titles.csv')
    
    # Clean the data like we did in the notebook
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    
    # Remove rows with missing critical info
    df = df.dropna(subset=['date_added', 'title', 'type'])
    
    return df

# Load the data
df = load_data()

# Step 4: Show some basic stats at the top
st.subheader("📊 Quick Stats")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Titles", f"{len(df):,}")
    
with col2:
    movies_count = len(df[df['type'] == 'Movie'])
    st.metric("Movies", f"{movies_count:,}")
    
with col3:
    shows_count = len(df[df['type'] == 'TV Show'])
    st.metric("TV Shows", f"{shows_count:,}")
    
with col4:
    countries_count = df['country'].nunique()
    st.metric("Countries", f"{countries_count}")

st.markdown("---")

# Step 5: Add a sidebar for filters
st.sidebar.header("🎛️ Filters")
st.sidebar.markdown("Use these to explore different parts of the data")

# Filter by content type
content_type = st.sidebar.multiselect(
    "Select Content Type:",
    options=['Movie', 'TV Show'],
    default=['Movie', 'TV Show']
)

# Filter by year range
min_year = int(df['year_added'].min())
max_year = int(df['year_added'].max())
year_range = st.sidebar.slider(
    "Select Year Range:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Apply filters to the data
filtered_df = df[
    (df['type'].isin(content_type)) & 
    (df['year_added'] >= year_range[0]) & 
    (df['year_added'] <= year_range[1])
]

st.sidebar.markdown(f"**Showing {len(filtered_df)} titles**")

# Step 6: Create visualizations
st.subheader("📈 Visualizations")

# First row: Pie chart and bar chart
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### Movies vs TV Shows")
    # Count content types
    type_counts = filtered_df['type'].value_counts()
    
    # Create pie chart
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['#E50914', '#221F1F']
    ax.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%',
           colors=colors, startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    plt.close()
    
    # Show caption only if Movie exists in the filtered data
    if 'Movie' in type_counts.index and len(filtered_df) > 0:
        st.caption(f"📝 Movies make up {type_counts['Movie']/len(filtered_df)*100:.1f}% of the content")
    else:
        st.caption(f"📝 Showing {len(filtered_df)} titles")

with col2:
    st.markdown("##### Top 10 Genres")
    # Get top 10 genres
    genre_counts = filtered_df['listed_in'].value_counts().head(10)
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(range(len(genre_counts)), genre_counts.values, color='#E50914')
    ax.set_yticks(range(len(genre_counts)))
    ax.set_yticklabels(genre_counts.index)
    ax.set_xlabel('Number of Titles')
    ax.set_title('Most Popular Genres')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    # Show caption
    if len(genre_counts) > 0:
        st.caption(f"📝 '{genre_counts.index[0]}' is the most popular genre")

st.markdown("---")

# Second row: Line chart for trends
st.markdown("##### 📊 Content Added Over Time")
yearly_data = filtered_df.groupby('year_added').size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(yearly_data['year_added'], yearly_data['count'], 
        marker='o', linewidth=2, markersize=6, color='#E50914')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Titles Added')
ax.set_title('Netflix Content Growth')
ax.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig)
plt.close()

# Find peak year
if len(yearly_data) > 0:
    peak_year = yearly_data.loc[yearly_data['count'].idxmax(), 'year_added']
    peak_count = yearly_data['count'].max()
    st.caption(f"📝 Netflix added the most content in {int(peak_year)} with {peak_count} titles")

st.markdown("---")

# Third row: Countries and Ratings
col1, col2 = st.columns(2)

with col1:
    st.markdown("##### 🌍 Top 10 Countries")
    country_counts = filtered_df['country'].value_counts().head(10)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(range(len(country_counts)), country_counts.values, color='#E50914')
    ax.set_yticks(range(len(country_counts)))
    ax.set_yticklabels(country_counts.index)
    ax.set_xlabel('Number of Titles')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    if len(country_counts) > 0:
        top_country = country_counts.index[0]
        st.caption(f"📝 {top_country} produces the most content")

with col2:
    st.markdown("##### 🎭 Content Ratings")
    rating_counts = filtered_df['rating'].value_counts()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(range(len(rating_counts)), rating_counts.values, color='#221F1F')
    ax.set_xticks(range(len(rating_counts)))
    ax.set_xticklabels(rating_counts.index, rotation=45, ha='right')
    ax.set_ylabel('Number of Titles')
    plt.tight_layout()
    st.pyplot(fig)
    plt.close()
    
    if len(rating_counts) > 0:
        top_rating = rating_counts.index[0]
        st.caption(f"📝 '{top_rating}' is the most common rating")

st.markdown("---")

# Footer
st.markdown("### 💡 Key Insights")
col1, col2 = st.columns(2)

with col1:
    st.info(f"""
    **Content Mix:** 
    - Movies: {len(filtered_df[filtered_df['type']=='Movie'])} ({len(filtered_df[filtered_df['type']=='Movie'])/len(filtered_df)*100:.1f}%)
    - TV Shows: {len(filtered_df[filtered_df['type']=='TV Show'])} ({len(filtered_df[filtered_df['type']=='TV Show'])/len(filtered_df)*100:.1f}%)
    """)

with col2:
    st.info(f"""
    **Geographic Reach:**
    - Content from {df['country'].nunique()} different countries
    - US dominates with the most titles
    """)

st.markdown("---")
st.markdown("**Data Source:** Netflix Movies and TV Shows (Kaggle)")
st.markdown("*Built with Streamlit - My first interactive dashboard!* 🎉")
