# π μκ³ λ¦¬μ¦ 6μΌμ°¨

## π 0. λ°μ΄ν° κ΅¬μ‘° & μκ³ λ¦¬μ¦
```python
νλ‘κ·Έλ¨ = λ°μ΄ν° κ΅¬μ‘° + μκ³ λ¦¬μ¦

Data Structure λ°μ΄ν° κ΅¬μ‘°
: λ°μ΄ν°λ₯Ό λ€μν λ°©μμΌλ‘ μ μ₯νκ³  + μ‘°ν, μ½μ, λ³κ²½, μ­μ μ κ°μ μ‘°μ κΈ°λ₯ μ κ³΅νλ€.

# μ λ°μ΄ν° κ΅¬μ‘°κ° μ€μνκ°?
μλ¬΄λ°λ λ΄κΈ° ~= λ³μ
'λ¬Έμ  μν©'μ λ°λΌ λ μ ν©ν λκ΅¬(ν΅)μ΄ νμνλ€!

λ°μ΄ν°λ₯Ό νμμ λ°λΌ μ μ₯νκ³  νμ©ν  μ μμΌλ―λ‘ 
λ¬Έμ λ₯Ό λ ν¨μ¨μ μΌλ‘ νκΈ° μν λκ΅¬κ° λλ€. 

=> μ΄λ»κ² μ μ₯νκ³  & μ΄λ»κ² νμ©(μ‘°μ)ν  μ μλμ§

μ μ¨μΌ νλμ§(why)
λ°μ΄ν° κ΅¬μ‘°λ₯Ό λ°°μ°λ μ΄μ : μ λ§λ€μ΄μ‘κ³ , μΈμ  μ¨μΌνλμ§ μκΈ° μν΄
```

## π 1. μ€ν(Stack)
```python
# μ€ν(Stack)μ΄λ?
: μ€νμ μλλ€λ μλ―Έλ‘μ¨, 
λ§μΉ μ μλ₯Ό μκ³  λΉΌλ―μ΄ 'λ°μ΄ν°λ₯Ό νμͺ½μμλ§ λ£κ³  λΉΌλ μλ£κ΅¬μ‘°' 
κ°μ₯ λ§μ§λ§μ λ€μ΄μ¨ λ°μ΄ν°κ° κ°μ₯ λ¨Όμ  λκ°λ―λ‘ LIFO(Last-in First-out, νμμ μΆ λ°©μ)

# μ€ν μλ£κ΅¬μ‘°μ λν λμ
push : μ€νμ μλ‘μ΄ λ°μ΄ν°λ₯Ό μ½μνλ νμ
pop : μ€νμ κ°μ₯ λ§μ§λ§ λ°μ΄ν°λ₯Ό κ°μ Έμ€λ νμ

# μ μ€νμ μ¨μΌν κΉ(why)?
=> λ°μ΄ν° κ΅¬μ‘°λ₯Ό λ°°μ°λ μ΄μ : μ λ§λ€μ΄μ‘κ³ , μΈμ  μ¨μΌνλμ§ μκΈ° μν΄
  1. λ€μ§κΈ°, λλλ¦¬κΈ°, λλμκ°κΈ° 
    ex) μΉλΈλΌμ°μ  νμ€ν λ¦¬, μλμ° νμκΈ°, ctrl + z, λ¨μ΄ λ€μ§κΈ° λ±
  2. λ§λ¬΄λ¦¬λμ§ μμ μΌμ μμ μ μ₯
    ex) κ΄νΈ λ§€μΉ­, ν¨μ νΈμΆ, λ°±νΈλνΉ, DFS(κΉμ΄ μ°μ  νμ)

# νμ΄μ¬μ 'λ¦¬μ€νΈ'λ‘ μ€νμ κ°νΈνκ² μ¬μ©ν  μ μλ€!

# μκ³ λ¦¬μ¦ λ¬Έμ νμ΄ μ κ·Όλ°©μ
λ¬Έμ  μ΄ν΄ -> μμ νμ -> νμμλ λ΄μ© μ§μ°κΈ° 
```

## π 2. ν(Queue)
```python
# ν(Queue)λ?
: ν μͺ½ λμμ λ°μ΄ν°λ₯Ό λ£κ³ , λ€λ₯Έ νμͺ½μμλ§ λ°μ΄ν°λ₯Ό λΊ μ μλ μλ£κ΅¬μ‘°
κ°μ₯ λ¨Όμ  λ€μ΄μ¨ λ°μ΄ν°κ° κ°μ₯ λ¨Όμ  λκ°λ―λ‘ FIFO(First-in First-out, μ μμ μΆ) λ°©μ

dequeue: νμ λ§¨ μ λ°μ΄ν°λ₯Ό κ°μ Έμ€λ νμ
enqueue: νμ λ§¨ λ€μ λ°μ΄ν°λ₯Ό μ½μνλ νμ

# ν μλ£κ΅¬μ‘°λ νμ΄μ¬ 'λ¦¬μ€νΈ'λ‘ κ°νΈνκ² μ¬μ©ν  μ μλ€!

# λ¦¬μ€νΈλ₯Ό μ΄μ©ν ν μλ£κ΅¬μ‘°μ λ¨μ 
: λ°μ΄ν°λ₯Ό λΊ λ ν μμ μλ λ°μ΄ν°κ° λ§μ κ²½μ° 'λΉν¨μ¨μ 'μ΄λ€.
λ§¨ μ λ°μ΄ν°κ° λΉ μ§λ©΄μ, λ¦¬μ€νΈμ μΈλ±μ€κ° νλμ© λΉκ²¨μ§κΈ° λλ¬Έμ΄λ€!

# λ±(Deque, Double-Ended Queue) μλ£κ΅¬μ‘°
== μ λ°©ν₯μΌλ‘ μ½μκ³Ό μ­μ κ° μμ λ‘μ΄ ν
== μ λ°©ν₯ μ½μ, μΆμΆμ΄ λͺ¨λ νλ³΄λ€ ν¨μ¬ λΉ λ₯΄λ€.
==> λ°λΌμ λ°μ΄ν°μ μ½μ μΆμΆμ΄ λ§μ κ²½μ°, μκ°μ ν¬κ² λ¨μΆμν¬ μ μλ€.

 appendleft(), popleft() <-> | Deque | <-> append(), pop()
```

![μ€νvsν](%EC%8A%A4%ED%83%9Dvs%ED%81%90.png)