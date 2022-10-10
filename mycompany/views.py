from django.shortcuts import render
from .models import *
from django.views.decorators.cache import cache_page


# Create your views here.
"""主页"""

@cache_page(50 * 15)
def index(request):

    # 获取banner图
    banners = Banner.objects.values('banner_show_photo')
    result_banner_arr = []
    for inx in range(0, len(banners)):
        path = '/media/' + banners[inx]['banner_show_photo']
        # path = banners[inx]['banner_show_photo']
        result_banner_arr.append(path)

    # 获取栏目表
    catgory_arr_result = getCategory()

    # 获取公司信息
    mes = CompanyContact.objects.all()

    result_banner_dic = {
                            'banner': result_banner_arr,
                            'category': catgory_arr_result,
                            'mes': mes[0]
                        }

    return render(request, 'index.html', result_banner_dic)


"""项目介绍"""
@cache_page(50 * 15)
def product(request,idx):
    print('--传值 ---', idx)
    index_id = request.GET.get('index_id')
    print('页面index ', index_id)
    # 获取栏目表
    catgory_arr_result = getCategory()
    # 根据id 获取子栏目
    sub_cate = SubCategory.objects.filter(category_id=idx)

    for vlaue in sub_cate:
        print('子项目ID:', vlaue.id)

    # 获取公司信息
    mes = CompanyContact.objects.all()

    if int(index_id) == 3:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 0
        }
    elif int(index_id) == 4:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 1
        }
    elif int(index_id) == 5:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 2
        }
    else:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 3
        }
    return render(request, 'product.html', result_dic)

"""职业发展"""
@cache_page(50 * 15)
def job(request, idx):
    print('--传值 ---', idx)
    index_id = request.GET.get('index_id')
    print('页面index ', index_id)
    # 获取栏目表
    catgory_arr_result = getCategory()

    # 根据id 获取子栏目
    sub_cate = SubCategory.objects.filter(category_id=idx)

    for vlaue in sub_cate:
        print('子项目ID:', vlaue.id)
    # li = []
    # for index_li in range(0, len(sub_cate)):
    #     print('ittt--->', index_li)
    #     li.append(index_li)
    # 获取公司信息
    mes = CompanyContact.objects.all()

    if int(index_id) == 7:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 0
        }
    else:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 1
        }

    return render(request, 'job.html', result_dic)

"""联系我们"""
@cache_page(50 * 15)
def contact(request, idx):
    print('--传值 ---', idx)
    index_id = request.GET.get('index_id')
    print('页面index ', index_id)
    # 获取栏目表
    catgory_arr_result = getCategory()

    # 根据id 获取子栏目
    sub_cate = SubCategory.objects.filter(category_id=idx)

    for vlaue in sub_cate:
        print('子项目ID:', vlaue.id)
    # li = []
    # for index_li in range(0, len(sub_cate)):
    #     print('ittt--->', index_li)
    #     li.append(index_li)
    # 获取公司信息
    mes = CompanyContact.objects.all()

    if int(index_id) == 9:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 0
        }
    else:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 1
        }

    return render(request, 'contactus.html', result_dic)

"""关于我们"""
@cache_page(50 * 15)
def about(request, idx):
    print('--传值 ---', idx)
    index_id = request.GET.get('index_id')
    print('页面index ', index_id)
    # 获取栏目表
    catgory_arr_result = getCategory()

    # 根据id 获取子栏目
    sub_cate = SubCategory.objects.filter(category_id=idx)
    # li = []
    # for index_li in range(0, len(sub_cate)):
    #     print('ittt--->', index_li)
    #     li.append(index_li)
    # 获取公司信息
    mes = CompanyContact.objects.all()

    if int(index_id) == 1:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 0
        }
    else:
        result_dic = {
            'category': catgory_arr_result,
            'mes': mes[0],
            'sub_cate': sub_cate,
            'index_id': 1
        }

    return render(request, 'aboutus.html', result_dic)

# 获取栏目
def getCategory():
    catgory_set = Category.objects.all().order_by('-sort')
    catgory_arr_result = []
    for object1 in catgory_set:
        # print('id :', object1.id)
        # print(object1.id)
        # print(object1.show_image_pc_in)
        temp_dic = {}
        temp_dic.__setitem__('id', object1.id)
        temp_dic.__setitem__('title', object1.title)
        temp_dic.__setitem__('tag_title', object1.tag_title)
        if len(object1.show_image_pc_index) > 0:
            temp_dic['show_image_pc_index'] = '/media/' + str(object1.show_image_pc_index)

        if len(object1.show_image_m_in) > 0:
            temp_dic['show_image_m_in'] = '/media/' + str(object1.show_image_m_in)

        if len(object1.show_image_pc_in) > 0:
            temp_dic['show_image_pc_in'] = '/media/' + str(object1.show_image_pc_in)

        temp_dic['des'] = ''
        if object1.tag_des:
            arr = object1.tag_des.split(',')
            temp_dic['des'] = arr
        catgory_arr_result.append(temp_dic)
    return catgory_arr_result
