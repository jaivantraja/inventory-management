from django.shortcuts import render
from main_page.models import Purchase
from main_page.models import Inventory
from main_page.models import Sales
# Create your views here.
def purchase_page(request):
    purchase_list = Purchase.objects.all()
    return render(request, 'purchases_page.html', {'purchase_items': purchase_list})

def make_purchase(request):
    inventory_entry = None
    if request.method == 'POST':
        gst_number = request.POST.get('gst_number')
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity'))
        cost = float(request.POST.get('cost'))
        total_cost = cost*quantity

        purchase = Purchase.objects.create(
            gst_number=gst_number,
            product_name=product_name,
            quantity=quantity,
            cost=cost,
            total_cost=total_cost,
        )

        inventory_entry = Inventory.objects.filter(gst_number=gst_number, product_name=product_name).exists()

        if inventory_entry:
            inventory_entry=Inventory.objects.get(gst_number=gst_number, product_name=product_name)
            inventory_entry.quantity += quantity
            inventory_entry.save()

        else:
            inventory = Inventory.objects.create(
                gst_number=gst_number,
                product_name=product_name,
                quantity=quantity,
                cost=cost,
            )
        purchase_list = Purchase.objects.all()
        return render(request, 'purchases_page.html',{'purchase_items': purchase_list})

def sales_page(request):
    sales_list = Sales.objects.all()
    return render(request, 'sales_page.html', {'sales_items': sales_list})

def make_sale(request):
    if request.method == 'POST':
        gst_number = request.POST.get('gst_number')
        product_name = request.POST.get('product_name')
        quantity = int(request.POST.get('quantity'))
        sender_gst = request.POST.get('sender_gst_number')

        product = Inventory.objects.get(gst_number=gst_number, product_name=product_name)
        cost = int(product.cost)
        total_cost = float(product.cost)*quantity

        if product.quantity >= quantity:

            product.quantity -= quantity
            product.save()

            sale = Sales.objects.create(
                gst_number=gst_number,
                product_name=product_name,
                quantity=quantity,
                cost=cost,
                total_cost=total_cost,
                sender_gst=sender_gst,
            )
            sales_list = Sales.objects.all()
            return render(request, 'sales_page.html', {'sales_items': sales_list})
def inventory_page(request):
    inventory_list = Inventory.objects.all()
    return render(request, 'inventory_page.html', {'inventory_items': inventory_list})









