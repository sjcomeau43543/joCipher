import argparse, re

num = ''
first = ''
second = ''
third = ''

def setup():
  global num
  global first
  global second
  global third
  global non
  num += '1'
  num += '2'
  num += '3'
  num += '4'
  num += '5'
  num += '6'
  num += '7'
  num += '8'
  num += '9'
  num += '0'
  first += 'q'
  first += 'w'
  first += 'e'
  first += 'r'
  first += 't'
  first += 'y'
  first += 'u'
  first += 'i'
  first += 'o'
  first += 'p'
  second += 'a'
  second += 's'
  second += 'd'
  second += 'f'
  second += 'g'
  second += 'h'
  second += 'j'
  second += 'k'
  second += 'l'
  third += 'z'
  third += 'x'
  third += 'c'
  third += 'v'
  third += 'b'
  third += 'n'
  third += 'm'

def encode(string, shift):
  result = ""

  # go through the string
  for i in range(len(string)):
    char = string.lower()[i]

    # encode it
    if char in num:
      new_char = num[(num.index(char)+shift)%len(num)]
      result += new_char
    elif char in first:
      new_char = first[(first.index(char)+shift)%len(first)]
      if string[i].isupper():
        result += new_char.upper()
      else:
        result += new_char
    elif char in second:
      new_char = second[(second.index(char)+shift)%len(second)]
      if string[i].isupper():
        result += new_char.upper()
      else:
        result += new_char
    elif char in third:
      new_char = third[(third.index(char)+shift)%len(third)]
      if string[i].isupper():
        result += new_char.upper()
      else:
        result += new_char
    else:
      result += char
  
  print result
  return 0

def decode(string, shift):
  result = ""
  shift = -1 * shift

  # go through the string
  for i in range(len(string)):
    char = string.lower()[i]

    # decode it
    if char in num:
      new_char = num[(num.index(char)+shift)%len(num)]
      result += new_char
    elif char in first:
      new_char = first[(first.index(char)+shift)%len(first)]
      if string[i].isupper():
        result += new_char.upper()
      else:
        result += new_char
    elif char in second:
      new_char = second[(second.index(char)+shift)%len(second)]
      if string[i].isupper():
        result += new_char.upper()
      else:
        result += new_char
    elif char in third:
      new_char = third[(third.index(char)+shift)%len(third)]
      if string[i].isupper():
        result += new_char.upper()
      else:
        result += new_char
    else:
      result += char
  
  print result
  return 0

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--string', '-s', type=str, required=True, help="the string to encode or decode")
  parser.add_argument('--shift', '-t', type=int, required=True, help="the shift value to use")
  parser.add_argument('--encode', '-e', required=False, action="store_true", help="encode the string")
  parser.add_argument('--decode', '-d', required=False, action="store_true", help="decode the string")

  args = parser.parse_args()

  setup()

  p = re.compile('[a-zA-Z0-9\-{}]')

  if p.match(args.string) is not None:
    if args.encode:
      ret = encode(args.string, args.shift)
    elif args.decode:
      ret = decode(args.string, args.shift)
    if ret is not 0:
      print 'Sorry, this cipher only uses the [a-zA-Z0-9\-{}]'
  else:
    print 'Sorry, this cipher only uses the [a-zA-Z0-9\-{}]'


if __name__ == '__main__':
  main()

