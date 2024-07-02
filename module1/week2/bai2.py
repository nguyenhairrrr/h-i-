def count_char(string):
  return {string[i]: string.count(string[i]) for i in range(len(string))}
string = 'Hai'
count_char(string)
