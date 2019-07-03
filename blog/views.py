from django.shortcuts import render

# Create your views here.
posts = [
        {
            'title':'this is a title for test',
            'author':'shahrooz mohammadloo', 
            'date_posted':'April, 2, 2019', 
            'content':'Amet ducimus maiores delectus accusamus velit illo Fugiat ratione et placeat impedit blanditiis Ipsa voluptatem ullam maiores perspiciatis aliquam. A mollitia fuga veritatis unde sint Sed deleniti tenetur consequatur facilis?',


            },
        {
            'title':'Second title for tesst',
            'author':'Alex toxin', 
            'date_posted':'Augost, 8, 2019', 
            'content':'Amet ducimus maiores delectus accusamus velit illo Fugiat ratione et placeat impedit blanditiis Ipsa voluptatem ullam maiores perspiciatis aliquam. A mollitia fuga veritatis unde sint Sed deleniti tenetur consequatur facilis?',


            }
        ]

def index(request):
    domy = {'posts':posts}
    return render(request, 'blog/index.html', domy)



def about(request):
    return render(request, 'blog/about.html')
