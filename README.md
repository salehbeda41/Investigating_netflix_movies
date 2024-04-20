# Movie Duration Analysis

This project is part of the Associate Data Science track in Datacamp. The goal of this project is to perform exploratory data analysis on a dataset containing information about movies available on Netflix. Specifically, we aim to investigate whether movies are getting shorter over time and explore possible contributing factors.

## Dataset

The dataset used in this project, `netflix_data.csv`, belongs to Datacamp and contains the following columns:

- `show_id`: The ID of the show
- `type`: Type of show (e.g., Movie, TV Show)
- `title`: Title of the show
- `director`: Director of the show
- `cast`: Cast of the show
- `country`: Country of origin
- `date_added`: Date added to Netflix
- `release_year`: Year of Netflix release
- `duration`: Duration of the show in minutes
- `description`: Description of the show
- `genre`: Show genre

## Analysis Steps

1. **Data Loading and Filtering**: We load the dataset and filter out TV shows to focus only on movies.

2. **Subsetting Data**: We subset the movie data to include only relevant columns such as title, country, genre, release year, and duration.

3. **Short Movie Analysis**: We identify movies shorter than 60 minutes and inspect possible contributing factors.

4. **Genre Analysis**: We categorize movies into four genre groups (Children, Documentaries, Stand-Up, and Other) and visualize their distribution over the years.

5. **Visualization**: We create a scatter plot of movie duration by release year, using colors to represent different genre groups.

6. **Conclusion**: Based on our analysis, we provide insights into whether movies are getting shorter over time.

## Dependencies

This project requires the following Python libraries:

- pandas
- matplotlib

You can install them using pip:

```
pip install pandas matplotlib
```

## Usage

To run the analysis, follow these steps:

1. Clone this repository to your local machine.
2. Download the dataset `netflix_data.csv` from the Datacamp platform and place it in the project directory.
3. Run the `main.py` Python script to execute the analysis steps.

## File Structure

- `main.py`: Python script containing the analysis code.
- `netflix_data.csv`: Dataset containing information about movies on Netflix.
- `LICENSE`: MIT License file.

## Contributors

- Saleh Beddah

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
