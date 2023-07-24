from django.db import models

# Create your models here.


class parentModel(models.Model):
    id = models.AutoField(primary_key=True)


class childModel(models.Model):
    id = models.AutoField(primary_key=True)  # 자동으로 고유 값이 생성되는 기본키 필드
    integer = models.IntegerField()  # 정수형 필드
    small_text = models.CharField(max_length=100)  # 텍스트 필드, 범위 정할 수 있음
    large_text = models.TextField()  # 텍스트 필드, 텍스트의 양이 많을 때 사용
    date = models.DateField()  # 날짜 필드
    foreign = models.ForeignKey(
        parentModel, on_delete=models.CASCADE)  # 외부키 필드
    # 느낌이 parentModel 데이터 한 개에 childModel 여러 데이터가 연결되는 것
    # on_delete (CASCADE) : 대상의 모델(parentModel)의 데이터가 삭제될 경우 이 모델도 같이 삭제 하겠다는 것

    # 텍스트 필드 선택형
    # 앞에는 models에서 지정하는 값이고 뒤에는 관리자 페이지에서 실제로 보여지는 값
    REPAIR_CHOICES = [
        ('B', '수리전'),
        ('A', '수리후'),
    ]
    repair_state = models.CharField(
        max_length=1,
        choices=REPAIR_CHOICES,
        default='B'
    )

    # 추가로 admin 페이지에서 데이터 타이틀로 뜰 요소를 정하는 것
    def __str__(self):
        return str(self.id)
