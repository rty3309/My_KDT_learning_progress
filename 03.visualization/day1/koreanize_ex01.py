import matplotlib.pyplot as plt
import koreanize_matplotlib    # 한글 출력

plt.plot([-1,0,1,2])    # y축 데이터
plt.title('그래프 제목', fontweight='bold')
plt.xlabel('간단한 그래프')
plt.show()