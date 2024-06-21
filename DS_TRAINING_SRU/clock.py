n=int(input())
hr=n//3600
n=n%3600
mi=n//60
sec=n%60
print(hr,"hr:",mi,"m:",sec,"s")