from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myworldcup.models import WorldCupTeam

# Create your views here.
# 获取所有数据和小组数据
team_list = WorldCupTeam.objects.all()
def team_index(request):
    # 生成paginator对象,定义每页显示4条记录
    paginator = Paginator(team_list, 4)
    # 从前端获取当前的页码数
    page = request.GET.get('page')
    try:
        # 获取当前页码的记录
        teams = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户输入的页码不是整数时,显示第1页的内容
        teams = paginator.page(1)
    except EmptyPage:
        # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        teams = paginator.page(paginator.num_pages)
    # 返回index.html页面
    return render(request,'myworldcup/index.html', {'teams' : teams,})

def GD_index(request):
    # 获取每个小组净胜球最多的组别，存到bestGD中
    best = 0
    bestGD = []
    # 约束组别开头为A，只取净胜球
    teamA_GD = WorldCupTeam.objects.values_list('GD',flat=True).filter(group__regex='A.*')
    # 获取的循环次数与组别的数字部分相同
    for count,team in enumerate(teamA_GD):
        if team > best:
            best = count+1
    s='A%d'%best
    bestGD.append(s)
    best=0
    teamB_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='B.*')
    for count, team in enumerate(teamB_GD):
        if team > best:
            best = count + 1
    s = 'B%d' % best
    bestGD.append(s)
    best = 0
    teamC_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='C.*')
    for count, team in enumerate(teamC_GD):
        if team > best:
            best = count + 1
    s = 'C%d' % best
    bestGD.append(s)
    best = 0
    teamD_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='D.*')
    for count, team in enumerate(teamD_GD):
        if team > best:
            best = count + 1
    s = 'D%d' % best
    bestGD.append(s)
    best = 0
    teamE_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='E.*')
    for count, team in enumerate(teamE_GD):
        if team > best:
            best = count + 1
    s = 'E%d' % best
    bestGD.append(s)
    best = 0
    teamF_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='F.*')
    for count, team in enumerate(teamF_GD):
        if team > best:
            best = count + 1
    s = 'F%d' % best
    bestGD.append(s)
    best = 0
    teamG_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='G.*')
    for count, team in enumerate(teamG_GD):
        if team > best:
            best = count + 1
    s = 'G%d' % best
    bestGD.append(s)
    best = 0
    teamH_GD = WorldCupTeam.objects.values_list('GD', flat=True).filter(group__regex='H.*')
    for count, team in enumerate(teamH_GD):
        if team > best:
            best = count + 1
    s = 'H%d' % best
    bestGD.append(s)
    return render(request,'myworldcup/GD.html', {
        'team_list' : team_list,
        'bestGD' : bestGD,
    })

#     def different_index(request):
# #     # 获取每场比赛最高分差的三场，存入列表中，字典存入分差最高的下标
# #     best = 0
# #     better = 0
# #     good = 0
# #     score = []
# #     different = {}
# #     # 把所有比赛的敌我得分存到列表中
# #     firstscore = WorldCupTeam.objects.values_list('firstgame_score', flat=True)
# #     secondscore = WorldCupTeam.objects.values_list('second_score', flat=True)
# #     thirdscore = WorldCupTeam.objects.values_list('thirdgame_score', flat=True)
# #     firstcompetitor = WorldCupTeam.objects.values_list('firstgame_competitor', flat=True)
# #     secondcompetitor = WorldCupTeam.objects.values_list('secondegame_competitor', flat=True)
# #     thirdcompetitor = WorldCupTeam.objects.values_list('thirdgame_competitor', flat=True)
# #     # 将列表转换成numpy数组，进行相减
# #     first_score = numpy.array(firstscore)
# #     second_score = numpy.array(secondscore)
# #     third_score = numpy.array(thirdscore)
# #     first_competitor = numpy.array(firstcompetitor)
# #     second_competitor = numpy.array(secondcompetitor)
# #     third_competitor = numpy.array(thirdcompetitor)
# #     array1 = first_score-first_competitor
# #     array2 = second_score-second_competitor
# #     array3 = third_score-third_competitor
# #     # 取分差最大三场比赛的分差和下标
# #     for count, game in enumerate(array1):
# #         if game > best | game < -best:
# #             good = better
# #             better = best
# #             best = game
# #             while count != 0 :
# #                 different[game]=count+1
# #     score.append(best)
# #     score.append(better)
# #     score.append(good)
# #     best = 0
# #     better = 0
# #     good = 0
# #     for count, game in enumerate(array2):
# #         if game > best | game < -best:
# #             good = better
# #             better = best
# #             best = game
# #             while count != 0 :
# #                 different.append(count+1)
# #     score.append(best)
# #     score.append(better)
# #     score.append(good)
# #     best = 0
# #     better = 0
# #     good = 0
# #     for count, game in enumerate(array3):
# #         if game > best | game < -best:
# #             good = better
# #             better = best
# #             best = game
# #             while count != 0 :
# #                 different.append(count+1)
# #     score.append(best)
# #     score.append(better)
# #     score.append(good)
# #     # 在之前存的九场分差最大的比赛挑出三场分差最大的
# #     for finaldifferent in score:
# #         if finaldifferent > good | finaldifferent < -good:
# #             good = finaldifferent
# #             if finaldifferent > better | finaldifferent < -better:
# #                 good = better
# #                 better = finaldifferent
# #                 if finaldifferent > best | finaldifferent < -best:
# #                     good = better
# #                     better = best
# #                     best = finaldifferent
# #     # 通过分差在字典中找到下标，把下标转换为组别
# #     best_game = different[best]
# #     better_game = different[better]
# #     good_game = different[good]
# #     game1=get_ABC(best_game)
# #     game2=get_ABC(better_game)
# #     game3=get_ABC(good_game)
#      return render(request, 'myworldcup/different.html', {
#          'team_list': team_list,
# #         'game1':  game1,
# #         'game2': game2,
# #        'game3': game3,
#      })

def advance_index(request):
    # 获取每个小组积分最多的两个组别，存到advance中
    best = 0
    good = 0
    advance = []
    # 约束组别开头为A，只取积分
    teamA_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='A.*')
    # 获取的循环次数与组别的数字部分相同，取积分最高的两个组别
    for count, team in enumerate(teamA_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'A%d' % best
    g = 'A%d' %good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamB_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='B.*')
    for count, team in enumerate(teamB_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'B%d' % best
    g = 'B%d' % good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamC_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='V.*')
    for count, team in enumerate(teamC_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'C%d' % best
    g = 'C%d' % good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamD_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='D.*')
    for count, team in enumerate(teamD_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'D%d' % best
    g = 'D%d' % good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamE_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='E.*')
    for count, team in enumerate(teamE_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'E%d' % best
    g = 'E%d' % good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamF_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='F.*')
    for count, team in enumerate(teamF_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'F%d' % best
    g = 'F%d' % good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamG_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='G.*')
    for count, team in enumerate(teamG_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'G%d' % best
    g = 'G%d' % good
    advance.append(b)
    advance.append(g)
    best = 0
    good = 0
    teamH_integral = WorldCupTeam.objects.values_list('integral', flat=True).filter(group__regex='H.*')
    for count, team in enumerate(teamH_integral):
        if team > best:
            good = best
            best = count + 1
    b = 'H%d' % best
    g = 'H%d' % good
    advance.append(b)
    advance.append(g)

    return render(request, 'myworldcup/advance.html', {
        'team_list': team_list,
        'advance' : advance,
    })

# 把下标转为组别
def get_ABC(x):
    if x <= 4:
        y = 'A%d' % x
        return y
    elif x <=8:
        x = x-4
        y = 'B%d' %x
        return y
    elif x <=12:
        x = x-8
        y = 'C%d' %x
        return y
    elif x <=16:
        x = x-12
        y = 'D%d' %x
        return y
    elif x <=20:
        x = x-16
        y = 'E%d' %x
        return y
    elif x <=24:
        x = x-20
        y = 'F%d' %x
        return y
    elif x <=28:
        x = x-24
        y = 'G%d' %x
        return y
    elif x <=32:
        x = x-28
        y = 'H%d' %x
        return y

