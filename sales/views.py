from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from common.models import Customer

html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
            <th>id</th>
            <th>姓名</th>
            <th>电话号码</th>
            <th>地址</th>
        </tr>
        
        {% for customer in customers %}
            <tr>
            
            {% for name, value in customer.items %}
                <td>{{ value }}</td>
            {% endfor %}
                   
            </tr>
        {% endfor %}
            
        </table>
    </body>
</html>
'''

from django.template import engines

django_engine = engines['django']
template = django_engine.from_string(html_template)


def listcustomers(request):
    # ----返回一个QuerySet对象，包含所有的表的记录
    # ----每一个表记录都是一个dict对象
    qs = Customer.objects.values()

    # ----检查request中是否存在phonenumber的参数,若无返回None
    ph = request.GET.get('phonenumber', None)
    if ph:
        qs = qs.filter(phonenumber=ph)

    # 传入渲染模板所需要的参数
    rendered = template.render({'customers': qs})

    return HttpResponse(rendered)
