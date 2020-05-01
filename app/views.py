from django.shortcuts import render

# Create your views here.


def render_page(request, page_name):
    str_args = request.POST.urlencode()
    dict_args = request.POST.dict()
    context = {}

    if page_name == "byeokje_photo":
        img_list = ["files/thumbnails/394/360x300.crop.jpg",
            "files/thumbnails/392/360x300.crop.jpg",
            "files/thumbnails/390/360x300.crop.jpg",
            "files/thumbnails/203/360x300.crop.jpg",
            "files/thumbnails/201/360x300.crop.jpg",
            "files/thumbnails/199/360x300.crop.jpg",
            "files/thumbnails/197/360x300.crop.jpg",
            "files/thumbnails/194/360x300.crop.jpg",
            "files/thumbnails/192/360x300.crop.jpg",
        ]
        context["img_list"] = img_list
    elif page_name == "gimpo_photo":
        img_list = [
            "files/thumbnails/285/360x300.crop.jpg",
            "files/thumbnails/283/360x300.crop.jpg",
            "files/thumbnails/281/360x300.crop.jpg",
            "files/thumbnails/279/360x300.crop.jpg",
            "files/thumbnails/277/360x300.crop.jpg",
            "files/thumbnails/275/360x300.crop.jpg",
        ]
        context["img_list"] = img_list
    elif page_name == "yangju_photo":
        img_list = [
            "files/thumbnails/381/360x300.crop.jpg",
            "files/thumbnails/379/360x300.crop.jpg",
            "files/thumbnails/377/360x300.crop.jpg",
            "files/thumbnails/371/360x300.crop.jpg",
            "files/thumbnails/369/360x300.crop.jpg",
            "files/thumbnails/367/360x300.crop.jpg",
            "files/thumbnails/321/360x300.crop.jpg",
            "files/thumbnails/318/360x300.crop.jpg",
            "files/thumbnails/316/360x300.crop.jpg",
            "files/thumbnails/314/360x300.crop.jpg",
            "files/thumbnails/312/360x300.crop.jpg",
            "files/thumbnails/310/360x300.crop.jpg",
        ]
        context["img_list"] = img_list
    elif page_name == "namyangju_photo":
        img_list = [
            "files/thumbnails/340/360x300.crop.jpg",
            "files/thumbnails/338/360x300.crop.jpg",
            "files/thumbnails/336/360x300.crop.jpg",
            "files/thumbnails/334/360x300.crop.jpg",
            "files/thumbnails/332/360x300.crop.jpg",
            "files/thumbnails/330/360x300.crop.jpg",
        ]
        context["img_list"] = img_list

    return render(request, page_name + '.html', context)