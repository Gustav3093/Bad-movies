import charts
import read_csv
import utils

def run():
  review_count, rating = utils.get_review_count_and_rating('./app/data.csv')
  result = utils.get_movies_points(review_count, rating)
  if len(result) > 0:
      labels, values = result
      charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()