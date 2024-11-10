X=[]
def prime_finder(n):
  prime_numbers=[]
  for i in range(2,n+1):
    Prime=True
    for num in range(2,int(i**0.5)+1):
      if i%num==0:
        Prime=False
        break
    if Prime:
      prime_numbers.append(i)
  return prime_numbers
