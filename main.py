class Uma:
    # 말딸 이름, 스펙, 전적 등등 저장? 말 개개인에게 저장하는게 좋을듯? -아니 각 시행횟수별로 저장해야 안 꼬인다
    # 어떤 거리 담당인지?

    pyoi = True

class TeamRace:
    # 각 팀레이스 시도별로 새 클래스를 만들어서 저장?
    # 경기별 경기장정보, 거리정보, 착순 저장

    short_length = 1000

    # ㄴ 이게 아니라 Race 자료형으로 해서 저장하는것

class Race:
    #팀레이스 각 경기 레이스 시도의 저장?
    #length는 거리, type는 어떤경기였는지
    #경기장 이름도 저장할까?
    length = 0
    type = 0
    where = 0

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


myteam = Team()
#프로그램에서 불러올 팀?

# 아 모르겠다 데이터베이스를 공부하자