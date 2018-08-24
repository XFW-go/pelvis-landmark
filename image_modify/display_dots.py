import cv2
import json


def Myfind(line, st, ed):
    pos0 = line.find('\'', st, ed)
    pos1 = line.find('jpg', st, ed)
    picn = line[pos0+1:pos1+3]  # pic_name
    pos0 = line.find('[', st, ed)
    pos1 = line.find(']', st, ed)
    my_data = []   # 存放同一张图的所有数据
    user_id = []  # 存放对于同一张图，来标过的id
    dat = []      # 存放一个id标的所有点
    while pos0 != -1:
        pos2 = pos0 + 1  # 找到方括号即一个id的数据找到了，+1后开始用json.loads转换成字典
        pos3 = 0  # 每一个json右括号的位置
        while pos2 < pos1:
            pos3 = line.find('}', pos2, ed)
            data = json.loads(line[pos2:pos3+1])
            dat.append(data)
            pos2 = line.find('{', pos3, ed)

        my_data.append(dat)

        pos4 = line.find('user', pos3, ed)
        pos4 += 9
        pos5 = pos4 + 1
        if line[pos4+1] != '\"':
            pos5 += 1
        user_id.append(line[pos4:pos5])

        pos0 = line.find('[', pos0 + 1, ed)
        pos1 = line.find(']', pos0 + 1, ed)

    return my_data, picn, user_id


file_name = 'image.txt'
with open(file_name) as f:
    for line in f.readlines():
        l1 = len(line)
        info, pic_name, ID = Myfind(line, 0, l1)
        l2 = len(info)  # num of people who pick the picture
        for i in range(l2):
            inf = info[i]
            l3 = len(inf)
            if l3 != 11 and l3 != 12 and l3 != 21 and l3 != 23:  # invalid data
                print("\nBAD CASE!!!!!!!!!!!!!!!!")
            path = "./***/"  # the pictures' location
            pic = cv2.imread(path + pic_name, 0)
            for j in range(l3):
                pt = inf[j]
                cv2.circle(pic, (pt['x'], pt['y']), pt['r'], (0, 0, 255))
            print('\n', ID[i], '\n')  # UserID
            cv2.imshow("pic", pic)
            cv2.waitKey(0)

