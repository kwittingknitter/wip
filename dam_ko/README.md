## About

Scripts for generating minimal pair sentences exhibiting differential argument markers in Korean

### Dataset format
```
{
    "context": "",
    "sentence_good": "",
    "sentence_bad": "",
    "dam_type": "",      # "s" for subject, "t" for topic, "o" for object
    ""
}
```

#### Dataset example

Subject example:
```
{
    "context": "지민과 수지가 버스를 기다리고 있다. 버스가 다가오는 걸 본 수지는 지민에게 말한다:",
    "sentence_good": "버스 온다.",
    "sentence_bad": "버스가 온다.",
    "dam_type": "s",
},
```

Topic example:
```
{
    "context": "지민과 수지가 집에 가려는데 버스를 탈지 택시를 잡을지 고민중이다. 택시는 10분 걸린다고 지민이 얘기 하자마자 버스가 다가오는 걸 본 수지는 지민에게 말한다:",
    "sentence_good": "버스 온다. 택시는 포기하자.",
    "sentence_bad": "버스 온다. 택시 포기하자.",
    "dam_type": "t",
},
```

Object example:
```
{
    "context": "점심때 지민과 수지는 따로 먹었다. 지민은 라면 먹고 수지는 김밥 먹었다. 수업 시작전에 수지가 지민한테 점심때 뭐 먹었는지 물어본다. 지민의 대답은:",
    "sentence_good": "라면 먹었어",
    "sentence_bad": "라면을 먹었어",
    "dam_type": "o",
},
```