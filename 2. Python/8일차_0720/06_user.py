import lotto_class

#인스턴스
lotto = lotto_class.Lotto()
lotto.generate_lotto() # 로또 생성
print(lotto.numbers) 
print(lotto.get_money([1, 2, 3, 4, 5, 6]))