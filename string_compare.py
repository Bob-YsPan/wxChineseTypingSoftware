answer = '君不見黃河之水天上來'
userin = '不見君黃河之水天上來'
answer_mod = []
userin_mod = []
correct_list = []
err_unchk_li = []

answer_mod.append(answer)
userin_mod.append(userin)

answer_input = answer_mod[0]
userin_input = userin_mod[0]
first_run = True
# 檢查正確字
# 先比較誰比較短
check_count = -1
if answer_input >= userin_input:
    check_count = len(userin_input)
else:
    check_count = len(answer_input)
# 邏輯：
# 由左到右，把正確的字抓出來(上下相同字)，並從那邊把字串切成幾個小區段
str_index = 0
for i in range(check_count):
    # print(answer[i:i+1])
    if answer_input[i:i + 1] == userin_input[i:i + 1]:
        mod_index = len(answer_mod) - 1
        print('mod index = ' + str(mod_index))
        print('append = ' + answer_mod[mod_index][str_index + 1:])
        answer_mod.append(answer_mod[mod_index][str_index + 1:])
        userin_mod.append(userin_mod[mod_index][str_index + 1:])
        print(answer_mod)
        print(userin_mod)
        if answer_mod[mod_index][:str_index] == '':
            answer_mod.pop(mod_index)
            userin_mod.pop(mod_index)
        else:
            print('modify = ' + answer_mod[mod_index][:str_index])
            answer_mod[mod_index] = answer_mod[mod_index][:str_index]
            userin_mod[mod_index] = userin_mod[mod_index][:str_index]
        str_index = 0
        # 如果第一次跑，產生List
        if first_run:
            correct_list.append(i)

    else:
        str_index = str_index + 1
        if first_run:
            err_unchk_li.append(i)
    print(answer_mod)
    print(userin_mod)
    print(correct_list)
    print(err_unchk_li)

if answer_mod[len(answer_mod) - 1] == '' and userin_mod[len(userin_mod) - 1 == '']:
    answer_mod.pop(len(answer_mod) - 1)
    userin_mod.pop(len(userin_mod) - 1)
    print(answer_mod)
    print(userin_mod)
    print(correct_list)
    print(err_unchk_li)

