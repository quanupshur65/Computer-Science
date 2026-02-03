class Review:
    def __init__(self, rating, text):
        self.rating = rating
        self.text = text

    def print_review(self):
        print("Rating:", self.rating, "/ 5")
        print("Review", self.text)


class Movie:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def average_rating(self):
        total = 0
        for review in self.reviews:
            total += review.rating 
        return total / len(self.reviews) if self.reviews else 0
    def show_reviews(self):
        for review in self.reviews:
            review.print_review()
            print()

    def best_review(self):
        highest = self.reviews[0].rating
        best_reviews = []

        for review in self.reviews:
            if review.rating > highest:
                highest = review.rating

        for review in self.reviews:
            if review.rating == highest:
                best_reviews.append(review)
    
        return best_reviews
    def worst_review(self):
        lowest = self.reviews[0].rating
        worst_reviews = []

        for review in self.reviews:
            if review.rating < lowest:
                lowest = review.rating

        for review in self.reviews:
            if review.rating == lowest:
                worst_reviews.append(review)

        return worst_reviews

movie = Movie("Cars")
review1 = Review(5, "Awesome racing scenes and funny characters.")
review2 = Review(4, "Very entertaining and fast paced.")
review3 = Review(3, "Good movie but mostly for kids.")
review4 = Review(2, "Not enough action for me.")

movie.add_review(review1)
movie.add_review(review2)
movie.add_review(review3)
movie.add_review(review4)

print("Movie:", movie.title)
print("/nAll Reviews:")
movie.show_reviews()

print("Average Rating", movie.average_rating())

print("/nBest Review:")
movie.best_review()[0].print_review()

print("/nWorst Review:")
movie.worst_review()[0].print_review()