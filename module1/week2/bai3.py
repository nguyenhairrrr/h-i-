a_file = open('/content/P1_data.txt', 'r')
data = a_file.read()
a_file.close()
def word_count(data):
  data = data.lower()
  data = data.split()
  return {data[i]: data.count(data[i]) for i in range(len(data))}
word_count(data)
