from django.shortcuts import render

# Create your views here.
def article(request):
    '''
    render the article page
    :param request:
    :return:
    '''
    return render(request, 'article.html', locals())