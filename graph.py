import matplotlib.pyplot as plt

plt.rc('font', family='D2Coding') # For MacOS

fig = plt.figure("Fuzzy AI")

distance = plt.subplot(3, 2, 1) #nrows = 3, ncols = 2, index = 1
plt.title('상대방 집까지 걸리는 시간(분)')
plt.plot([0, 15, 45], [1, 1, 0], 'go-')
plt.plot([15, 45, 90, 120], [0, 1, 1, 0], 'bo-')
plt.plot([90, 120, 140], [0, 1, 1], 'ro-')
# plt.xticks(visible=False)
plt.axis([0, 140, 0, 1.1])
plt.grid(True)

meetCount = plt.subplot(3, 2, 2) # index = 2
plt.title('한달에 만나는 횟수(번)')
plt.plot([0, 5, 10], [1, 1, 0], 'go-')
plt.plot([5, 10, 20, 25], [0, 1, 1, 0], 'bo-')
plt.plot([20, 25, 30], [0, 1, 1], 'ro-')
plt.axis([0, 30, 0, 1.1])
plt.grid(True)


replyTime = plt.subplot(3, 2, 3, sharex=distance) # nrows = 3, ncols = 2, index = 3, graph1 x축 공유
plt.title('답장이 오는데 걸리는 시간(분)')
plt.plot([0, 10, 40], [1, 1, 0], 'go-')
plt.plot([10, 40, 60, 90], [0, 1, 1, 0], 'bo-')
plt.plot([35, 120, 140], [0, 1, 1], 'ro-')
plt.axis([0, 140, 0, 1.1])
# plt.xlabel('time (m)', labelpad=10, fontdict={'color' : 'b', 'weight' : 'bold', 'size' : 12}, loc='right')
plt.grid(True)

questionMarks = plt.subplot(3, 2, 4) # index = 4
plt.title('일주일에 상대방이 보내는 물음표 갯수(개)')
plt.plot([0, 10, 20], [1, 1, 0], 'go-')
plt.plot([10, 20, 50, 60], [0, 1, 1, 0], 'bo-')
plt.plot([50, 60, 70], [0, 1, 1], 'ro-')
plt.axis([0, 70, 0, 1.1])
plt.grid(True)


graph5 = plt.subplot(3, 2, 5) # index = 5
plt.title('사귀 확률 (%)')
plt.plot([0, 5, 20], [1, 1, 0], 'go-')
plt.plot([5, 20, 30, 45], [0, 1, 1, 0], 'bo-')
plt.plot([30, 45, 55, 70], [0, 1, 1, 0], 'ro-')
plt.plot([55, 70, 80, 95], [0, 1, 1, 0], 'yo-')
plt.plot([80, 95, 100], [0, 1, 1], 'co-')
plt.axis([0, 100, 0, 1.1])
plt.grid(True)

plt.tight_layout()
plt.show()
