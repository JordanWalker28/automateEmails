def countTime(newList):
    timeList = []
    for i in newList:
        timeList.append(i[0:8])
    print(timeList)
    
    
    
newList = ["00:09:01.1078011",
"00:13:37.8615263",
"00:11:50.7668146",
"00:13:59.4735126",
"00:07:46.9573894",
"00:10:00.5683610",
"00:10:54.1271729",
"00:14:09.3492916",
"00:41:53.7395511",
"00:10:21.3569702",
"00:10:34.5580787"]

totalTime = countTime(newList)
