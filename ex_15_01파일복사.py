# 파일 복사

# 1. 파일 복사 개념
# 파일 복사는 원본 파일 source의 복사본 파일 copy을 만드는 것
# 1) 원본 파일로 부터 파일의 내용을 읽어서 2) 변수에 저장한 뒤 3) 복사본 파일을 전송하면
# 간단하게 파일 복사를 구현 할 수 있음

# 2. 파일 복사 구현
# 텍스트 파일 뿐만 아니라 이미지, 동영상과 같은 바이너리 파일들도 파일 복사가 가능하도록
# 구현하기 위해서 바이너리 모드로 파일을 열여야 함
# 원본 파일의 내용을 읽을때


# 3. 동영상 파일을 복사
# 4. with문 사용
# close() 메소드의 호출이 자동으로 처리

# 5. 복사 단위
# 원본 파일을 한 번에 읽어서 모두 변수에 저장하려면 메모리 용량이 부담스러움
# 원본 파일에서 한 번에 읽어 들이는 데이터의 크기를 1kb(1024Byte)로 설정해 복사 프로그램을 구현


# 6. 복사 프로그램의 구현


buffer_size = 1024          # 1024 Byte 로 1 KB 를 의미 함
with open('./input/code.mp4', 'rb') as source :
    with open('./output/code2.mp4', 'wb') as copy :
        while True :
            buffer = source.read(buffer_size)   # buffer_size만큼 읽어 들이도록 구현
            if not buffer :     # if buffer == '' :
                break
            copy.write(buffer)

print('code2.mp4 파일이 복사되었습니다.')
