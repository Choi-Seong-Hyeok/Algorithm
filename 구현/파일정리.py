N = int(input())
files = list()
extension_count = {}

# 파일 입력 받기
for _ in range(N):
    val = str(input())
    files.append(val)

# 확장자 별로 파일 개수 세기
for file in files:
    extension = file.split('.')[-1]
    extension_count[extension] = extension_count.get(extension, 0) + 1

# 확장자 정렬
sorted_extensions = sorted(extension_count.keys())

# 결과 출력
for ext in sorted_extensions:
    print(ext, extension_count[ext])
