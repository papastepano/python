# Write your solution here:
class Series:
    def __init__(self, name: str, seasons: int, genres: list):
        self.name = name
        self.seasons = seasons
        self.genres = genres
        self.rating = []

    def __str__(self):
        genres_str = ", ".join(self.genres)
        ratings = ""
        if self.rating:
            ratings += f"{len(self.rating)} ratings, "
            ratings += f"average {sum(self.rating) / len(self.rating):.1f} points"
        else:
            ratings  += "no ratings"
        return f"{self.name} ({self.seasons} seasons)\ngenres: {genres_str}\n{ratings}"

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.rating.append(rating)
        else:
            raise ValueError("Rating must be between 0 and 5")

def minimum_grade(grade: float, series: list):
    result = []
    for series in series:
        if sum(series.rating) / len(series.rating) >= grade:
            series.title = series.name
            result.append(series)
    return result


def includes_genre(genre: str, series_list: list):
    result = []
    for series in series_list:
        if genre in series.genres:
            series.title = series.name
            result.append(series)
    return result

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series)
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)