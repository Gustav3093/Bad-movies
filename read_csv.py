import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter = ',')
      header = next(reader)
      data = []        
      for row in reader: 
        iterable = zip(header, row, strict = True)
        print(list(iterable))
        names_dict = dict(iterable)
        data.append(names_dict)
        return data       
     


if __name__ == '__main__':
    read_csv('./app/data.csv')
  