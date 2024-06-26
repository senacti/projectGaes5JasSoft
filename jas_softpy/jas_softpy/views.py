from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from tablib import Dataset
from django.contrib.auth import logout
from production.admin import SupplieResource
from sales.models import Pays, PurchaseOrder, Sales

from production.models import ProductionOrder, SupplieProduction, Supplies
from inventory.models import Product
from postulation.models import Employed, Postulation
from suggestions.models import Suggestions

from .forms import RegisterForm
from django.contrib import messages

def custom_login_required(request):   
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('index')
        
@login_required
def home(request):
    return render(request,'home.html',{
        #context
})

@login_required
def producto(request):
    return render(request,'producto',{
        #context
})

@login_required
def rrhh(request):
    return render(request,'rrhh.html',{
        #context
    })

@login_required
def postulacion(request):
    return render(request,'postulation/Postulacion.html',{
        #context
    })

@login_required
def ordenpedido(request):
    return render(request,'ordenpedido.html',{
        #context
    })

@login_required
def insumo(request):
    return render(request,'insumo.html',{
        #context
    })

@login_required
def ofertas(request):
    return render(request,'ofertas.html',{
        #context
    })
    
def prueba(request):
    return render(request,'correo.html',{
        #context
    })


def send_email(mail):
    
    context = {'mail': mail}

    template = get_template('correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
         'Correo de prueba',
         'Primer correo JAS_SOFT',
         settings.EMAIL_HOST_USER,
         [mail],
    )

    email.attach_alternative(content, 'text/html')
    email.send()


def correo(request):
    if request.method == 'POST':
         mail = request.POST.get('mail')
         send_email(mail)
        
    return render(request,'suc.html',{})

def index(request):
    return render(request,'index.html',{
        #context
    })    

@login_required
def sales(request):
    return render(request,'sales/ventas.html',{
        #context
    })   

def login_view(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return home(request)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'login.html',{
        
})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login_jas')

def register(request):    

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password, last_name=last_name)
            if user:
                login(request, user)
                messages.success(request, 'Registro exitoso')
                return redirect('login_jas')
            
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def create_production_order(request):
    if request.method == 'POST':
        try:
            quantity_used = int(request.POST['quantity_used[]'])
            supplies_ids = request.POST.getlist('supplies_id[]')

            current_datetime = datetime.now()
           
            last_production_order = ProductionOrder.objects.last()
            if last_production_order and last_production_order.supplieProductionCode:
                last_code = int(last_production_order.supplieProductionCode)
                supplie_production_code = str(last_code + 1).zfill(5)
            else:
                supplie_production_code = "00001"

            for supplies_id in supplies_ids:
                supplies_instance = Supplies.objects.get(id=supplies_id)

                if quantity_used <= supplies_instance.stock:
                    production_order = ProductionOrder.objects.create(
                        supplieProductionCode=supplie_production_code  
                    )

                    SupplieProduction.objects.create(
                        quantity=quantity_used,
                        Production_OrderDate=current_datetime,
                        production_order=production_order,
                        supplies=supplies_instance
                    )

                    supplies_instance.stock -= quantity_used
                    supplies_instance.save()
                else:
                    messages.error(request, f'No hay suficiente stock para el insumo {supplies_instance.name}')
                    return redirect('ordenpedido') 

            messages.success(request, '¡Orden de producción creada exitosamente!')
            return redirect('ordenpedido') 

        except Exception as e:
            messages.error(request, f'Error al procesar el formulario: {str(e)}')
            return redirect('ordenpedido') 
    else:
        return render(request, 'ordenpedido.html')
                        
def edit_production_order(request, id):
        productionorder = ProductionOrder.objects.get(id=id)
        return render(request, "production/EditProductOrder.html", {"ProductionOrder": productionorder})
    
def editProductionOrder(request,id):  
    if request.method == 'POST':
        try:
            order = ProductionOrder.objects.get(id=id)
            if not order:
                messages.error(request, 'La orden de producción no existe')
                return redirect('ordenpedido')

            quantity_used = int(request.POST['quantity_used[]'])
            supplies_ids = request.POST.getlist('supplies_id[]')

            current_datetime = datetime.now()

            for supplies_id in supplies_ids:
                supplies_instance = Supplies.objects.get(id=supplies_id)

                if quantity_used <= supplies_instance.stock:
                    order.supplieProductionCode = request.POST['supplieProductionCode']  # Supongamos que también quieres editar este campo
                    order.save()

                    SupplieProduction.objects.filter(production_order=order).update(
                        quantity=quantity_used,
                        Production_OrderDate=current_datetime,
                        supplies=supplies_instance
                    )

                    supplies_instance.stock -= quantity_used
                    supplies_instance.save()
                else:
                    messages.error(request, f'No hay suficiente stock para el insumo {supplies_instance.name}')
                    return redirect('ordenpedido')

            messages.success(request, '¡Orden de producción editada exitosamente!')
            return redirect('ordenpedido')

        except Exception as e:
            messages.error(request, f'Error al procesar el formulario: {str(e)}')
            return redirect('ordenpedido')
    else:
        return render(request, 'EditProductOrder.html')
    
def deleteProductionOrder(request, id):    
    productionorder = get_object_or_404(ProductionOrder, id=id)
    productionorder.delete()
    messages.success(request, 'Orden de producción eliminada!')
    
    return redirect('ordenpedido')   

def save(self, *args, **kwargs):
        if not self.id:
            last_object = Supplies.objects.last()
            if last_object:
                self.supplieCode = last_object.supplieCode + 1
            else:
                self.supplieCode = 100001
        super(Supplies, self).save(*args, **kwargs) 

def createsupplies(request):
   
    name = request.POST['name']
    stock = int(request.POST['stock'])
    size = request.POST['size']
    color = request.POST['color']    

    supplies = Supplies.objects.create(
        name = name, 
        stock = stock, 
        size = size,
        color = color,
    )
    
    messages.success(request, '¡el insumo se registro exitosamente!')
    return redirect('insumo')

def editsupplies(request, id):
    supplies = Supplies.objects.get(id=id)
    return render(request, "supplies/EditSupplies.html", {"Supplies":supplies})
    
@require_POST
def EditSupplies(request, id):
    if request.method == 'POST':
        supplies = get_object_or_404(Supplies, id=id)
        supplies.name = request.POST.get('name', '')
        supplies.stock = int(request.POST.get('stock', 0))
        supplies.size = request.POST.get('size', '')
        supplies.color = request.POST.get('color', '')       
        supplies.save()
        messages.success(request, '¡El insumo se ha actualizado!')
    else:
        messages.error(request, 'La solicitud no es válida.')

    return redirect('insumo')
    
def deleteSupplies(request, id):
    
    supplies = Supplies.objects.get(pk=id)
    supplies.delete()    
    messages.success(request, 'Orden de producción eliminado!')
    return redirect('insumo') 

def import_supplies(request):
    if request.method == 'POST':
        supplie_resource = SupplieResource()
        dataset = Dataset()
        new_supplies = request.FILES['myfile']

        import_supplies = dataset.load(new_supplies.read(), format='xlsx')
        result = supplie_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            supplie_resource.import_data(dataset, dry_run=False)
            messages.success(request, 'Los datos se han importado correctamente.')
            return HttpResponseRedirect(reverse('insumo'))
        else:
            messages.error(request, 'Hubo un error al importar los datos.')
            return render(request, 'production/insumo.html')
    else:
        return render(request, 'production/insumo.html')

def export_supplies(request):
    
    supplie_resource = SupplieResource()
    dataset = supplie_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="supplies.xlsx"'
    return response
    
def createinventory(request):
    if request.method == 'POST':     
        name = request.POST.get('name')
        stock = request.POST.get('stock')
        current_datetime = datetime.now()
        size = request.POST.get('size')
        color = request.POST.get('color')
        state = request.POST.get('state')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        inventory = Product.objects.create(
            name = name, 
            stock = stock, 
            size = size,
            color = color,
            state = state,
            category = category,
            image = image,
            fabricationDate = current_datetime 
        )
    
    messages.success(request, '¡el producto se registro exitosamente!')
    return redirect('producto')

def editinventory(request, id):
    producto = Product.objects.get(id=id)    
    return render(request, "inventory/editInventory.html", {"Product":producto})

@require_POST
def EditInventory(request, id):       
    if request.method == 'POST':
        producto = get_object_or_404(Product, id=id)
        producto.name = request.POST.get('name','')
        producto.stock = int(request.POST.get('stock', 0)) 
        producto.size = request.POST.get('size', '')
        producto.color = request.POST.get('color', '')
        producto.state = request.POST.get('state', '')
        producto.category = request.POST.get('category', '')     
        producto.save()
        messages.success(request, '¡El producto se ha actualizado!')
    else:
        messages.error(request, '¡La solicitud no es valida!')
    
    return redirect('producto')

def deleteinventory(request, id):
    
    producto = Product.objects.get(pk=id)
    producto.delete()    
    messages.success(request, 'Producto eliminado!')
    return redirect('producto')

def create_postulation(request):

    if request.method == 'POST':
        start_offers = datetime.now()
        descrip_offer = request.POST['descripOffer']
        profile_postulation = request.POST['profilePostulation']
        state_postulations = request.POST['StatePostulations']    

        postulation = Postulation.objects.create(
            startOffers = start_offers, 
            descripOffer = descrip_offer, 
            profilePostulation = profile_postulation,
            StatePostulations = state_postulations,
        )
        messages.success(request, '¡La postulación se registró exitosamente!')
        return redirect('Postulacion')

def editpostulation(request, id):
    postulacion = Postulation.objects.get(id=id)    
    return render(request, "postulation/editPostulation.html", {"Postulation":postulacion})

@require_POST
def EditPostulation(request, id):       
    if request.method == 'POST':
        postulacion = get_object_or_404(Postulation, id=id)
        postulacion.descripOffer = request.POST.get('descripOffer', '')
        postulacion.profilePostulation = request.POST.get('profilePostulation', '')
        postulacion.StatePostulations = request.POST.get('StatePostulations', '')
        postulacion.save()
        messages.success(request, '¡La postulación se ha actualizado!')
    else:
        messages.error(request, '¡La solicitud no es valida!')
    
    return redirect('Postulacion')

def deletepostulation(request, id):
    
    postulacion = get_object_or_404(Postulation, pk=id)
    postulacion.delete()    
    messages.success(request, 'Postulación eliminada!')
    return redirect('Postulacion')

def create_sales(request):
    if request.method == 'POST':        
        saleDate = datetime.now()
        saleAmount = request.POST['saleAmount']
        saleSubAmount = request.POST['saleSubAmount']
        saleIvaAmount = request.POST['saleIvaAmount']        
        employed_id = request.POST.get('employed_id')
        pays_id = request.POST.get('pays_id')
        purchaseOrder_id = request.POST.get('purchaseOrder_id')

        employed_instance = Employed.objects.get(id=employed_id) 
        pays_instance = Pays.objects.get(id=pays_id)
        purchaseOrder_instance = PurchaseOrder.objects.filter(id=purchaseOrder_id).first()

        Sales.objects.create(            
            saleDate=saleDate,
            saleAmount=saleAmount,
            saleSubAmount=saleSubAmount,
            saleIvaAmount=saleIvaAmount,            
            employed=employed_instance,  
            pays=pays_instance,
            purchaseOrder=purchaseOrder_instance,            
        )
       
        """try:
            
            product_id = request.POST.get('product')
            product_instance = Product.objects.get(id=product_id)

            quantity_sold = int(request.POST.get('stockProduct'))

            if product_instance.stock >= quantity_sold:
                product_instance.stock -= quantity_sold
                product_instance.save()
            else:
                messages.error(request, f"No hay suficiente stock disponible para el producto {product_instance.name}")
                sale_instance.delete()
                return redirect('ventas')  

        except Product.DoesNotExist:            
            messages.error(request, "El producto asociado a la venta no existe")            
            sale_instance.delete()
            return redirect('ventas')  """

        messages.success(request, '¡La venta se registró exitosamente!')
        return redirect('ventas')
    else:        
        iva_choices = Sales.IVA_CHOICES
        return render(request, 'tu_template.html', {'iva_choices': iva_choices})

    
def editsales(request, id):
    sales = Sales.objects.get(id=id)    
    return render(request, "Sales/editSales.html", {"Sales":sales})

@require_POST
def EditSales(request, id):       
    if request.method == 'POST':
        sales = get_object_or_404(Sales, id=id)        
        print(request.POST,"---------")
        
               
        
        sales.saleAmount = request.POST.get('saleAmount', '')
        sales.saleSubAmount = request.POST.get('saleSubAmount', '')
        sales.saleIvaAmount = request.POST.get('saleIvaAmount', '')
       
        sales.save()
        messages.success(request, '¡La venta se ha actualizado!')
        print("Venta actualizada:", sales) 
    else:
        messages.error(request, '¡La solicitud no es válida!')
    
    return redirect('ventas')

def deletesales(request, id):
    
    sales = Sales.objects.get(pk=id)
    sales.delete()    
    messages.success(request, 'Postulación eliminada!')
    return redirect('ventas')


from django.contrib import messages

def create_suggestion(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        descriptCategory = request.POST.get('descriptCategory')
        
        suggestion = Suggestions.objects.create(
            category=category,
            descriptCategory=descriptCategory
        )
        
        messages.success(request, '¡La sugerencia se registró exitosamente!')
        return redirect('sugerencias')
    


def editsuggestion(request, id):
    sugerencia = get_object_or_404(Suggestions, id=id)    
    return render(request, "suggestions/editSuggestions.html", {"Sugerencia": sugerencia})

@require_POST
def EditSuggestion(request, id):
    sugerencia = get_object_or_404(Suggestions, id=id)
    sugerencia.category = request.POST.get('category', '')
    sugerencia.descriptCategory = request.POST.get('descriptCategory', '')
    sugerencia.save()
    messages.success(request, '¡La sugerencia se ha actualizado!')
    return redirect('sugerencias')

def deletesuggestion(request, id):
    sugerencia = get_object_or_404(Suggestions, pk=id)
    sugerencia.delete()    
    messages.success(request, 'Sugerencia eliminada!')
    return redirect('sugerencias')