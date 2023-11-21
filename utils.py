import csv

def get_review_count_and_rating(csv_filename):
  
  with open(csv_filename, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    review_count = 0
    rating = 0
    for row in csv_reader:
      review_count += 1
      rating += int(row[1])
  return review_count, rating

   

def get_movies_points(review_count, rating):
    rating = {
        'Rating': int(rating['review_count']),
        'Review': int(review_count),
    }
    labels = list(rating.keys())
    values = list(rating.values())
    return labels, values