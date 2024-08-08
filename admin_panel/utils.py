from django.http import HttpResponse

def check_staff(input_func):    
    def output_func(*args):
        if args[0].user.is_staff is True: 
            return input_func(*args)                
        else:
            return HttpResponse("<h1>Страница не найдена</h1>", status=404)
    return output_func 