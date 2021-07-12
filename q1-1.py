ARRAY_LENGTH = 5  # 배열의 행과 열 크기(고정)


def replaceData(numData):  # numData	2차원 정수 배열
    retData = []  # 조건에 따라서 전처리된 2차원 배열

    retData = numData[:]

    for i in range(ARRAY_LENGTH):
        for j in range(ARRAY_LENGTH):
            if retData[i][j] < 0:
                retData[i][j] = 0
            if retData[i][j] > 0:
                retData[i][j] = retData[i][j] % 100
            return retData


