class Uma:
    # 말딸 이름, 스펙, 전적 등등 저장? 말 개개인에게 저장하는게 좋을듯? -아니 각 시행횟수별로 저장해야 안 꼬인다
    # 어떤 거리 담당인지?

    pyoi = True

class Race:
    # 각 레이스별로 새 클래스를 만들어서 저장?
    # 경기별 경기장정보, 거리정보, 착순 저장

    short_length = 1000

class Team:
    # 지금 내가 갖고있는 애들 정보를 저장해서 일일이 레이스별로 입력할 필요 없이 Race 클래스를 만들 때 불러온다.

    # 단거리 1번마, 2번마, 3번마 이런식으로?
    short = []
    mile = []
    midium = []
    long = []
    dirt = []

    def change_member(a, b):
        # team 의 멤버를 바꾸는 함수로 하자.
        # a에 거리적성, b에 번호를 넣어서 그번호 바꾸기
        pyoi = a