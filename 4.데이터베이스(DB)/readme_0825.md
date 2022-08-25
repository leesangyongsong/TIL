# 📚 0825 데이터베이스(DB)

## 📌 QuerySet API
```SQL
1. gt --초과
Entry.objects.filter(id__gt=4)
=> SELECT ... WHERE ID > 4; 와 대응

2. gte --이상
Entry.objects.filter(id__gte=4)
=> SELECT ... WHERE ID >= 4; 와 대응

3. lt --미만
Entry.objects.filter(id__lt=4)
=> SELECT ... WHERE ID < 4; 와 대응

4. lte --이하
Entry.objects.filter(id__lte=4)
=> SELECT ... WHERE ID <= 4; 와 대응

5. in -- 포함
Entry.objects.filter(id__in=[1, 3, 4])
=> SELECT ... WHERE id IN (1, 3, 4);

Entry.objects.filter(headline__in='abc')
=> SELECT ... WERER headline IN ('a', 'b', 'c');

6. startswith -- 포함
Entry.objects.filter(headline__startswith='Lennon')
=> SELECT ... WHERE headline LIKE 'Lennon%';

- istartswith -- 포함, 대소문자 상관없이
Entry.objects.filter(headline__istartswith='Lennon')
=> SELECT ... WHERE headline ILIKE 'Lennon%';

7. endswith -- 포함
Entry.objects.filter(headline__endswith='Lennon')
=> SELECT ... WHERE headline Like '%Lennon';

- iendswith -- 포함, 대소문자 상관없이
Entry.objects.filter(headline__iendswith='Lennon')
=> SELECT ... WHERE headline ILike '%Lennon';

8. contains -- 포함
Entry.object.get(headline__contains='Lennon')
=> SELECT ... WHERE headline LIKE '%Lennon%';

- icontains -- 포함, 대소문자 상관없이
Entry.object.get(headline__icontains='Lennon')
=> SELECT ... WHERE headline ILIKE '%Lennon%';

9. range
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
=> SELECT ... WHERE pub_date
   BETWEEN '2005-01-01' and '2005-03-31';

10. 복합활용
inner_qs = Blog.objects.filter(name__contains='Cheddar')
entrites = Entry.objects.filter(blog__in=inner_qs)

SELECT ...
WHERE blog.id IN 
(SELECT id FROM ... WHERE NAME LIKE '$Cheddar$')

-- 활용
Entry.objects.all()[0]
=> SELECT ... LIMIT 1;

Entry.objects.all()[2:5]
=> SELECT ... LIMIT 3 OFFSET 2;

Entry.objects.order_by('id') --오름차순
=> SELECT ... ORDER BY id;

Entry.objects.order_by('-id') --내림차순
=> SELECT ... ORDER BY id DESC;
```

## 📌 ORM 확장(1:N)
```SQL
-- 모델링(ORM)
class Genre(models.Model):
   name = models.CharField(max_length=30)

class Artist(models.Model):
   name = models.CharField(max_length=30)

class Album(models.Model):
   name = models.CharField(max_length=30)
   genre = models.ForeignKey('Genre',
on_delete=models.CASCADE)
   artist = models.ForeignKey('Artist',
on_delete=models.CASCADE)

-- Foreign Key (외래키)
   - 키를 사용하여 부모 테이블의 유일한 값을 참조(참조 무결성)
      - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
   - 외래 키의 값이 반드시 부모 테이블의 기본 키일 필요는 없지만
     유일한 값이어야 함

-- models.ForignKey 필드
   - 2개의 필수 위치 인자
      - Model class: 참조하는 모델
      - on_delete: 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
         - CASCADE: 부모 객체(참조된 객체)가 삭제 됐을 때
                    이를 참조하는 객체도 삭제 
         - PROTECT: 삭제되지 않음(ex: 댓글 있을 경우 삭제 x)
         - SET_NULL: NULL 설정
         - SET_DEFAULT: 기본 값 설정

-- Create
   artist = Artist.objects.get(id=1)
   genre = Genre.objects.get(id=1)

   album = Album()
   album.name = '앨범1'
   album.artist = artist -- 1. 객체의 저장
   album.genre = genre
   album.save()

-- 참조와 역참조
class Genre(models.Model):
   name = models.CharField(max_length=30)

class Artist(models.Model):
   name = models.CharField(max_length=30)

class Album(models.Model):
   name = models.CharField(max_length=30)
   genre = models.ForeignKey('Genre',
on_delete=models.CASCADE)
   artist = models.ForeignKey('Artist',
on_delete=models.CASCADE)

1. 참조
album = Album.objects.get(id=1)
album.artist
-- <Artist: Artist object (1)>
album.genre
-- <Genre: Genre object (1)>

2. 역참조
genre = Genre.objects.get(id=1)
genre.album_set.all()
-- <QuerySet 
--    [<Album: Album object (1)>, 
--    <Album: Album object (2)>
-- ]>
```