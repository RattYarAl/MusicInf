from django.core.paginator import Paginator


def pages(request, music_list, music_numb):
    paginator = Paginator(music_list, music_numb)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
