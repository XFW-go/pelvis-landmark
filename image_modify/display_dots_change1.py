import cv2
import json


def Myfind(line, st, ed):
    pos0 = line.find('\'', st, ed)
    pos1 = line.find('jpg', st, ed)
    picn = line[pos0+1:pos1+3]  # pic_name
    pos0 = line.find('[', st, ed)
    pos1 = line.find(']', st, ed)
    my_data = []
    user_id = []

    while pos0 != -1:
        dat = []
        pos2 = pos0 + 1
        pos3 = 0
        data = []

        while pos2 < pos1:
            pos3 = line.find('}', pos2, ed)
            
            data = json.loads(line[pos2:pos3+1])
            dat.append(data)

            pos2 = line.find('{', pos3, ed)
            if pos2 == -1:
                break

        pos4 = line.find('userID', pos3, ed)

        pos4 += 9
        pos5 = pos4 + 1
        if line[pos4+1] != '\"':
            pos5 += 1

        my_data.append(dat)
        user_id.append(line[pos4:pos5])

        pos0 = line.find('[', pos0 + 1, ed)
        pos1 = line.find(']', pos0 + 1, ed)

    return my_data, picn, user_id


file_name = 'image2.sql'
IDtot = [0] * 30
tot = [0] * 30
pictot = [0] * 722
totpic = [0] * 722
picnum = 0
picname = [0] * 722
with open(file_name, mode='r', encoding='UTF-8') as f:
    for line in f.readlines():
        if line[0] != '(':
            continue
        l1 = len(line)
        info, pic_name, ID = Myfind(line, 0, l1)
        # print(len(info), pic_name, len(ID))
        l2 = len(info)  # num of people who pick the picture
        
        for i in range(l2):
            inf = info[i]
            l3 = len(inf)
            print(pic_name, ID[i], l3)
            totpic[picnum] = totpic[picnum]+1
            IDtot[int(ID[i])] = IDtot[int(ID[i])]+1
            if l3 != 11 and l3 != 12 and l3 != 21 and l3 != 23:  # invalid data
                print("\nBAD CASE!!!!!!!!!!!!!!!!")
                continue
            pictot[picnum] = pictot[picnum] + 1
            tot[int(ID[i])] = tot[int(ID[i])] + 1
            path = 'data/data/'  # the pictures' location
            pic = cv2.imread(path + pic_name, 3)
            picnn = pic_name[0:-4]
            with open('save_data/' + ID[i] + '_' + picnn + '.txt', 'w') as fxy:
                fxy.write("npoints: %d\n" % l3)
                for j in range(l3):
                    pt = inf[j]
                    r = int(pt['r'])
                    fg = l3 % 11
                    if fg == 10:
                        fg = 0
                    ix = int(pt['x'])
                    iy = int(pt['y'])
                    fxy.write("%f %f\n" % (pt['x'], pt['y']))

                    if r == 0:
                        r = r + 3
                    if j == 0:
                        cv2.circle(pic, (ix, iy), r, (255, 255, 255))
                    elif j <= 5:
                        cv2.circle(pic, (ix, iy), r, (255, 0, 0))
                    elif j <= 8:
                        cv2.circle(pic, (ix, iy), r, (0, 255, 0))
                    elif j <= 10 + fg:
                        cv2.circle(pic, (ix, iy), r, (0, 0, 255))
                    elif j <= 15 + fg:
                        cv2.circle(pic, (ix, iy), r, (255, 255, 0))
                    elif j <= 18 + fg:
                        cv2.circle(pic, (ix, iy), r, (255, 0, 255))
                    elif j <= 20 + 2 * fg:
                        cv2.circle(pic, (ix, iy), r, (0, 255, 255))
                cv2.imwrite('save_data/' + ID[i] + '_' + pic_name, pic)
        print(picnum)
        picname[picnum] = pic_name
        picnum = picnum + 1

print(IDtot)
print(tot)

sumpic = [0] * 6
for i in range(picnum):
    sumpic[totpic[i]] = sumpic[totpic[i]] + 1
print(sumpic)


sumpic = [0] * 6
for i in range(picnum):
    sumpic[pictot[i]] = sumpic[pictot[i]] + 1

print(sumpic)
for i in range(picnum):
    if (pictot[i] == 0):
        print(picname[i])

print(sum(IDtot))
print(sum(tot))
print(sum(pictot))