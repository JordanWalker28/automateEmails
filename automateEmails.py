import datetime

def countTime(newList):
    timeList = []
    for i in newList:
        i = i[0:8]
        timeList.append(i)

    time = convertTime(timeList)
    print(time)
    

def convertTime(time):
    totalSecs = 0
    for tm in time:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)
    return ("%d:%02d:%02d" % (hr, min, sec))
    
    
newList = ["Test1 0 00:09:01.1078011",
"Test2 0 00:13:37.8615263",
"Test3 0 00:11:50.7668146",
"Test4 0 00:13:59.4735126",
"Test5 0 00:07:46.9573894",
"Test6 0 00:10:00.5683610",
"Test7 0 00:10:54.1271729",
"Test8 0 00:14:09.3492916",
"Test9 0 00:41:53.7395511",
"Test10 0 00:10:21.3569702",
"Test11 1 00:10:34.5580787"]

Tests = []
PassFails = []
Times = []

for i in newList:
    i = i.split(" ")
    Tests.append(i[0])
    PassFails.append(i[1])
    Times.append(i[2])

totalTime = countTime(Times)
